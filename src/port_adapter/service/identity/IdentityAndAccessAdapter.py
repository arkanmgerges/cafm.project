"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod

from src.domain_model.project.Project import Project
from src.domain_model.token.TokenData import TokenData
from src.domain_model.user.User import User


class IdentityAndAccessAdapter(ABC):
    @abstractmethod
    def projectById(self, tokenData: TokenData = None, id: str = None) -> Project:
        """Retrieve projects

        Args:
            tokenData (TokenData): Token data that has info about the token
            id (str): Project id

        """

    @abstractmethod
    def projects(self, tokenData: TokenData = None) -> dict:
        """Retrieve projects

        Args:
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def projectsByOrganizationId(self, tokenData: TokenData = None, organizationId: str = None) -> dict:
        """Retrieve projects by organization id

        Args:
            tokenData (TokenData): Token data that has info about the token
            organizationId (str): Organization id used to retrieve the projects
        """

    @abstractmethod
    def organizations(self, tokenData: TokenData = None) -> dict:
        """Retrieve organizations

        Args:
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def organizationById(self, tokenData: TokenData = None, id: str = None) -> dict:
        """Retrieve organization by id

        Args:
            tokenData (TokenData): Token data that has info about the token
            id (str): Organization id

        """

    @abstractmethod
    def organizationsByType(self, tokenData: TokenData = None, type: str = None) -> dict:
        """Retrieve organizations by type

        Args:
            tokenData (TokenData): Token data that has info about the token
            type (str): Organizations by type

        """

    @abstractmethod
    def userById(self, tokenData: TokenData = None, id: str = None) -> User:
        """Retrieve users

        Args:
            tokenData (TokenData): Token data that has info about the token
            id (str): User id

        """

    @abstractmethod
    def users(self, tokenData: TokenData = None) -> dict:
        """Retrieve users

        Args:
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def organizationsIncludeUsersIncludeRoles(self, tokenData: TokenData = None,) -> dict:
        """Retrieve organizations that include users that include roles

        Args:
            tokenData (TokenData): Token data that has info about the token
        """