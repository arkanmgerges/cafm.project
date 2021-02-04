"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.organization.Organization import Organization
from src.domain_model.policy.PolicyRepository import PolicyRepository
from src.domain_model.role.Role import Role
from src.domain_model.token.TokenData import TokenData
from src.domain_model.user.User import User
from src.resource.logging.decorator import debugLogger


class PolicyService:
    def __init__(self, policyRepo: PolicyRepository):
        self._repo: PolicyRepository = policyRepo

    @debugLogger
    def assignRoleToUser(self, role: Role, user: User, tokenData: TokenData = None):
        from src.domain_model.policy.RoleToUserAssigned import \
            RoleToUserAssigned
        DomainPublishedEvents.addEventForPublishing(RoleToUserAssigned(role=role, user=user))

    @debugLogger
    def revokeRoleToUserAssignment(self, role: Role, user: User, tokenData: TokenData = None):
        from src.domain_model.policy.RoleToUserAssignmentRevoked import \
            RoleToUserAssignmentRevoked
        DomainPublishedEvents.addEventForPublishing(RoleToUserAssignmentRevoked(role=role, user=user))

    @debugLogger
    def assignUserToOrganization(self, organization: Organization, user: User, tokenData: TokenData = None):
        from src.domain_model.policy.UserToOrganizationAssigned import UserToOrganizationAssigned
        DomainPublishedEvents.addEventForPublishing(UserToOrganizationAssigned(organization=organization, user=user))

    @debugLogger
    def revokeUserToOrganizationAssignment(self, organization: Organization, user: User, tokenData: TokenData = None):
        from src.domain_model.policy.UserToOrganizationAssignmentRevoked import UserToOrganizationAssignmentRevoked
        DomainPublishedEvents.addEventForPublishing(
            UserToOrganizationAssignmentRevoked(organization=organization, user=user))
