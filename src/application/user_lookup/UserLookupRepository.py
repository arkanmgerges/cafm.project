"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod

from src.application.user_lookup.UserLookup import UserLookup


class UserLookupRepository(ABC):
    @abstractmethod
    def userLookupByUserId(self, id: str) -> UserLookup:
        """Get user lookup by user id

        Args:
            id (str): The id of the user lookup

        Returns:
            UserLookup: user lookup object

        """
