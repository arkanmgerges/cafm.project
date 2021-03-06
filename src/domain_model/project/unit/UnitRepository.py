"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List
from src.domain_model.project.unit.Unit import Unit
from src.domain_model.token.TokenData import TokenData


class UnitRepository(ABC):
    @abstractmethod
    def bulkSave(self, objList: List[Unit], tokenData: TokenData = None):
        """Bulk save unit list

        Args:
            objList (List[Unit]): The unit list that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def bulkDelete(self, objList: List[Unit], tokenData: TokenData = None):
        """Bulk delete unit list

        Args:
            objList (List[Unit]): The unit list that needs to be deleted
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def save(self, obj: Unit, tokenData: TokenData = None):
        """Save unit

        Args:
            obj (Unit): The unit that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteUnit(self, obj: Unit, tokenData: TokenData) -> None:
        """Delete a unit

        Args:
            obj (Unit): The unit that needs to be deleted
            tokenData (TokenData): Token data used for deleting the unit

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the unit could not be deleted
        """

    @abstractmethod
    def unitById(self, id: str) -> Unit:
        """Get unit by id

        Args:
            id (str): The id of the unit

        Returns:
            Unit: unit object

        :raises:
            `UnitDoesNotExistException <src.domain_model.resource.exception.UnitDoesNotExistException>`
            Raise an exception if the unit does not exist
        """

    @abstractmethod
    def units(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of units based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'quantity', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """
