"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from src.application.user_lookup.UserLookup import UserLookup
from src.application.user_lookup.UserLookupRepository import UserLookupRepository
from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.resource.exception.UserDoesNotExistException import UserDoesNotExistException
from src.domain_model.role.Role import Role
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.user.User import User
from src.domain_model.user.UserRepository import UserRepository
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.port_adapter.repository.db_model.User import User as DbUser
from src.port_adapter.repository.db_model.Role import Role as DbRole
from src.port_adapter.repository.db_model.Organization import Organization as DbOrganization


class UserLookupRepositoryImpl(UserLookupRepository):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi
        self._roleRepo: RoleRepository = AppDi.instance.get(RoleRepository)
        self._userRepo: UserRepository = AppDi.instance.get(UserRepository)
        self._organizationRepo: OrganizationRepository = AppDi.instance.get(OrganizationRepository)
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}")
            SessionFactory = sessionmaker(bind=self._db)
            self._dbSession: Session = SessionFactory()
        except Exception as e:
            logger.warn(f'[{UserLookupRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def userLookupByUserId(self, id: str) -> UserLookup:
        userLookup = UserLookup()

        dbObject = self._dbSession.query(DbUser).filter_by(id=id).first()
        if dbObject is None:
            raise UserDoesNotExistException(f'id = {id}')
        user = self._userFromDbObject(dbObject=dbObject)
        userLookup.addUser(user)

        for org in dbObject.organizations:
            userLookup.addOrganization(self._organizationFromDbObject(org))

        for role in dbObject.roles:
            userLookup.addRole(self._roleFromDbObject(role))

        return userLookup

    @debugLogger
    def _userFromDbObject(self, dbObject):
        return User(id=dbObject.id,
                    email=dbObject.email,
                    firstName=dbObject.firstName,
                    lastName=dbObject.lastName,
                    addressOne=dbObject.addressOne,
                    addressTwo=dbObject.addressTwo,
                    postalCode=dbObject.postalCode,
                    phoneNumber=dbObject.phoneNumber,
                    avatarImage=dbObject.avatarImage,
                    countryId=dbObject.countryId,
                    cityId=dbObject.cityId,
                    countryStateName=dbObject.countryStateName,
                    startDate=dbObject.startDate.timestamp() if dbObject.startDate != None else None)

    @debugLogger
    def _organizationFromDbObject(self, dbObject: DbOrganization):
        return Organization(id=dbObject.id,
                            name=dbObject.name,
                            websiteUrl=dbObject.websiteUrl,
                            organizationType=dbObject.organizationType,
                            addressOne=dbObject.addressOne,
                            addressTwo=dbObject.addressTwo,
                            postalCode=dbObject.postalCode,
                            countryId=dbObject.countryId,
                            cityId=dbObject.cityId,
                            countryStateName=dbObject.countryStateName,
                            managerFirstName=dbObject.managerFirstName,
                            managerLastName=dbObject.managerLastName,
                            managerEmail=dbObject.managerEmail,
                            managerPhoneNumber=dbObject.managerPhoneNumber,
                            managerAvatar=dbObject.managerAvatar)

    @debugLogger
    def _roleFromDbObject(self, dbObject: DbRole):
        return Role(id=dbObject.id, name=dbObject.name)