"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain_model.project.equipment.Equipment import Equipment
from src.domain_model.token.TokenData import TokenData


class EquipmentRepository(ABC):
    @abstractmethod
    def save(self, obj: Equipment, tokenData: TokenData):
        """Save equipment

        Args:
            obj (Equipment): The equipment that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def createEquipment(self, obj: Equipment, tokenData: TokenData):
        """Create equipment

        Args:
            obj (Equipment): The equipment that needs to be created
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteEquipment(self, obj: Equipment, tokenData: TokenData) -> None:
        """Delete a equipment

        Args:
            obj (Equipment): The equipment that needs to be deleted
            tokenData (TokenData): Token data used for deleting the equipment

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the equipment could not be deleted
        """

    @abstractmethod
    def updateEquipment(self, obj: Equipment, tokenData: TokenData) -> None:
        """Update a equipment

        Args:
            obj (Equipment): The equipment that needs to be updated
            tokenData (TokenData): Token data used for updating the equipment

        :raises:
            `ObjectCouldNotNotBeUpdatedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeUpdatedException>`
            Raise an exception if the equipment could not be updated
        """

    @abstractmethod
    def equipmentByName(self, name: str) -> Equipment:
        """Get equipment by name

        Args:
            name (str): The name of the equipment

        Returns:
            Equipment: equipment object
            
        :raises:
            `EquipmentDoesNotExistException <src.domain_model.resource.exception.EquipmentDoesNotExistException>`
            Raise an exception if the equipment does not exist
        """

    @abstractmethod
    def equipmentById(self, id: str) -> Equipment:
        """Get equipment by id

        Args:
            id (str): The id of the equipment

        Returns:
            Equipment: equipment object

        :raises:
            `EquipmentDoesNotExistException <src.domain_model.resource.exception.EquipmentDoesNotExistException>`
            Raise an exception if the equipment does not exist
        """

    @abstractmethod
    def equipments(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
                 order: List[dict] = None) -> dict:
        """Get list of equipments based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'quantity', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "itemCount": 0}
        """
