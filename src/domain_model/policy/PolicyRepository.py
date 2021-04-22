"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod

from src.domain_model.organization.Organization import Organization
from src.domain_model.role.Role import Role
from src.domain_model.token.TokenData import TokenData
from src.domain_model.user.User import User


class PolicyRepository(ABC):
    @abstractmethod
    def assignRoleToUser(self, role: Role, user: User, tokenData: TokenData):
        """Assign role to user policy

        Args:
            role (Role): The role to be assigned to the user
            user (User): The user that will have the role assigned to
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def revokeRoleToUserAssignment(self, role: Role, user: User, tokenData: TokenData):
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
    def assignRoleToOrganization(self, role: Role, organization: Organization, tokenData: TokenData):
        """Assign role to organization policy

        Args:
            organization (Organization): The organization to be assigned to the user
            role (Role): The role that will have the organization assigned to
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def revokeRoleToOrganizationAssignment(self, role: Role, organization: Organization, tokenData: TokenData):
        """Revoke role to organization assignment policy

        Args:
            organization (Organization): The organization to be revoked from the role
            role (Role): The role that will have the organization revoked from
            tokenData (TokenData): Token data that has info about the token
        """
