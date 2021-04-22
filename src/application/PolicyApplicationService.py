"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.policy.PolicyRepository import PolicyRepository
from src.domain_model.policy.PolicyService import PolicyService
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.token.TokenService import TokenService
from src.domain_model.user.UserRepository import UserRepository
from src.resource.logging.decorator import debugLogger


class PolicyApplicationService:
    def __init__(
        self,
        repo: PolicyRepository,
        policyService: PolicyService,
        userRepo: UserRepository,
        roleRepo: RoleRepository,
        organizationRepo: OrganizationRepository,
    ):
        self._repo = repo
        self._userRepo = userRepo
        self._roleRepo: RoleRepository = roleRepo
        self._organizationRepo: OrganizationRepository = organizationRepo
        self._policyService: PolicyService = policyService

    @debugLogger
    def assignRoleToUser(self, userId: str, roleId: str, token: str = ""):
        from src.domain_model.role.Role import Role
        from src.domain_model.user.User import User

        role: Role = self._roleRepo.roleById(id=roleId)
        user: User = self._userRepo.userById(id=userId)
        tokenData = TokenService.tokenDataFromToken(token=token)
        self._policyService.assignRoleToUser(role=role, user=user)

    @debugLogger
    def revokeRoleToUserAssignment(self, userId: str, roleId: str, token: str = ""):
        from src.domain_model.user.User import User
        from src.domain_model.role.Role import Role

        role: Role = self._roleRepo.roleById(id=roleId)
        user: User = self._userRepo.userById(id=userId)
        tokenData = TokenService.tokenDataFromToken(token=token)
        self._policyService.revokeRoleToUserAssignment(role=role, user=user)

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
        tokenData = TokenService.tokenDataFromToken(token=token)
        self._policyService.assignUserToOrganization(
            organization=organization, user=user
        )

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
        tokenData = TokenService.tokenDataFromToken(token=token)
        self._policyService.revokeUserToOrganizationAssignment(
            organization=organization, user=user
        )
