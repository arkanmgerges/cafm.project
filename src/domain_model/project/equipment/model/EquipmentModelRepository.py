"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain_model.project.equipment.model.EquipmentModel import EquipmentModel
from src.domain_model.token.TokenData import TokenData


class EquipmentModelRepository(ABC):
    @abstractmethod
    def save(self, obj: EquipmentModel, tokenData: TokenData):
        """Save equipment model

        Args:
            obj (EquipmentModel): The equipment model that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteEquipmentModel(self, obj: EquipmentModel, tokenData: TokenData) -> None:
        """Delete a equipment model

        Args:
            obj (EquipmentModel): The equipment model that needs to be deleted
            tokenData (TokenData): Token data used for deleting the equipment model

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the equipment model could not be deleted
        """

    @abstractmethod
    def equipmentModelByName(self, name: str) -> EquipmentModel:
        """Get equipment model by name

        Args:
            name (str): The name of the equipment model

        Returns:
            EquipmentModel: equipment model object

        :raises:
            `EquipmentModelDoesNotExistException <src.domain_model.resource.exception.EquipmentModelDoesNotExistException>`
            Raise an exception if the equipment model does not exist
        """

    @abstractmethod
    def equipmentModelById(self, id: str) -> EquipmentModel:
        """Get equipment model by id

        Args:
            id (str): The id of the equipment model

        Returns:
            EquipmentModel: equipment model object

        :raises:
            `EquipmentModelDoesNotExistException <src.domain_model.resource.exception.EquipmentModelDoesNotExistException>`
            Raise an exception if the equipment model does not exist
        """

    @abstractmethod
    def equipmentModels(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of equipment models based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'quantity', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "itemCount": 0}
        """
