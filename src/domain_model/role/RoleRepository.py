"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain_model.role.Role import Role
from src.domain_model.token.TokenData import TokenData


class RoleRepository(ABC):
    @abstractmethod
    def save(self, obj: Role, tokenData: TokenData = None):
        """Save role

        Args:
            obj (Role): The role that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteRole(self, obj: Role, tokenData: TokenData) -> None:
        """Delete a role

        Args:
            obj (Role): The role that needs to be deleted
            tokenData (TokenData): Token data used for deleting the role

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the role could not be deleted
        """

    @abstractmethod
    def roleByName(self, name: str) -> Role:
        """Get role by name

        Args:
            name (str): The name of the role

        Returns:
            Role: role object

        :raises:
            `RoleDoesNotExistException <src.domain_model.resource.exception.RoleDoesNotExistException>`
            Raise an exception if the role does not exist
        """

    @abstractmethod
    def roleById(self, id: str) -> Role:
        """Get role by id

        Args:
            id (str): The id of the role

        Returns:
            Role: role object

        :raises:
            `RoleDoesNotExistException <src.domain_model.resource.exception.RoleDoesNotExistException>`
            Raise an exception if the role does not exist
        """

    @abstractmethod
    def roles(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of roles based on the owned roles that the role has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'age', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """
