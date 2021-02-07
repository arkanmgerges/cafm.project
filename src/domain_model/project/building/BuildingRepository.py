"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod

from src.domain_model.project.building.Building import Building
from src.domain_model.token.TokenData import TokenData


class BuildingRepository(ABC):
    @abstractmethod
    def save(self, obj: Building, tokenData: TokenData):
        """Save building

        Args:
            obj (Building): The building that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def createBuilding(self, obj: Building, tokenData: TokenData):
        """Create building

        Args:
            obj (Building): The building that needs to be created
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteBuilding(self, obj: Building, tokenData: TokenData) -> None:
        """Delete a building

        Args:
            obj (Building): The building that needs to be deleted
            tokenData (TokenData): Token data used for deleting the building

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the building could not be deleted
        """

    @abstractmethod
    def buildingById(self, id: str) -> Building:
        """Get building by id

        Args:
            id (str): The id of the building

        Returns:
            Building: building object

        :raises:
            `BuildingDoesNotExistException <src.domain_model.resource.exception.BuildingDoesNotExistException>`
            Raise an exception if the building does not exist
        """

    @abstractmethod
    def save(self, obj: Building):
        """Save building

        Args:
            obj (Building): Building to be saved
        """