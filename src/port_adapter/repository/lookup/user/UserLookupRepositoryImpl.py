"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.common.model.UserIncludesOrganizationsAndRoles import UserIncludesOrganizationsAndRoles
from src.domain_model.project.Project import Project
from src.port_adapter.repository.db_model.role__project__junction import ROLE__PROJECT__JUNCTION
from src.port_adapter.repository.lookup.common.sql.SqlLookupBaseRepository import SqlLookupBaseRepository
from typing import List

from sqlalchemy.inspection import inspect
from sqlalchemy.sql.expression import text

from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from src.application.lookup.user.UserLookup import UserLookup
from src.application.lookup.user.UserLookupRepository import UserLookupRepository
from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.resource.exception.UserDoesNotExistException import (
    UserDoesNotExistException,
)
from src.domain_model.role.Role import Role
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.token.TokenData import TokenData
from src.domain_model.user.User import User
from src.domain_model.user.UserRepository import UserRepository
from src.port_adapter.repository.db_model.Organization import (
    Organization as DbOrganization,
)
from src.port_adapter.repository.db_model.Role import Role as DbRole
from src.port_adapter.repository.db_model.Project import Project as DbProject
from src.port_adapter.repository.db_model.User import User as DbUser
from src.port_adapter.repository.db_model.role__organization__junction import (
    ROLE__ORGANIZATION__JUNCTION,
)
from src.port_adapter.repository.db_model.user__role__junction import (
    USER__ROLE__JUNCTION,
)
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger


class UserLookupRepositoryImpl(SqlLookupBaseRepository, UserLookupRepository):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi

        self._roleRepo: RoleRepository = AppDi.instance.get(RoleRepository)
        self._userRepo: UserRepository = AppDi.instance.get(UserRepository)
        self._organizationRepo: OrganizationRepository = AppDi.instance.get(
            OrganizationRepository
        )

        self._dbUserColumnsMapping = inspect(DbUser).c
        self._dbRoleColumnsMapping = inspect(DbRole).c
        self._dbProjectColumnsMapping = inspect(DbProject).c
        self._dbOrganizationColumnsMapping = inspect(DbOrganization).c

    @debugLogger
    def userLookupByUserId(self, id: str) -> UserLookup:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        userLookup = UserLookup()

        dbObject = dbSession.query(DbUser).filter_by(id=id).first()
        if dbObject is None:
            raise UserDoesNotExistException(f"id = {id}")
        user = self._userFromDbObject(dbItemResult=dbObject, usePrefix=False)
        userLookup.addUser(user)

        organizations = {}
        for role in dbObject.roles:
            userLookup.addRole(self._roleFromDbObject(role, usePrefix=False))
            for org in role.organizations:
                organizations[org.id] = org

        for org in organizations.values():
            userLookup.addOrganization(self._organizationFromDbObject(org, usePrefix=False))

        return userLookup

    @debugLogger
    def userLookupByUserEmail(self, email: str) -> UserLookup:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        userLookup = UserLookup()

        dbObject = dbSession.query(DbUser).filter_by(email=email).first()
        if dbObject is None:
            raise UserDoesNotExistException(f"id = {email}")
        user = self._userFromDbObject(dbItemResult=dbObject, usePrefix=False)

        userLookup.addUser(user)

        organizations = {}
        for role in dbObject.roles:
            userLookup.addRole(self._roleFromDbObject(role, usePrefix=False))
            for org in role.organizations:
                organizations[org.id] = org

        for org in organizations.values():
            userLookup.addOrganization(self._organizationFromDbObject(org, usePrefix=False))

        return userLookup

    @debugLogger
    def lookup(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
        filter: List[dict] = None,
    ) -> dict:
        # logger.debug(dbSession.query(DbUser)\
        #     .options(joinedload(DbUser.organizations), joinedload(DbUser.roles))\
        #     .order_by(text('user.email'))\
        #     .limit(resultSize).offset(resultFrom).statement)

        dbSession = ApplicationServiceLifeCycle.dbContext()
        sortData = ""
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]

        sortData = sortData.replace("user.", "user_")
        sortData = sortData.replace("role.", "role_")
        sortData = sortData.replace("organization.", "organization_")
        if sortData != "":
            sortData = f"ORDER BY {sortData}"

        filterData = self._constructFiltering(filter)

        userCols = ",".join(
            [f"user.{x.name} AS user_{x.name}" for x in self._dbUserColumnsMapping]
        )
        roleCols = ",".join(
            [f"role.{x.name} AS role_{x.name}" for x in self._dbRoleColumnsMapping]
        )
        projectCols = ",".join(
            [f"project.{x.name} AS project_{x.name}" for x in self._dbProjectColumnsMapping]
        )
        orgCols = ",".join(
            [
                f"organization.{x.name} AS organization_{x.name}"
                for x in self._dbOrganizationColumnsMapping
            ]
        )
        selectCols = f"{userCols},{roleCols},{orgCols},{projectCols}"

        sql = f"""FROM user
                    LEFT OUTER JOIN
                        {USER__ROLE__JUNCTION} user__role__junc ON user.id = user__role__junc.user_id
                    LEFT OUTER JOIN
                        role ON role.id = user__role__junc.role_id
                    LEFT OUTER JOIN
                        {ROLE__ORGANIZATION__JUNCTION} role__org__junc ON role.id = role__org__junc.role_id
                    LEFT OUTER JOIN
                        organization ON organization.id = role__org__junc.organization_id
                    LEFT OUTER JOIN
                        {ROLE__PROJECT__JUNCTION} role__project__junc ON role.id = role__project__junc.role_id
                    LEFT OUTER JOIN
                        project ON project.id = role__project__junc.project_id 
                """

        dbItemsResult = dbSession.execute(
            text(f"SELECT {selectCols} {sql}\n{filterData}\n{sortData}\nLIMIT {resultSize} OFFSET {resultFrom}")
        )

        dbObjectsCount = dbSession.execute(
            text(f"SELECT count(1) FROM (SELECT count(1) {sql}\n{filterData} GROUP BY user.id) t")
        ).scalar()
        result = {"items": [], "totalItemCount": dbObjectsCount}

        userLookupsDict = {}

        for dbItemResult in dbItemsResult:
            user = self._userFromDbObject(dbItemResult=dbItemResult)
            if user.id() not in userLookupsDict:
                userLookup = UserLookup()
                userLookup.addUser(user)
                userLookupsDict[user.id()] = userLookup

                org: Organization = self._organizationFromDbObject(
                    dbItemResult=dbItemResult
                )
                role: Role = self._roleFromDbObject(dbItemResult=dbItemResult)
                project: Project = self._projectFromDbObject(dbItemResult=dbItemResult)
                if org is not None:
                    userLookup.addOrganization(
                        self._organizationFromDbObject(dbItemResult=dbItemResult)
                    )
                if role is not None:
                    userLookup.addRole(
                        self._roleFromDbObject(dbItemResult=dbItemResult)
                    )
                if project is not None:
                    userLookup.addProject(
                        self._projectFromDbObject(dbItemResult=dbItemResult)
                    )
                result["items"].append(userLookup)
            else:
                userLookup = userLookupsDict[user.id()]
                org: Organization = self._organizationFromDbObject(
                    dbItemResult=dbItemResult
                )
                role: Role = self._roleFromDbObject(dbItemResult=dbItemResult)
                project: Project = self._projectFromDbObject(dbItemResult=dbItemResult)
                if project is not None:
                    userLookup.addProject(
                        self._projectFromDbObject(dbItemResult=dbItemResult)
                    )
                if org is not None:
                    userLookup.addOrganization(
                        self._organizationFromDbObject(dbItemResult=dbItemResult)
                    )
                if role is not None:
                    userLookup.addRole(
                        self._roleFromDbObject(dbItemResult=dbItemResult)
                    )
        return result

    @debugLogger
    def usersFilteredByUsersIncludeOrganizationsAndRoles(
            self,
            tokenData: TokenData,
            resultFrom: int = 0,
            resultSize: int = 10,
            order: List[dict] = None,
            filter: List[dict] = None,
            usersIncludeOrganizationsAndRoles: List[UserIncludesOrganizationsAndRoles] = None,
    ) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        sortData = ""
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]

        # Users and count
        query = (
            dbSession.query(DbUser)
                .filter(DbUser.id.in_([x.user().id() for x in usersIncludeOrganizationsAndRoles]))
        )
        for filterItem in filter:
            filterString = self._constructFilterItemByKeyword(filterItem=filterItem, keyword="")
            if filterString is not None:
                query = query.filter(text(filterString))
        users = query.order_by(text(sortData)).all()
        # itemsCount = query.count()

        # Organizations
        query = (
            dbSession.query(DbOrganization)
                .filter(
                DbOrganization.id.in_(
                    [x2.id() for x1 in usersIncludeOrganizationsAndRoles for x2 in x1.organizations()]
                )
            )
        )
        for filterItem in filter:
            filterString = self._constructFilterItemByKeyword(filterItem=filterItem, keyword="organizations.", keywordReplacementInKey="organization.")
            if filterString is not None:
                query = query.filter(text(filterString))
        organizations = query.all()
        items = self._itemsByUserIncludesOrganizationsAndRoles(
            dbOrganizations=organizations,
            dbUsers=users,
            usersIncludeOrganizationsAndRoles=usersIncludeOrganizationsAndRoles,
        )

        items = self._filterEmptyOrganizations(items)

        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": items[resultFrom: resultFrom + resultSize],
            "totalItemCount": len(items),
        }

    def _filterEmptyOrganizations(self, items: List[UserIncludesOrganizationsAndRoles]):
        result = {}
        for item in items:
            if item.organizations() and item.user().id() not in result:
                result[item.user().id()] = item
        return list(result.values())


    def _itemsByUserIncludesOrganizationsAndRoles(
        self,
        dbOrganizations,
        dbUsers,
        usersIncludeOrganizationsAndRoles: List[UserIncludesOrganizationsAndRoles],
    ):
        items = []

        for dbUser in dbUsers:
            for userIncludesOrganizationsAndRoles in usersIncludeOrganizationsAndRoles:
                if dbUser.id == userIncludesOrganizationsAndRoles.user().id():
                    newItem = UserIncludesOrganizationsAndRoles(
                        user=self._userFromDbObject(dbUser, usePrefix=False)
                    )
                    [newItem.roles().append(x) for x in userIncludesOrganizationsAndRoles.roles()]
                    for dbOrg in dbOrganizations:
                        for org in userIncludesOrganizationsAndRoles.organizations():
                            if dbOrg.id == org.id():
                                newItem.organizations().append(self._organizationFromDbObject(dbOrg, usePrefix=False))
                    items.append(newItem)
        return items

    @debugLogger
    def _userFromDbObject(self, dbItemResult, usePrefix=True):
        if getattr(dbItemResult, f'user_id' if usePrefix else 'id', None) is not None:
            attributes = ['id', 'email', 'firstName', 'lastName', 'addressOne', 'addressTwo', 'postalCode',
                          'phoneNumber', 'avatarImage', 'countryId', 'cityId', 'countryStateName', 'countryStateIsoCode',
                          ]
            mapping = {"countryStateName": "subdivision_1_name", "countryStateIsoCode": "subdivision_1_iso_code"}
            kwargs = {x: getattr(dbItemResult, f'user_{Util.camelCaseToLowerSnakeCase(mapping[x] if x in mapping else x)}' if usePrefix else x, None) for x in attributes}
            kwargs['startDate'] = DateTimeHelper.datetimeToInt(getattr(dbItemResult, f'user_startDate', None))
            return User(**kwargs)
        return None

    @debugLogger
    def _organizationFromDbObject(self, dbItemResult, usePrefix=True):
        if getattr(dbItemResult, f'organization_id' if usePrefix else 'id', None) is not None:
            attributes = ['id', 'name', 'websiteUrl', 'organizationType', 'addressOne', 'addressTwo', 'postalCode',
                          'countryId', 'cityId', 'countryStateName', 'countryStateIsoCode', 'managerFirstName',
                          'managerLastName', 'managerEmail', 'managerPhoneNumber', 'managerAvatar',
                          ]
            kwargs = {x: getattr(dbItemResult, f'organization_{Util.camelCaseToLowerSnakeCase(x)}' if usePrefix else x, None) for x in attributes}
            return Organization(**kwargs)
        return None

    @debugLogger
    def _projectFromDbObject(self, dbItemResult, usePrefix=True):
        if getattr(dbItemResult, f'project_id' if usePrefix else 'id', None) is not None:
            attributes = ['id', 'name', 'cityId', 'countryId', 'addressLine', 'addressLineTwo',
                          'beneficiaryId', 'postalCode', 'countryStateName', 'countryStateIsoCode', 'developerName',
                          'developerCityId', 'developerCountryId', 'developerAddressLineOne', 'developerAddressLineTwo',
                          'developerContact', 'developerEmail', 'developerPhoneNumber', 'developerWarranty',
                          'developerPostalCode', 'developerCountryStateName', 'developerCountryStateIsoCode',
                          ]
            mapping = {"countryStateName": "subdivision_1_name", "countryStateIsoCode": "subdivision_1_iso_code",
                       "developerCountryStateName": "developer_subdivision_1_name", "developerCountryStateIsoCode": "developer_subdivision_1_iso_code",
                       "developerContact": "developer_contact_person", "developerPhoneNumber": "developer_phone"}
            kwargs = {x: getattr(dbItemResult, f'project_{Util.camelCaseToLowerSnakeCase(mapping[x] if x in mapping else x)}' if usePrefix else x, None) for x in attributes}
            kwargs['startDate'] = DateTimeHelper.datetimeToInt(getattr(dbItemResult, f'project_startDate', None))
            return Project(**kwargs)
        return None

    @debugLogger
    def _roleFromDbObject(self, dbItemResult, usePrefix=True):
        if getattr(dbItemResult, f'role_id' if usePrefix else 'id', None) is not None:
            attributes = ['id', 'name', 'title']
            kwargs = {x: getattr(dbItemResult, f'role_{Util.camelCaseToLowerSnakeCase(x)}' if usePrefix else x, None) for x in attributes}
            return Role(**kwargs)
        return None