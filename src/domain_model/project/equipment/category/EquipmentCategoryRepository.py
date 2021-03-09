"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain_model.project.equipment.category.EquipmentCategory import EquipmentCategory
from src.domain_model.token.TokenData import TokenData


class EquipmentCategoryRepository(ABC):
    @abstractmethod
    def save(self, obj: EquipmentCategory, tokenData: TokenData):
        """Save equipment category

        Args:
            obj (EquipmentCategory): The equipment category that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteEquipmentCategory(self, obj: EquipmentCategory, tokenData: TokenData) -> None:
        """Delete a equipment category

        Args:
            obj (EquipmentCategory): The equipment category that needs to be deleted
            tokenData (TokenData): Token data used for deleting the equipment category

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the equipment category could not be deleted
        """

    @abstractmethod
    def equipmentCategoryByName(self, name: str) -> EquipmentCategory:
        """Get equipment category by name

        Args:
            name (str): The name of the equipment category

        Returns:
            EquipmentCategory: equipment category object
            
        :raises:
            `EquipmentCategoryDoesNotExistException <src.domain_model.resource.exception.EquipmentCategoryDoesNotExistException>`
            Raise an exception if the equipment category does not exist
        """

    @abstractmethod
    def equipmentCategoryById(self, id: str) -> EquipmentCategory:
        """Get equipment category by id

        Args:
            id (str): The id of the equipment category

        Returns:
            EquipmentCategory: equipment category object

        :raises:
            `EquipmentCategoryDoesNotExistException <src.domain_model.resource.exception.EquipmentCategoryDoesNotExistException>`
            Raise an exception if the equipment category does not exist
        """

    @abstractmethod
    def equipmentCategories(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
                            order: List[dict] = None) -> dict:
        """Get list of equipment categories based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'quantity', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "itemCount": 0}
        """
