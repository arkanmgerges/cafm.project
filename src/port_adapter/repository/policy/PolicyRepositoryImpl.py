"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.application.lifecycle.ApplicationServiceLifeCycle import (
    ApplicationServiceLifeCycle,
)
from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.policy.PolicyRepository import PolicyRepository
from src.domain_model.project.Project import Project
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.role.Role import Role
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.token.TokenData import TokenData
from src.domain_model.user.User import User
from src.domain_model.user.UserRepository import UserRepository
from src.port_adapter.repository.db_model.Organization import (
    Organization as DbOrganization,
)
from src.port_adapter.repository.db_model.Project import Project as DbProject
from src.port_adapter.repository.db_model.Role import Role as DbRole
from src.port_adapter.repository.db_model.User import User as DbUser
from src.resource.logging.decorator import debugLogger


class PolicyRepositoryImpl(PolicyRepository):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi

        self._roleRepo: RoleRepository = AppDi.instance.get(RoleRepository)
        self._userRepo: UserRepository = AppDi.instance.get(UserRepository)
        self._organizationRepo: OrganizationRepository = AppDi.instance.get(
            OrganizationRepository
        )
        self._projectRepo: ProjectRepository = AppDi.instance.get(ProjectRepository)

    @debugLogger
    def assignRoleToUser(self, role: Role, user: User, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbUserObject = dbSession.query(DbUser).filter_by(id=user.id()).first()
        if dbUserObject is not None:
            dbRoleObject = dbSession.query(DbRole).filter_by(id=role.id()).first()
            if dbRoleObject is not None:
                dbUserObject.roles.append(dbRoleObject)

    @debugLogger
    def revokeRoleToUserAssignment(
        self, role: Role, user: User, tokenData: TokenData = None
    ):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbUserObject = dbSession.query(DbUser).filter_by(id=user.id()).first()
        if dbUserObject is not None:
            dbRoleObject = dbSession.query(DbRole).filter_by(id=role.id()).first()
            if dbRoleObject is not None:
                for obj in dbUserObject.roles:
                    if obj.id == role.id():
                        dbUserObject.roles.remove(obj)

    @debugLogger
    def assignUserToOrganization(
        self, organization: Organization, user: User, tokenData: TokenData = None
    ):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbUserObject = dbSession.query(DbUser).filter_by(id=user.id()).first()
        if dbUserObject is not None:
            dbOrganizationObject = (
                dbSession.query(DbOrganization).filter_by(id=organization.id()).first()
            )
            if dbOrganizationObject is not None:
                dbUserObject.organizations.append(dbOrganizationObject)

    @debugLogger
    def revokeUserToOrganizationAssignment(
        self, organization: Organization, user: User, tokenData: TokenData = None
    ):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbUserObject = dbSession.query(DbUser).filter_by(id=user.id()).first()
        if dbUserObject is not None:
            dbOrganizationObject = (
                dbSession.query(DbOrganization).filter_by(id=organization.id()).first()
            )
            if dbOrganizationObject is not None:
                for obj in dbUserObject.organizations:
                    if obj.id == organization.id():
                        dbUserObject.organizations.remove(obj)

    def assignRoleToOrganization(
        self, role: Role, organization: Organization, tokenData: TokenData
    ):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbRoleObject = dbSession.query(DbRole).filter_by(id=role.id()).first()
        if dbRoleObject is not None:
            dbOrganizationObject = (
                dbSession.query(DbOrganization).filter_by(id=organization.id()).first()
            )
            if dbOrganizationObject is not None:
                dbRoleObject.organizations.append(dbOrganizationObject)

    def revokeRoleToOrganizationAssignment(
        self, role: Role, organization: Organization, tokenData: TokenData
    ):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbRoleObject = dbSession.query(DbRole).filter_by(id=role.id()).first()
        if dbRoleObject is not None:
            dbOrganizationObject = (
                dbSession.query(DbOrganization).filter_by(id=organization.id()).first()
            )
            if dbOrganizationObject is not None:
                for obj in dbRoleObject.organizations:
                    if obj.id == organization.id():
                        dbRoleObject.organizations.remove(obj)

    def assignRoleToProject(self, role: Role, project: Project, tokenData: TokenData):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbRoleObject = dbSession.query(DbRole).filter_by(id=role.id()).first()
        if dbRoleObject is not None:
            dbProjectObject = (
                dbSession.query(DbProject).filter_by(id=project.id()).first()
            )
            if dbProjectObject is not None:
                dbRoleObject.projects.append(dbProjectObject)

    def revokeRoleToProjectAssignment(
        self, role: Role, project: Project, tokenData: TokenData
    ):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbRoleObject = dbSession.query(DbRole).filter_by(id=role.id()).first()
        if dbRoleObject is not None:
            dbProjectObject = (
                dbSession.query(DbProject).filter_by(id=project.id()).first()
            )
            if dbProjectObject is not None:
                for obj in dbRoleObject.projects:
                    if obj.id == project.id():
                        dbRoleObject.projects.remove(obj)

    @debugLogger
    def assignProjectToOrganization(
        self, organization: Organization, project: Project, tokenData: TokenData = None
    ):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        try:
            dbProjectObject = (
                dbSession.query(DbProject).filter_by(id=project.id()).first()
            )
            if dbProjectObject is not None:
                dbOrganizationObject = (
                    dbSession.query(DbOrganization)
                    .filter_by(id=organization.id())
                    .first()
                )
                if dbOrganizationObject is not None:
                    dbProjectObject.organizations.append(dbOrganizationObject)
                    dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def revokeProjectToOrganizationAssignment(
        self, organization: Organization, project: Project, tokenData: TokenData = None
    ):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        try:
            dbProjectObject = (
                dbSession.query(DbProject).filter_by(id=project.id()).first()
            )
            if dbProjectObject is not None:
                dbOrganizationObject = (
                    dbSession.query(DbOrganization)
                    .filter_by(id=organization.id())
                    .first()
                )
                if dbOrganizationObject is not None:
                    for obj in dbProjectObject.organizations:
                        if obj.id == organization.id():
                            dbProjectObject.organizations.remove(obj)
                    dbSession.commit()
        finally:
            dbSession.close()
