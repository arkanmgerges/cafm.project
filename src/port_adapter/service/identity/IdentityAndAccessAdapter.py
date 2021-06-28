"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod

from src.domain_model.token.TokenData import TokenData


class IdentityAndAccessAdapter(ABC):
    @abstractmethod
    def projects(self, tokenData: TokenData = None) -> dict:
        """Retrieve projects

        Args:
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def projectsByRealmId(self, tokenData: TokenData = None, realmId: str = None) -> dict:
        """Retrieve projects by realm id

        Args:
            tokenData (TokenData): Token data that has info about the token
            realmId (str): Organization id used to retrieve the projects
        """