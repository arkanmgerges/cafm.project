"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.tag.Tag import Tag
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.organization.Organization import Organization
from src.domain_model.policy.PolicyRepository import PolicyRepository
from src.domain_model.project.Project import Project
from src.domain_model.role.Role import Role
from src.domain_model.token.TokenData import TokenData
from src.domain_model.user.User import User
from src.resource.logging.decorator import debugLogger


class PolicyService:
    def __init__(self, policyRepo: PolicyRepository):
        self._repo: PolicyRepository = policyRepo

    @debugLogger
    def assignRoleToUser(self, role: Role, user: User, tokenData: TokenData = None):
        from src.domain_model.policy.RoleToUserAssigned import RoleToUserAssigned

        DomainPublishedEvents.addEventForPublishing(
            RoleToUserAssigned(role=role, user=user)
        )
        self._repo.assignRoleToUser(role=role, user=user)

    @debugLogger
    def revokeRoleToUserAssignment(
        self, role: Role, user: User, tokenData: TokenData = None
    ):
        from src.domain_model.policy.RoleToUserAssignmentRevoked import (
            RoleToUserAssignmentRevoked,
        )

        DomainPublishedEvents.addEventForPublishing(
            RoleToUserAssignmentRevoked(role=role, user=user)
        )
        self._repo.revokeRoleToUserAssignment(role=role, user=user)

    @debugLogger
    def assignUserToOrganization(
        self, organization: Organization, user: User, tokenData: TokenData = None
    ):
        from src.domain_model.policy.UserToOrganizationAssigned import (
            UserToOrganizationAssigned,
        )

        DomainPublishedEvents.addEventForPublishing(
            UserToOrganizationAssigned(organization=organization, user=user)
        )
        self._repo.assignUserToOrganization(organization=organization, user=user)

    @debugLogger
    def revokeUserToOrganizationAssignment(
        self, organization: Organization, user: User, tokenData: TokenData = None
    ):
        from src.domain_model.policy.UserToOrganizationAssignmentRevoked import (
            UserToOrganizationAssignmentRevoked,
        )

        DomainPublishedEvents.addEventForPublishing(
            UserToOrganizationAssignmentRevoked(organization=organization, user=user)
        )
        self._repo.revokeUserToOrganizationAssignment(
            organization=organization, user=user
        )

    @debugLogger
    def assignRoleToOrganization(
        self, role: Role, organization: Organization, tokenData: TokenData = None
    ):
        self._repo.assignRoleToOrganization(
            organization=organization, role=role, tokenData=tokenData
        )

    @debugLogger
    def revokeRoleToOrganizationAssignment(
        self, role: Role, organization: Organization, tokenData: TokenData = None
    ):
        self._repo.revokeRoleToOrganizationAssignment(
            organization=organization, role=role, tokenData=tokenData
        )

    @debugLogger
    def assignRoleToProject(
        self, role: Role, project: Project, tokenData: TokenData = None
    ):
        self._repo.assignRoleToProject(project=project, role=role, tokenData=tokenData)

    @debugLogger
    def assignTagToRole(
        self, role: Role, tag: Tag, tokenData: TokenData = None
    ):
        self._repo.assignTagToRole(tag=tag, role=role, tokenData=tokenData)

    @debugLogger
    def revokeRoleToProjectAssignment(
        self, role: Role, project: Project, tokenData: TokenData = None
    ):
        self._repo.revokeRoleToProjectAssignment(
            project=project, role=role, tokenData=tokenData
        )

    @debugLogger
    def assignProjectToOrganization(
        self, organization: Organization, project: Project, tokenData: TokenData = None
    ):
        from src.domain_model.policy.ProjectToOrganizationAssigned import (
            ProjectToOrganizationAssigned,
        )

        DomainPublishedEvents.addEventForPublishing(
            ProjectToOrganizationAssigned(organization=organization, project=project)
        )
        self._repo.assignProjectToOrganization(
            organization=organization, project=project
        )

    @debugLogger
    def revokeProjectToOrganizationAssignment(
        self, organization: Organization, project: Project, tokenData: TokenData = None
    ):
        from src.domain_model.policy.ProjectToOrganizationAssignmentRevoked import (
            ProjectToOrganizationAssignmentRevoked,
        )

        DomainPublishedEvents.addEventForPublishing(
            ProjectToOrganizationAssignmentRevoked(
                organization=organization, project=project
            )
        )
        self._repo.revokeProjectToOrganizationAssignment(
            organization=organization, project=project
        )