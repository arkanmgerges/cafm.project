"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.application.lookup.user.UserLookup import UserLookup
from src.domain_model.common.model.UserIncludesOrganizationsAndRoles import UserIncludesOrganizationsAndRoles
from src.domain_model.token.TokenData import TokenData


class UserLookupRepository(ABC):
    @abstractmethod
    def userLookupByUserId(self, id: str) -> UserLookup:
        """Get user lookup by user id

        Args:
            id (str): The id of the user lookup

        Returns:
            UserLookup: user lookup object

        """

    @abstractmethod
    def userLookupByUserEmail(self, email: str) -> UserLookup:
        """Get user lookup by user email

        Args:
            email (str): The email of the user lookup

        Returns:
            UserLookup: user lookup object

        """

    @abstractmethod
    def lookup(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        filter: List[dict] = None
    ) -> dict:
        """Get list of user lookups based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'age', 'direction': 'desc'}]
            filter (List[dict]): A list of filters e.g. [{'user.name': 'John', 'user.age': '38'},]
        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """

    @abstractmethod
    def usersFilteredByUsersIncludeOrganizationsAndRoles(
            self,
            tokenData: TokenData,
            resultFrom: int = 0,
            resultSize: int = 10,
            order: List[dict] = None,
            filter: List[dict] = None,
            usersIncludeOrganizationsAndRoles: List[UserIncludesOrganizationsAndRoles] = None,
    ) -> dict:
     """Retrieve users that include organizations and roles by list of users that include organizations and roles

             Args:
                 tokenData (TokenData): A token data object
                 resultFrom (int): The start offset of the result item
                 resultSize (int): The size of the items in the result
                 order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                     {'orderBy': 'age', 'direction': 'desc'}]
                 filter (List[dict]): A list of filters e.g. [{'user.name': 'John', 'user.age': '38'},]
                 usersIncludeOrganizationsAndRoles (List[UserIncludesOrganizationsAndRoles]): List of user
                     objects that include organizations and roles to be used for filtering

             Returns:
                 dict: A dict that has {"items": [], "totalItemCount": 0}
             """
