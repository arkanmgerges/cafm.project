"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain_model.project.equipment.project_category.EquipmentProjectCategory import (
    EquipmentProjectCategory,
)
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import (
    EquipmentCategoryGroup,
)
from src.domain_model.token.TokenData import TokenData


class EquipmentProjectCategoryRepository(ABC):
    @abstractmethod
    def bulkSave(self, objList: List[EquipmentProjectCategory], tokenData: TokenData = None):
        """Bulk save equipment project category list

        Args:
            objList (List[EquipmentProjectCategory]): The equipment project category list that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def bulkDelete(self, objList: List[EquipmentProjectCategory], tokenData: TokenData = None):
        """Bulk delete equipment project category list

        Args:
            objList (List[EquipmentProjectCategory]): The equipment project category list that needs to be deleted
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def save(self, obj: EquipmentProjectCategory, tokenData: TokenData = None):
        """Save equipment project category

        Args:
            obj (EquipmentProjectCategory): The equipment project category that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteEquipmentProjectCategory(
        self, obj: EquipmentProjectCategory, tokenData: TokenData
    ) -> None:
        """Delete a equipment project category

        Args:
            obj (EquipmentProjectCategory): The equipment project category that needs to be deleted
            tokenData (TokenData): Token data used for deleting the equipment project category

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the equipment project category could not be deleted
        """

    @abstractmethod
    def equipmentProjectCategoryByName(self, name: str) -> EquipmentProjectCategory:
        """Get equipment project category by name

        Args:
            name (str): The name of the equipment project category

        Returns:
            EquipmentProjectCategory: equipment project category object

        :raises:
            `EquipmentProjectCategoryDoesNotExistException <src.domain_model.resource.exception.EquipmentProjectCategoryDoesNotExistException>`
            Raise an exception if the equipment project category does not exist
        """

    @abstractmethod
    def equipmentProjectCategoryById(self, id: str) -> EquipmentProjectCategory:
        """Get equipment project category by id

        Args:
            id (str): The id of the equipment project category

        Returns:
            EquipmentProjectCategory: equipment project category object

        :raises:
            `EquipmentProjectCategoryDoesNotExistException <src.domain_model.resource.exception.EquipmentProjectCategoryDoesNotExistException>`
            Raise an exception if the equipment project category does not exist
        """

    @abstractmethod
    def equipmentProjectCategoriesByProjectId(self, projectId: str) -> EquipmentProjectCategory:
        """Get equipment project categories by project id

        Args:
            projectId (str): The id of the project

        Returns:
            dict: A dict that has {"items": []}
        """

    @abstractmethod
    def equipmentProjectCategories(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of equipment project categories based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'quantity', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """

    @abstractmethod
    def equipmentCategoryGroupsByEquipmentProjectCategoryId(
        self,
        tokenData: TokenData,
        id: str,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of equipment category groups by equipment project category id

        Args:
            id (str): A equipment project category id
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'quantity', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """

    @abstractmethod
    def linkEquipmentProjectCategoryGroup(
        self, category: EquipmentProjectCategory, group: EquipmentCategoryGroup
    ) -> None:
        """Link a equipment project category and equipment category group together

        Args:
            category (EquipmentProjectCategory): A equipment project category
            group (EquipmentCategoryGroup): A equipment category group
        """

    @abstractmethod
    def unLinkEquipmentProjectCategoryGroup(
        self, category: EquipmentProjectCategory, group: EquipmentCategoryGroup
    ) -> None:
        """Unlink a equipment project category from a equipment category group

        Args:
            category (EquipmentProjectCategory): A equipment project category
            group (EquipmentCategoryGroup): A equipment category group
        """
