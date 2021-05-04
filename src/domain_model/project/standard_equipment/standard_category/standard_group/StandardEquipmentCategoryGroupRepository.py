"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List
from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroup import (
    StandardEquipmentCategoryGroup,
)
from src.domain_model.token.TokenData import TokenData


class StandardEquipmentCategoryGroupRepository(ABC):
    @abstractmethod
    def bulkSave(self, objList: List[StandardEquipmentCategoryGroup], tokenData: TokenData):
        """Bulk save standard equipment category group list

        Args:
            objList (List[StandardEquipmentCategoryGroup]): The standard equipment category group list that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def bulkDelete(self, objList: List[StandardEquipmentCategoryGroup], tokenData: TokenData):
        """Bulk delete standard equipment category group list

        Args:
            objList (List[StandardEquipmentCategoryGroup]): The standard equipment category group list that needs to be deleted
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def save(self, obj: StandardEquipmentCategoryGroup, tokenData: TokenData):
        """Save standard equipment category group

        Args:
            obj (StandardEquipmentCategoryGroup): The standard equipment category group that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteStandardEquipmentCategoryGroup(
        self, obj: StandardEquipmentCategoryGroup, tokenData: TokenData
    ) -> None:
        """Delete a standard equipment category group

        Args:
            obj (StandardEquipmentCategoryGroup): The standard equipment category group that needs to be deleted
            tokenData (TokenData): Token data used for deleting the standard equipment category group

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the standard equipment category group could not be deleted
        """

    @abstractmethod
    def standardEquipmentCategoryGroupById(
        self, id: str
    ) -> StandardEquipmentCategoryGroup:
        """Get standard equipment category group by id

        Args:
            id (str): The id of the standard equipment category group

        Returns:
            StandardEquipmentCategoryGroup: standard equipment category group object

        :raises:
            `StandardEquipmentCategoryGroupDoesNotExistException <src.domain_model.resource.exception.StandardEquipmentCategoryGroupDoesNotExistException>`
            Raise an exception if the standard equipment category group does not exist
        """

    @abstractmethod
    def standardEquipmentCategoryGroups(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of standard equipment category groups based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'quantity', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """
