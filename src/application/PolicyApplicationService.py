"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.application.lifecycle.decorator.transactional import transactional
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.policy.PolicyRepository import PolicyRepository
from src.domain_model.policy.PolicyService import PolicyService
from src.domain_model.project.ProjectRepository import ProjectRepository
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.token.TokenService import TokenService
from src.domain_model.user.UserRepository import UserRepository
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class PolicyApplicationService:
    def __init__(
        self,
        repo: PolicyRepository,
        policyService: PolicyService,
        userRepo: UserRepository,
        roleRepo: RoleRepository,
        organizationRepo: OrganizationRepository,
        projectRepo: ProjectRepository,
    ):
        self._repo = repo
        self._userRepo = userRepo
        self._roleRepo: RoleRepository = roleRepo
        self._organizationRepo: OrganizationRepository = organizationRepo
        self._projectRepo: ProjectRepository = projectRepo
        self._policyService: PolicyService = policyService

    @transactional
    @debugLogger
    def assignRoleToUser(self, userId: str, roleId: str, token: str = ""):
        from src.domain_model.role.Role import Role
        from src.domain_model.user.User import User

        role: Role = self._roleRepo.roleById(id=roleId)
        user: User = self._userRepo.userById(id=userId)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        self._policyService.assignRoleToUser(role=role, user=user)

    @transactional
    @debugLogger
    def revokeRoleToUserAssignment(self, userId: str, roleId: str, token: str = ""):
        from src.domain_model.user.User import User
        from src.domain_model.role.Role import Role

        role: Role = self._roleRepo.roleById(id=roleId)
        user: User = self._userRepo.userById(id=userId)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        self._policyService.revokeRoleToUserAssignment(role=role, user=user)

    @transactional
    @debugLogger
    def assignUserToOrganization(
        self, userId: str, organizationId: str, token: str = ""
    ):
        from src.domain_model.user.User import User
        from src.domain_model.organization.Organization import Organization

        organization: Organization = self._organizationRepo.organizationById(
            id=organizationId
        )
        user: User = self._userRepo.userById(id=userId)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        self._policyService.assignUserToOrganization(
            organization=organization, user=user
        )

    @transactional
    @debugLogger
    def revokeUserToOrganizationAssignment(
        self, userId: str, organizationId: str, token: str = ""
    ):
        from src.domain_model.user.User import User
        from src.domain_model.organization.Organization import Organization

        organization: Organization = self._organizationRepo.organizationById(
            id=organizationId
        )
        user: User = self._userRepo.userById(id=userId)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        self._policyService.revokeUserToOrganizationAssignment(
            organization=organization, user=user
        )

    @transactional
    @debugLogger
    def assignRoleToOrganization(
        self, roleId: str, organizationId: str, token: str = ""
    ):
        from src.domain_model.role.Role import Role
        from src.domain_model.organization.Organization import Organization

        role: Role = self._roleRepo.roleById(id=roleId)
        organization: Organization = self._organizationRepo.organizationById(
            id=organizationId
        )
        _tokenData = TokenService.tokenDataFromToken(token=token)
        self._policyService.assignRoleToOrganization(
            role=role, organization=organization
        )

    @transactional
    @debugLogger
    def revokeRoleToOrganizationAssignment(
        self, roleId: str, organizationId: str, token: str = ""
    ):
        from src.domain_model.role.Role import Role
        from src.domain_model.organization.Organization import Organization

        role: Role = self._roleRepo.roleById(id=roleId)
        organization: Organization = self._organizationRepo.organizationById(
            id=organizationId
        )
        _tokenData = TokenService.tokenDataFromToken(token=token)
        self._policyService.revokeRoleToOrganizationAssignment(
            organization=organization, role=role
        )

    @transactional
    @debugLogger
    def assignRoleToProject(self, roleId: str, projectId: str, token: str = ""):
        from src.domain_model.role.Role import Role
        from src.domain_model.project.Project import Project

        role: Role = self._roleRepo.roleById(id=roleId)
        project: Project = self._projectRepo.projectById(id=projectId)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        self._policyService.assignRoleToProject(role=role, project=project)

    @transactional
    @debugLogger
    def revokeRoleToProjectAssignment(
        self, roleId: str, projectId: str, token: str = ""
    ):
        from src.domain_model.role.Role import Role
        from src.domain_model.project.Project import Project

        role: Role = self._roleRepo.roleById(id=roleId)
        project: Project = self._projectRepo.projectById(id=projectId)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        self._policyService.revokeRoleToProjectAssignment(project=project, role=role)

    @transactional
    @debugLogger
    def assignProjectToOrganization(
        self, projectId: str, organizationId: str, token: str = ""
    ):
        from src.domain_model.project.Project import Project
        from src.domain_model.organization.Organization import Organization

        organization: Organization = self._organizationRepo.organizationById(
            id=organizationId
        )
        project: Project = self._projectRepo.projectById(id=projectId)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        self._policyService.assignProjectToOrganization(
            organization=organization, project=project
        )

    @transactional
    @debugLogger
    def revokeProjectToOrganizationAssignment(
        self, projectId: str, organizationId: str, token: str = ""
    ):
        from src.domain_model.project.Project import Project
        from src.domain_model.organization.Organization import Organization

        organization: Organization = self._organizationRepo.organizationById(
            id=organizationId
        )
        project: Project = self._projectRepo.projectById(id=projectId)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        self._policyService.revokeProjectToOrganizationAssignment(
            organization=organization, project=project
        )
