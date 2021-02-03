"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod

from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.token.TokenData import TokenData


class BuildingLevelRepository(ABC):
    @abstractmethod
    def createBuildingLevel(self, obj: BuildingLevel, tokenData: TokenData):
        """Create building level

        Args:
            obj (BuildingLevel): The building level that needs to be created
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteBuildingLevel(self, obj: BuildingLevel, tokenData: TokenData) -> None:
        """Delete a building level

        Args:
            obj (BuildingLevel): The building level that needs to be deleted
            tokenData (TokenData): Token data used for deleting the building level

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the building level could not be deleted
        """

    @abstractmethod
    def buildingLevelById(self, id: str) -> BuildingLevel:
        """Get building level by id

        Args:
            id (str): The id of the building level

        Returns:
            BuildingLevel: building level object

        :raises:
            `BuildingLevelDoesNotExistException <src.domain_model.resource.exception.BuildingLevelDoesNotExistException>`
            Raise an exception if the building level does not exist
        """
