"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from src.domain_model.tag.Tag import Tag

from src.domain_model.project.Project import Project
from src.domain_model.organization.Organization import Organization
from src.domain_model.role.Role import Role
from src.domain_model.token.TokenData import TokenData
from src.domain_model.user.User import User


class PolicyRepository(ABC):
    @abstractmethod
    def assignRoleToUser(self, role: Role, user: User, tokenData: TokenData = None):
        """Assign role to user policy

        Args:
            role (Role): The role to be assigned to the user
            user (User): The user that will have the role assigned to
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def revokeRoleToUserAssignment(
        self, role: Role, user: User, tokenData: TokenData = None
    ):
        """Revoke role to user policy

        Args:
            role (Role): The role to be revoked from the user
            user (User): The user that will have the role revoked from
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def assignUserToOrganization(
        self, organization: Organization, user: User, tokenData: TokenData
    ):
        """Assign organization to user policy

        Args:
            organization (Organization): The organization to be assigned to the user
            user (User): The user that will have the organization assigned to
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def revokeUserToOrganizationAssignment(
        self, organization: Organization, user: User, tokenData: TokenData
    ):
        """Revoke organization to user policy

        Args:
            organization (Organization): The organization to be revoked from the user
            user (User): The user that will have the organization revoked from
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def assignRoleToOrganization(
        self, role: Role, organization: Organization, tokenData: TokenData
    ):
        """Assign role to organization policy

        Args:
            organization (Organization): The organization to be assigned to the user
            role (Role): The role that will have the organization assigned to
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def revokeRoleToOrganizationAssignment(
        self, role: Role, organization: Organization, tokenData: TokenData
    ):
        """Revoke role to organization assignment policy

        Args:
            organization (Organization): The organization to be revoked from the role
            role (Role): The role that will have the organization revoked from
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def assignRoleToProject(self, role: Role, project: Project, tokenData: TokenData):
        """Assign role to project policy

        Args:
            project (Project): The project to be assigned to the user
            role (Role): The role that will have the project assigned to
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def revokeRoleToProjectAssignment(
        self, role: Role, project: Project, tokenData: TokenData
    ):
        """Revoke role to project assignment policy

        Args:
            project (Project): The project to be revoked from the role
            role (Role): The role that will have the project revoked from
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def assignProjectToOrganization(
        self, organization: Organization, project: User, tokenData: TokenData
    ):
        """Assign organization to project policy

        Args:
            organization (Organization): The organization to be assigned to the project
            project (Project): The project that will have the organization assigned to
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def revokeProjectToOrganizationAssignment(
        self, organization: Organization, project: Project, tokenData: TokenData
    ):
        """Revoke organization to project policy

        Args:
            organization (Organization): The organization to be revoked from the project
            project (Project): The project that will have the organization revoked from
            tokenData (TokenData): Token data that has info about the token
        """