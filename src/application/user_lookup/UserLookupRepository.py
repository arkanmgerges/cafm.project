"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.application.user_lookup.UserLookup import UserLookup
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
    def userLookups(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
                    order: List[dict] = None) -> dict:
        """Get list of user lookups based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'age', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "itemCount": 0}
        """
