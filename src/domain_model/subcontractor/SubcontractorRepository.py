"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from abc import ABC, abstractmethod

from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.token.TokenData import TokenData


class SubcontractorRepository(ABC):
    @abstractmethod
    def save(self, obj: Subcontractor, tokenData: TokenData):
        """Save subcontractor

        Args:
            obj (Subcontractor): The subcontractor that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def createSubcontractor(self, obj: Subcontractor, tokenData: TokenData):
        """Create subcontractor

        Args:
            obj (Subcontractor): The subcontractor that needs to be created
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteSubcontractor(self, obj: Subcontractor, tokenData: TokenData) -> None:
        """Delete an subcontractor

        Args:
            obj (Organization): The subcontractor that needs to be deleted
            tokenData (TokenData): Token data used for deleting the subcontractor

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the subcontractor could not be deleted
        """

    @abstractmethod
    def updateSubcontractor(self, obj: Subcontractor, tokenData: TokenData) -> None:
        """Update a subcontractor

        Args:
            obj (Subcontractor): The subcontractor that needs to be updated
            tokenData (TokenData): Token data used for updating the subcontractor

        :raises:
            `ObjectCouldNotNotBeUpdatedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeUpdatedException>`
            Raise an exception if the subcontractor could not be updated
        """

    @abstractmethod
    def subcontractorByName(self, companyName: str) -> Subcontractor:
        """Get subcontractor by name

        Args:
            name (str): The name of the subcontractor

        Returns:
            Organization: subcontractor object

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
            Organization: subcontractor object

        :raises:
            `SubcontractorDoesNotExistException <src.domain_model.resource.exception.SubcontractorDoesNotExistException>`
            Raise an exception if the subcontractor does not exist
        """