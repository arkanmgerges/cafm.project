"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.room.BuildingLevelRoom import (
    BuildingLevelRoom,
)
from src.domain_model.token.TokenData import TokenData


class BuildingLevelRepository(ABC):
    @abstractmethod
    def bulkSave(self, objList: List[BuildingLevel], tokenData: TokenData):
        """Bulk save building level list

        Args:
            objList (List[BuildingLevel]): The building level list that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def bulkDelete(self, objList: List[BuildingLevel], tokenData: TokenData):
        """Bulk delete building level list

        Args:
            objList (List[BuildingLevel]): The building level list that needs to be deleted
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def save(self, obj: BuildingLevel, tokenData: TokenData):
        """Save building level

        Args:
            obj (BuildingLevel): The building level that needs to be saved
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
    def linkBuildingLevelToBuilding(
        self, buildingLevel: BuildingLevel, building: Building, tokenData: TokenData
    ) -> None:
        """Link building level to building

        Args:
            buildingLevel (BuildingLevel): The building level that will be linked to the building
            building (Building): The building that will be linked to the building level
        """

    @abstractmethod
    def unlinkBuildingLevelFromBuilding(
        self, buildingLevel: BuildingLevel, building: Building, tokenData: TokenData
    ) -> None:
        """Unlink building level from building

        Args:
            buildingLevel (BuildingLevel): The building level that will be unlinked from the building
            building (Building): The building that will be unlinked from the building level
        """

    @abstractmethod
    def addBuildingLevelRoomToBuildingLevel(
        self,
        buildingLevelRoom: BuildingLevelRoom,
        buildingLevel: BuildingLevel,
        tokenData: TokenData,
    ):
        """Add a room into a building level

        Args:
            buildingLevelRoom (BuildingLevelRoom): The building level room that needs to be added to the building level
            buildingLevel (BuildingLevel): The building level that will contain the building level room
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def removeBuildingLevelRoomFromBuildingLevel(
        self,
        buildingLevelRoom: BuildingLevelRoom,
        buildingLevel: BuildingLevel,
        tokenData: TokenData,
    ):
        """Remove a room from building level

        Args:
            buildingLevelRoom (BuildingLevelRoom): The building level room that needs to be removed from the building level
            buildingLevel (BuildingLevel): The building level that contains the building level room
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def buildingLevels(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        include: List[str] = None,
        buildingId: str = None,
    ) -> dict:
        """Get list of building levels based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'id', 'direction': 'desc'}]
            include (List[str]): A list of string that is used to include inner data
            buildingId (str): A building id for the building levels

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """

    @abstractmethod
    def buildingLevelById(
        self, id: str, include: List[str], tokenData: TokenData
    ) -> BuildingLevel:
        """Get building level by id

        Args:
            id (str): The id of the building level
            include (List[str]): A list of string that is used to include inner data
            tokenData (TokenData): A token data object

        Returns:
            BuildingLevel: building level object

        :raises:
            `BuildingLevelDoesNotExistException <src.domain_model.resource.exception.BuildingLevelDoesNotExistException>`
            Raise an exception if the building level does not exist
        """
