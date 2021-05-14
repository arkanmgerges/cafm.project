"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List
from src.domain_model.subcontractor.category.SubcontractorCategory import (
    SubcontractorCategory,
)
from src.domain_model.token.TokenData import TokenData


class SubcontractorCategoryRepository(ABC):
    @abstractmethod
    def save(self, obj: SubcontractorCategory, tokenData: TokenData = None):
        """Save subcontractor category

        Args:
            obj (SubcontractorCategory): The subcontractor category that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteSubcontractorCategory(
        self, obj: SubcontractorCategory, tokenData: TokenData
    ) -> None:
        """Delete a subcontractor category

        Args:
            obj (SubcontractorCategory): The subcontractor category that needs to be deleted
            tokenData (TokenData): Token data used for deleting the subcontractor category

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the subcontractor category could not be deleted
        """

    @abstractmethod
    def bulkSave(self, objList: List[SubcontractorCategory], tokenData: TokenData = None):
        """Bulk save subcontractor category list

        Args:
            objList (List[SubcontractorCategory]): The subcontractor category list that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def bulkDelete(self, objList: List[SubcontractorCategory], tokenData: TokenData = None):
        """Bulk delete subcontractor category list

        Args:
            objList (List[SubcontractorCategory]): The subcontractor category list that needs to be deleted
            tokenData (TokenData): Token data that has info about the token

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the subcontractor category could not be deleted
        """

    @abstractmethod
    def subcontractorCategoryById(self, id: str) -> SubcontractorCategory:
        """Get subcontractor category by id

        Args:
            id (str): The id of the subcontractor category

        Returns:
            SubcontractorCategory: subcontractor category object

        :raises:
            `SubcontractorCategoryDoesNotExistException <src.domain_model.resource.exception.SubcontractorCategoryDoesNotExistException>`
            Raise an exception if the subcontractor category does not exist
        """

    @abstractmethod
    def subcontractorCategories(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of subcontractor categories based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'quantity', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """
