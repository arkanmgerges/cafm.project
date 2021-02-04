"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain_model.organization.Organization import Organization
from src.domain_model.token.TokenData import TokenData


class OrganizationRepository(ABC):
    @abstractmethod
    def save(self, obj: Organization, tokenData: TokenData):
        """Save organization

        Args:
            obj (Organization): The organization that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def createOrganization(self, obj: Organization, tokenData: TokenData):
        """Create organization

        Args:
            obj (Organization): The organization that needs to be created
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteOrganization(self, obj: Organization, tokenData: TokenData) -> None:
        """Delete an organization

        Args:
            obj (Organization): The organization that needs to be deleted
            tokenData (TokenData): Token data used for deleting the organization

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the organization could not be deleted
        """

    @abstractmethod
    def updateOrganization(self, obj: Organization, tokenData: TokenData) -> None:
        """Update a organization

        Args:
            obj (Organization): The organization that needs to be updated
            tokenData (TokenData): Token data used for updating the organization

        :raises:
            `ObjectCouldNotNotBeUpdatedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeUpdatedException>`
            Raise an exception if the organization could not be updated
        """

    @abstractmethod
    def organizationByName(self, name: str) -> Organization:
        """Get organization by name

        Args:
            name (str): The name of the organization

        Returns:
            Organization: organization object
            
        :raises:
            `OrganizationDoesNotExistException <src.domain_model.resource.exception.OrganizationDoesNotExistException>`
            Raise an exception if the organization does not exist
        """

    @abstractmethod
    def organizationById(self, id: str) -> Organization:
        """Get organization by id

        Args:
            id (str): The id of the organization

        Returns:
            Organization: organization object

        :raises:
            `OrganizationDoesNotExistException <src.domain_model.resource.exception.OrganizationDoesNotExistException>`
            Raise an exception if the organization does not exist
        """

    @abstractmethod
    def organizations(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
                      order: List[dict] = None) -> dict:
        """Get list of organizations based on the owned roles that the organization has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'age', 'direction': 'desc'}]

        Returns:
            dict: A dict that has {"items": [], "itemCount": 0}
        """
