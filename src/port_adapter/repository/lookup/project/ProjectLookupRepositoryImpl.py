"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.project.Project import Project
from src.port_adapter.repository.db_model.role__project__junction import ROLE__PROJECT__JUNCTION
from src.port_adapter.repository.lookup.common.sql.SqlLookupBaseRepository import SqlLookupBaseRepository
from typing import List

from sqlalchemy.inspection import inspect
from sqlalchemy.sql.expression import text

from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from src.application.lookup.project.ProjectLookup import ProjectLookup
from src.application.lookup.project.ProjectLookupRepository import ProjectLookupRepository
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


class ProjectLookupRepositoryImpl(SqlLookupBaseRepository, ProjectLookupRepository):
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

        sql = f"""FROM project
                    LEFT OUTER JOIN
                        {ROLE__PROJECT__JUNCTION} role__project__junc ON project.id = role__project__junc.project_id 
                    LEFT OUTER JOIN
                        role ON role.id = role__project__junc.role_id
                    LEFT OUTER JOIN
                        {USER__ROLE__JUNCTION} user__role__junc ON role.id = user__role__junc.role_id
                    LEFT OUTER JOIN
                        user ON user.id = user__role__junc.user_id
                    LEFT OUTER JOIN
                        {ROLE__ORGANIZATION__JUNCTION} role__org__junc ON role.id = role__org__junc.role_id
                    LEFT OUTER JOIN
                        organization ON organization.id = role__org__junc.organization_id
                    

                """

        dbItemsResult = dbSession.execute(
            text(f"SELECT {selectCols} {sql}\n{filterData}\n{sortData}\nLIMIT {resultSize} OFFSET {resultFrom}")
        )

        dbObjectsCount = dbSession.execute(
            text(f"SELECT count(1) FROM (SELECT count(1) {sql}\n{filterData} GROUP BY project.id) t")
        ).scalar()
        result = {"items": [], "totalItemCount": dbObjectsCount}

        baseLookupDict = {}

        for dbItemResult in dbItemsResult:
            project = self._projectFromDbObject(dbItemResult=dbItemResult)
            if project.id() not in baseLookupDict:
                projectLookup = ProjectLookup()
                projectLookup.addProject(project)
                baseLookupDict[project.id()] = projectLookup

                org: Organization = self._organizationFromDbObject(
                    dbItemResult=dbItemResult
                )
                role: Role = self._roleFromDbObject(dbItemResult=dbItemResult)
                user: User = self._userFromDbObject(dbItemResult=dbItemResult)
                if org is not None:
                    projectLookup.addOrganization(
                        self._organizationFromDbObject(dbItemResult=dbItemResult)
                    )
                if role is not None:
                    projectLookup.addRole(
                        self._roleFromDbObject(dbItemResult=dbItemResult)
                    )
                if user is not None:
                    projectLookup.addUser(
                        self._userFromDbObject(dbItemResult=dbItemResult)
                    )
                result["items"].append(projectLookup)
            else:
                projectLookup = baseLookupDict[project.id()]
                org: Organization = self._organizationFromDbObject(
                    dbItemResult=dbItemResult
                )
                role: Role = self._roleFromDbObject(dbItemResult=dbItemResult)
                user: User = self._userFromDbObject(dbItemResult=dbItemResult)
                if user is not None:
                    projectLookup.addUser(
                        self._userFromDbObject(dbItemResult=dbItemResult)
                    )
                if org is not None:
                    projectLookup.addOrganization(
                        self._organizationFromDbObject(dbItemResult=dbItemResult)
                    )
                if role is not None:
                    projectLookup.addRole(
                        self._roleFromDbObject(dbItemResult=dbItemResult)
                    )
        return result

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