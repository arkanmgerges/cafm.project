"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import (
    EquipmentCategoryGroup,
)
from src.domain_model.token.TokenData import TokenData


class EquipmentCategoryGroupRepository(ABC):
    @abstractmethod
    def bulkSave(self, objList: List[EquipmentCategoryGroup], tokenData: TokenData = None):
        """Bulk save equipment category group list

        Args:
            objList (List[EquipmentCategoryGroup]): The equipment category group list that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def bulkDelete(self, objList: List[EquipmentCategoryGroup], tokenData: TokenData = None):
        """Bulk delete equipment category group list

        Args:
            objList (List[EquipmentCategoryGroup]): The equipment category group list that needs to be deleted
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def save(self, obj: EquipmentCategoryGroup, tokenData: TokenData = None):
        """Save equipment category group

        Args:
            obj (EquipmentCategoryGroup): The equipment category group that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteEquipmentCategoryGroup(
        self, obj: EquipmentCategoryGroup, tokenData: TokenData
    ) -> None:
        """Delete a equipment category group

        Args:
            obj (EquipmentCategoryGroup): The equipment category group that needs to be deleted
            tokenData (TokenData): Token data used for deleting the equipment category group

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the equipment category group could not be deleted
        """

    @abstractmethod
    def equipmentCategoryGroupById(self, id: str) -> EquipmentCategoryGroup:
        """Get equipment category group by id

        Args:
            id (str): The id of the equipment category group

        Returns:
            EquipmentCategoryGroup: equipment category group object

        :raises:
            `EquipmentCategoryGroupDoesNotExistException <src.domain_model.resource.exception.EquipmentCategoryGroupDoesNotExistException>`
            Raise an exception if the equipment category group does not exist
        """

    @abstractmethod
    def equipmentCategoryGroupByNameAndProjectId(self, name: str, projectId: str) -> EquipmentCategoryGroup:
        """Get equipment category group by id and project id

        Args:
            id (str): The id of the equipment category group
            projectId (str): The id of the equipment category group


        Returns:
            EquipmentCategoryGroup: equipment category group object
        """

    @abstractmethod
    def equipmentCategoryGroups(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of equipment category groups based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'quantity', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """

