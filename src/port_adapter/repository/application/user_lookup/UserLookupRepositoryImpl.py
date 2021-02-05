"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.inspection import inspect
from sqlalchemy.sql.expression import text

from src.application.user_lookup.UserLookup import UserLookup
from src.application.user_lookup.UserLookupRepository import UserLookupRepository
from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.resource.exception.UserDoesNotExistException import UserDoesNotExistException
from src.domain_model.role.Role import Role
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.token.TokenData import TokenData
from src.domain_model.user.User import User
from src.domain_model.user.UserRepository import UserRepository
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.Organization import Organization as DbOrganization
from src.port_adapter.repository.db_model.Role import Role as DbRole
from src.port_adapter.repository.db_model.User import User as DbUser
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class UserLookupRepositoryImpl(UserLookupRepository):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi
        self._roleRepo: RoleRepository = AppDi.instance.get(RoleRepository)
        self._userRepo: UserRepository = AppDi.instance.get(UserRepository)
        self._organizationRepo: OrganizationRepository = AppDi.instance.get(OrganizationRepository)

        self._dbUserColumnsMapping = inspect(DbUser).c
        self._dbRoleColumnsMapping = inspect(DbRole).c
        self._dbOrganizationColumnsMapping = inspect(DbOrganization).c
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}")
        except Exception as e:
            logger.warn(f'[{UserLookupRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def userLookupByUserId(self, id: str) -> UserLookup:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            userLookup = UserLookup()

            dbObject = dbSession.query(DbUser).filter_by(id=id).first()
            if dbObject is None:
                raise UserDoesNotExistException(f'id = {id}')
            user = self._userFromDbItemResult(dbItemResult=dbObject)
            userLookup.addUser(user)

            for org in dbObject.organizations:
                userLookup.addOrganization(self._organizationFromDbObject(org))

            for role in dbObject.roles:
                userLookup.addRole(self._roleFromDbObject(role))

            return userLookup
        finally:
            dbSession.close()

    @debugLogger
    def userLookupByUserEmail(self, email: str) -> UserLookup:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            userLookup = UserLookup()

            dbObject = dbSession.query(DbUser).filter_by(email=email).first()
            if dbObject is None:
                raise UserDoesNotExistException(f'id = {email}')
            user = self._userFromDbItemResult(dbItemResult=dbObject)
            userLookup.addUser(user)

            for org in dbObject.organizations:
                userLookup.addOrganization(self._organizationFromDbObject(org))

            for role in dbObject.roles:
                userLookup.addRole(self._roleFromDbObject(role))

            return userLookup
        finally:
            dbSession.close()

    @debugLogger
    def userLookups(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100, token: str = '',
                    order: List[dict] = None) -> dict:
        # logger.debug(dbSession.query(DbUser)\
        #     .options(joinedload(DbUser.organizations), joinedload(DbUser.roles))\
        #     .order_by(text('user.email'))\
        #     .limit(resultSize).offset(resultFrom).statement)

        sortData = ''
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]

        sortData = sortData.replace('user.', 'user_')
        sortData = sortData.replace('role.', 'role_')
        sortData = sortData.replace('organization.', 'organization_')
        if sortData != '':
            sortData = f'ORDER BY {sortData}'

        userCols = ','.join([f'user.{x.name} AS user_{x.name}' for x in self._dbUserColumnsMapping])
        roleCols = ','.join([f'role.{x.name} AS role_{x.name}' for x in self._dbRoleColumnsMapping])
        orgCols = ','.join(
            [f'organization.{x.name} AS organization_{x.name}' for x in self._dbOrganizationColumnsMapping])
        selectCols = f'{userCols},{roleCols},{orgCols}'
        dbItemsResult = self._db.execute(text(
            f'''SELECT {selectCols} FROM user
                    LEFT OUTER JOIN
                        user_role_junction user_role_junc ON user.id = user_role_junc.user_id
                    LEFT OUTER JOIN
                        role ON user_role_junc.role_id = role.id
                    LEFT OUTER JOIN
                        user_organization_junction user_org_junc ON user.id = user_org_junc.user_id
                    LEFT OUTER JOIN
                        organization ON user_org_junc.organization_id = organization.id
                    
                    {sortData}       
                    LIMIT {resultSize} OFFSET {resultFrom}                            
        '''))

        dbObjectsCount = self._db.execute(text(
            f'''SELECT count(1) FROM user
                    LEFT OUTER JOIN
                        user_role_junction user_role_junc ON user.id = user_role_junc.user_id
                    LEFT OUTER JOIN
                        role ON user_role_junc.role_id = role.id
                    LEFT OUTER JOIN
                        user_organization_junction user_org_junc ON user.id = user_org_junc.user_id
                    LEFT OUTER JOIN
                        organization ON user_org_junc.organization_id = organization.id                                   
        ''')).scalar()

        result = {"items": [], "itemCount": dbObjectsCount}

        userLookupsDict = {}
        for dbItemResult in dbItemsResult:
            user = self._userFromDbItemResult(dbItemResult=dbItemResult)
            if user.id() not in userLookupsDict:
                userLookup = UserLookup()
                userLookup.addUser(user)
                userLookupsDict[user.id()] = userLookup

                org: Organization = self._organizationFromDbObject(dbItemResult=dbItemResult)
                role: Role = self._roleFromDbObject(dbItemResult=dbItemResult)
                if org is not None:
                    userLookup.addOrganization(self._organizationFromDbObject(dbItemResult=dbItemResult))
                if role is not None:
                    userLookup.addRole(self._roleFromDbObject(dbItemResult=dbItemResult))
                result['items'].append(userLookup)
            else:
                userLookup = userLookupsDict[user.id()]
                org: Organization = self._organizationFromDbObject(dbItemResult=dbItemResult)
                role: Role = self._roleFromDbObject(dbItemResult=dbItemResult)
                if org is not None:
                    userLookup.addOrganization(self._organizationFromDbObject(dbItemResult=dbItemResult))
                if role is not None:
                    userLookup.addRole(self._roleFromDbObject(dbItemResult=dbItemResult))

        return result

    @debugLogger
    def _userFromDbItemResult(self, dbItemResult):
        prefix = 'user_'
        return User(id=dbItemResult[f'{prefix}{self._dbUserColumnsMapping.id.name}'],
                    email=dbItemResult[f'{prefix}{self._dbUserColumnsMapping.email.name}'],
                    firstName=dbItemResult[f'{prefix}{self._dbUserColumnsMapping.firstName.name}'],
                    lastName=dbItemResult[f'{prefix}{self._dbUserColumnsMapping.lastName.name}'],
                    addressOne=dbItemResult[f'{prefix}{self._dbUserColumnsMapping.addressOne.name}'],
                    addressTwo=dbItemResult[f'{prefix}{self._dbUserColumnsMapping.addressTwo.name}'],
                    postalCode=dbItemResult[f'{prefix}{self._dbUserColumnsMapping.postalCode.name}'],
                    phoneNumber=dbItemResult[f'{prefix}{self._dbUserColumnsMapping.phoneNumber.name}'],
                    avatarImage=dbItemResult[f'{prefix}{self._dbUserColumnsMapping.avatarImage.name}'],
                    countryId=dbItemResult[f'{prefix}{self._dbUserColumnsMapping.countryId.name}'],
                    cityId=dbItemResult[f'{prefix}{self._dbUserColumnsMapping.cityId.name}'],
                    countryStateName=dbItemResult[f'{prefix}{self._dbUserColumnsMapping.countryStateName.name}'],
                    startDate=dbItemResult[f'{prefix}{self._dbUserColumnsMapping.startDate.name}']
                    if dbItemResult[f'{prefix}{self._dbUserColumnsMapping.startDate.name}'] != None else None)

    @debugLogger
    def _organizationFromDbObject(self, dbItemResult):
        prefix = 'organization_'
        if dbItemResult[f'{prefix}{self._dbOrganizationColumnsMapping.id.name}'] is None:
            return None
        return Organization(id=dbItemResult[f'{prefix}{self._dbOrganizationColumnsMapping.id.name}'],
                            name=dbItemResult[f'{prefix}{self._dbOrganizationColumnsMapping.name.name}'],
                            websiteUrl=dbItemResult[f'{prefix}{self._dbOrganizationColumnsMapping.websiteUrl.name}'],
                            organizationType=dbItemResult[
                                f'{prefix}{self._dbOrganizationColumnsMapping.organizationType.name}'],
                            addressOne=dbItemResult[f'{prefix}{self._dbOrganizationColumnsMapping.addressOne.name}'],
                            addressTwo=dbItemResult[f'{prefix}{self._dbOrganizationColumnsMapping.addressTwo.name}'],
                            postalCode=dbItemResult[f'{prefix}{self._dbOrganizationColumnsMapping.postalCode.name}'],
                            countryId=dbItemResult[f'{prefix}{self._dbOrganizationColumnsMapping.countryId.name}'],
                            cityId=dbItemResult[f'{prefix}{self._dbOrganizationColumnsMapping.cityId.name}'],
                            countryStateName=dbItemResult[
                                f'{prefix}{self._dbOrganizationColumnsMapping.countryStateName.name}'],
                            managerFirstName=dbItemResult[
                                f'{prefix}{self._dbOrganizationColumnsMapping.managerFirstName.name}'],
                            managerLastName=dbItemResult[
                                f'{prefix}{self._dbOrganizationColumnsMapping.managerLastName.name}'],
                            managerEmail=dbItemResult[
                                f'{prefix}{self._dbOrganizationColumnsMapping.managerEmail.name}'],
                            managerPhoneNumber=dbItemResult[
                                f'{prefix}{self._dbOrganizationColumnsMapping.managerPhoneNumber.name}'],
                            managerAvatar=dbItemResult[
                                f'{prefix}{self._dbOrganizationColumnsMapping.managerAvatar.name}'])

    @debugLogger
    def _roleFromDbObject(self, dbItemResult):
        prefix = 'role_'
        if dbItemResult[f'{prefix}{self._dbRoleColumnsMapping.id.name}'] is None:
            return None
        return Role(id=dbItemResult[f'{prefix}{self._dbRoleColumnsMapping.id.name}'],
                    name=dbItemResult[f'{prefix}{self._dbRoleColumnsMapping.name.name}'])
