"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

from sqlalchemy import create_engine

from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.policy.PolicyRepository import PolicyRepository
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

class PolicyRepositoryImpl(PolicyRepository):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi
        self._roleRepo: RoleRepository = AppDi.instance.get(RoleRepository)
        self._userRepo: UserRepository = AppDi.instance.get(UserRepository)
        self._organizationRepo: OrganizationRepository = AppDi.instance.get(OrganizationRepository)
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}")
        except Exception as e:
            logger.warn(f'[{PolicyRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def assignRoleToUser(self, role: Role, user: User, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbUserObject = dbSession.query(DbUser).filter_by(id=user.id()).first()
            if dbUserObject is not None:
                dbRoleObject = dbSession.query(DbRole).filter_by(id=role.id()).first()
                if dbRoleObject is not None:
                    dbUserObject.roles.append(dbRoleObject)
                    dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def revokeRoleToUserAssignment(self, role: Role, user: User, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbUserObject = dbSession.query(DbUser).filter_by(id=user.id()).first()
            if dbUserObject is not None:
                dbRoleObject = dbSession.query(DbRole).filter_by(id=role.id()).first()
                if dbRoleObject is not None:
                    for obj in dbUserObject.roles:
                        if obj.id == role.id():
                            dbUserObject.roles.remove(obj)
                    dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def assignUserToOrganization(self, organization: Organization, user: User, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbUserObject = dbSession.query(DbUser).filter_by(id=user.id()).first()
            if dbUserObject is not None:
                dbOrganizationObject = dbSession.query(DbOrganization).filter_by(id=organization.id()).first()
                if dbOrganizationObject is not None:
                    dbUserObject.organizations.append(dbOrganizationObject)
                    dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def revokeUserToOrganizationAssignment(self, organization: Organization, user: User, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbUserObject = dbSession.query(DbUser).filter_by(id=user.id()).first()
            if dbUserObject is not None:
                dbOrganizationObject = dbSession.query(DbOrganization).filter_by(id=organization.id()).first()
                if dbOrganizationObject is not None:
                    for obj in dbUserObject.organizations:
                        if obj.id == organization.id():
                            dbUserObject.organizations.remove(obj)
                    dbSession.commit()
        finally:
            dbSession.close()
