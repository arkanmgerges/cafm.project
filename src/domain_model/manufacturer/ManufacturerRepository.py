"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain_model.manufacturer.Manufacturer import Manufacturer
from src.domain_model.token.TokenData import TokenData


class ManufacturerRepository(ABC):
    @abstractmethod
    def save(self, obj: Manufacturer, tokenData: TokenData):
        """Save manufacturer

        Args:
            obj (Manufacturer): The manufacturer that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteManufacturer(self, obj: Manufacturer, tokenData: TokenData) -> None:
        """Delete a manufacturer

        Args:
            obj (Manufacturer): The manufacturer that needs to be deleted
            tokenData (TokenData): Token data used for deleting the manufacturer

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the manufacturer could not be deleted
        """

    @abstractmethod
    def manufacturerByName(self, name: str) -> Manufacturer:
        """Get manufacturer by name

        Args:
            name (str): The name of the manufacturer

        Returns:
            Manufacturer: manufacturer object
            
        :raises:
            `ManufacturerDoesNotExistException <src.domain_model.resource.exception.ManufacturerDoesNotExistException>`
            Raise an exception if the manufacturer does not exist
        """

    @abstractmethod
    def manufacturerById(self, id: str) -> Manufacturer:
        """Get manufacturer by id

        Args:
            id (str): The id of the manufacturer

        Returns:
            Manufacturer: manufacturer object

        :raises:
            `ManufacturerDoesNotExistException <src.domain_model.resource.exception.ManufacturerDoesNotExistException>`
            Raise an exception if the manufacturer does not exist
        """

    @abstractmethod
    def manufacturers(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
                 order: List[dict] = None) -> dict:
        """Get list of manufacturers based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'quantity', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "itemCount": 0}
        """
