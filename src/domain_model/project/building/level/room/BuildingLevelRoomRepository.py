"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod

from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.domain_model.token.TokenData import TokenData


class BuildingLevelRoomRepository(ABC):
    @abstractmethod
    def save(self, obj: BuildingLevelRoom, tokenData: TokenData):
        """Save building level room

        Args:
            obj (BuildingLevelRoom): The building level room that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def createBuildingLevelRoom(self, obj: BuildingLevelRoom, tokenData: TokenData):
        """Create building level room

        Args:
            obj (BuildingLevelRoom): The building level room that needs to be created
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteBuildingLevelRoom(self, obj: BuildingLevelRoom, tokenData: TokenData) -> None:
        """Delete a building level room

        Args:
            obj (BuildingLevelRoom): The building level room that needs to be deleted
            tokenData (TokenData): Token data used for deleting the building level

        :raises:
            `ObjectCouldNotNotBeDeletedException
            <src.domain_model.resource.exception.ObjectCouldNotNotBeDeletedException>`
            Raise an exception if the building level could not be deleted
        """

    @abstractmethod
    def buildingLevelRoomById(self, id: str) -> BuildingLevelRoom:
        """Get building level room by id

        Args:
            id (str): The id of the building level room

        Returns:
            BuildingLevelRoom: building level room object

        :raises:
            `BuildingLevelRoomDoesNotExistException <src.domain_model.resource.exception.BuildingLevelRoomDoesNotExistException>`
            Raise an exception if the building level room does not exist
        """
