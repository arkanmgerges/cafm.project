"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from abc import ABC, abstractmethod
from typing import List

from src.domain_model.organization.Organization import Organization
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.token.TokenData import TokenData


class SubcontractorRepository(ABC):
    @abstractmethod
    def bulkSave(self, objList: List[Subcontractor], tokenData: TokenData):
        """Bulk save subcontractor list

        Args:
            objList (List[Subcontractor]): The subcontractor list that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def bulkDelete(self, objList: List[Subcontractor], tokenData: TokenData):
        """Bulk delete subcontractor list

        Args:
            objList (List[Subcontractor]): The subcontractor list that needs to be deleted
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def save(self, obj: Subcontractor, tokenData: TokenData):
        """Save subcontractor

        Args:
            obj (Subcontractor): The subcontractor that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteSubcontractor(self, obj: Subcontractor, tokenData: TokenData) -> None:
        """Delete an subcontractor

        Args:
            obj (Subcontractor): The subcontractor that needs to be deleted
            tokenData (TokenData): Token data used for deleting the subcontractor

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the subcontractor could not be deleted
        """

    @abstractmethod
    def assignSubcontractorToOrganization(
        self,
        subcontractor: Subcontractor,
        organization: Organization,
        tokenData: TokenData,
    ):
        """Assign subcontractor to organization

        Args:
            subcontractor (Subcontractor): The subcontractor to be assigned to the organization
            organization (Organization): The organization that will have the subcontractor assigned to
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def revokeRoleToUserAssignment(
        self,
        subcontractor: Subcontractor,
        organization: Organization,
        tokenData: TokenData,
    ):
        """Revoke subcontractor from organization

        Args:
            subcontractor (Subcontractor): The subcontractor to be revoked from the organization
            organization (Organization): The organization that will have the subcontractor revoked from
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def subcontractorByName(self, companyName: str) -> Subcontractor:
        """Get subcontractor by name

        Args:
            name (str): The name of the subcontractor

        Returns:
            Subcontractor: subcontractor object

        :raises:
            `SubcontractorDoesNotExistException <src.domain_model.resource.exception.SubcontractorDoesNotExistException>`
            Raise an exception if the subcontractor does not exist
        """

    @abstractmethod
    def subcontractorById(self, id: str) -> Subcontractor:
        """Get subcontractor by id

        Args:
            id (str): The id of the subcontractor

        Returns:
            Subcontractor: subcontractor object

        :raises:
            `SubcontractorDoesNotExistException <src.domain_model.resource.exception.SubcontractorDoesNotExistException>`
            Raise an exception if the subcontractor does not exist
        """

    @abstractmethod
    def subcontractors(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of subcontractors

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'age', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "itemCount": 0}
        """

    @abstractmethod
    def subcontractorsByOrganizationId(
        self,
        organizationId: str,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of subcontractors

        Args:
            organizationId (str): The id of organization
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'age', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "itemCount": 0}
        """

    @abstractmethod
    def subcontractorsBySubcontractorCategoryId(
        self,
        subcontractorCategoryId: str,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        """Get list of subcontractors by subcontractor category id

        Args:
            subcontractorCategoryId (str): The id of subcontractor category
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'age', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "itemCount": 0}
        """
