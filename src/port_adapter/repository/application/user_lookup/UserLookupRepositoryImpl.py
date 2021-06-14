"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from sqlalchemy.inspection import inspect
from sqlalchemy.sql.expression import text

from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from src.application.user_lookup.UserLookup import UserLookup
from src.application.user_lookup.UserLookupRepository import UserLookupRepository
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
from src.port_adapter.repository.db_model.User import User as DbUser
from src.port_adapter.repository.db_model.role__organization__junction import (
    ROLE__ORGANIZATION__JUNCTION,
)
from src.port_adapter.repository.db_model.user__role__junction import (
    USER__ROLE__JUNCTION,
)
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger


class UserLookupRepositoryImpl(UserLookupRepository):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi

        self._roleRepo: RoleRepository = AppDi.instance.get(RoleRepository)
        self._userRepo: UserRepository = AppDi.instance.get(UserRepository)
        self._organizationRepo: OrganizationRepository = AppDi.instance.get(
            OrganizationRepository
        )

        self._dbUserColumnsMapping = inspect(DbUser).c
        self._dbRoleColumnsMapping = inspect(DbRole).c
        self._dbOrganizationColumnsMapping = inspect(DbOrganization).c

    @debugLogger
    def userLookupByUserId(self, id: str) -> UserLookup:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        userLookup = UserLookup()

        dbObject = dbSession.query(DbUser).filter_by(id=id).first()
        if dbObject is None:
            raise UserDoesNotExistException(f"id = {id}")
        user = self._userFromDbItemResult(dbItemResult=dbObject, usePrefix=False)
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
        user = self._userFromDbItemResult(dbItemResult=dbObject, usePrefix=False)

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
    def userLookups(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
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

        userCols = ",".join(
            [f"user.{x.name} AS user_{x.name}" for x in self._dbUserColumnsMapping]
        )
        roleCols = ",".join(
            [f"role.{x.name} AS role_{x.name}" for x in self._dbRoleColumnsMapping]
        )
        orgCols = ",".join(
            [
                f"organization.{x.name} AS organization_{x.name}"
                for x in self._dbOrganizationColumnsMapping
            ]
        )
        selectCols = f"{userCols},{roleCols},{orgCols}"

        dbItemsResult = dbSession.execute(
            text(
                f"""SELECT {selectCols} FROM user
                    LEFT OUTER JOIN
                        {USER__ROLE__JUNCTION} user__role__junc ON user.id = user__role__junc.user_id
                    LEFT OUTER JOIN
                        role ON role.id = user__role__junc.role_id
                    LEFT OUTER JOIN
                        {ROLE__ORGANIZATION__JUNCTION} role__org__junc ON role.id = role__org__junc.role_id
                    LEFT OUTER JOIN
                        organization ON organization.id = role__org__junc.organization_id
                    
                    {sortData}       
                    LIMIT {resultSize} OFFSET {resultFrom}                            
        """
            )
        )
        dbObjectsCount = dbSession.execute(
            text(
                f"""SELECT count(1) FROM user
                    LEFT OUTER JOIN
                        {USER__ROLE__JUNCTION} user__role__junc ON user.id = user__role__junc.user_id
                    LEFT OUTER JOIN
                        role ON user__role__junc.role_id = role.id
                    LEFT OUTER JOIN
                        {ROLE__ORGANIZATION__JUNCTION} role__org__junc ON role.id = role__org__junc.role_id
                    LEFT OUTER JOIN
                        organization ON role__org__junc.organization_id = organization.id                                   
        """
            )
        ).scalar()

        result = {"items": [], "totalItemCount": dbObjectsCount}

        userLookupsDict = {}

        for dbItemResult in dbItemsResult:
            user = self._userFromDbItemResult(dbItemResult=dbItemResult)
            if user.id() not in userLookupsDict:
                userLookup = UserLookup()
                userLookup.addUser(user)
                userLookupsDict[user.id()] = userLookup

                org: Organization = self._organizationFromDbObject(
                    dbItemResult=dbItemResult
                )
                role: Role = self._roleFromDbObject(dbItemResult=dbItemResult)
                if org is not None:
                    userLookup.addOrganization(
                        self._organizationFromDbObject(dbItemResult=dbItemResult)
                    )
                if role is not None:
                    userLookup.addRole(
                        self._roleFromDbObject(dbItemResult=dbItemResult)
                    )
                result["items"].append(userLookup)
            else:
                userLookup = userLookupsDict[user.id()]
                org: Organization = self._organizationFromDbObject(
                    dbItemResult=dbItemResult
                )
                role: Role = self._roleFromDbObject(dbItemResult=dbItemResult)
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
    def _userFromDbItemResult(self, dbItemResult, usePrefix=True):
        if getattr(dbItemResult, f'user_id' if usePrefix else 'id', None) is not None:
            attributes = ['id', 'email', 'firstName', 'lastName', 'addressOne', 'addressTwo', 'postalCode',
                          'phoneNumber', 'avatarImage', 'countryId', 'cityId', 'countryStateName', 'countryStateIsoCode',
                          ]
            kwargs = {x: getattr(dbItemResult, f'user_{Util.camelCaseToLowerSnakeCase(x)}' if usePrefix else x, None) for x in attributes}
            from src.resource.common.DateTimeHelper import DateTimeHelper
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
    def _roleFromDbObject(self, dbItemResult, usePrefix=True):
        if getattr(dbItemResult, f'role_id' if usePrefix else 'id', None) is not None:
            attributes = ['id', 'name', 'title']
            kwargs = {x: getattr(dbItemResult, f'role_{Util.camelCaseToLowerSnakeCase(x)}' if usePrefix else x, None) for x in attributes}
            return Role(**kwargs)
        return None