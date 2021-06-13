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
    def bulkSave(self, objList: List[dict], tokenData: TokenData = None):
        """Bulk save building level list

        Args:
            objList (List[dict]): The building level list with building id that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def bulkDelete(self, objList: List[BuildingLevel], tokenData: TokenData = None):
        """Bulk delete building level list

        Args:
            objList (List[BuildingLevel]): The building level list that needs to be deleted
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def save(self, obj: BuildingLevel, tokenData: TokenData = None):
        """Save building level

        Args:
            obj (BuildingLevel): The building level that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def deleteBuildingLevel(self, obj: BuildingLevel, tokenData: TokenData = None) -> None:
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
        self, buildingLevel: BuildingLevel, building: Building, tokenData: TokenData = None
    ) -> None:
        """Link building level to building

        Args:
            buildingLevel (BuildingLevel): The building level that will be linked to the building
            building (Building): The building that will be linked to the building level
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def unlinkBuildingLevelFromBuilding(
        self, buildingLevel: BuildingLevel, building: Building, tokenData: TokenData = None
    ) -> None:
        """Unlink building level from building

        Args:
            buildingLevel (BuildingLevel): The building level that will be unlinked from the building
            building (Building): The building that will be unlinked from the building level
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def addBuildingLevelRoomToBuildingLevel(
        self,
        buildingLevelRoom: BuildingLevelRoom,
        buildingLevel: BuildingLevel,
        tokenData: TokenData = None,
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
        tokenData: TokenData = None,
    ):
        """Remove a room from building level

        Args:
            buildingLevelRoom (BuildingLevelRoom): The building level room that needs to be removed from the building level
            buildingLevel (BuildingLevel): The building level that contains the building level room
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def removeBuildingLevel(self,
                            buildingLevel: BuildingLevel,
                            tokenData: TokenData,
                            ignoreRelations: bool):
        """Remove a building level

        Args:
            buildingLevel (BuildingLevel): The building level that needs to be removed
            tokenData (TokenData): Token data that has info about the token
            ignoreRelations (bool): Ignore relational checks if it is true, else throw an error if there is any enforced relational checks
        """

    @abstractmethod
    def buildingLevels(
        self,
        tokenData: TokenData = None,
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
    def buildingLevelsByBuildingId(self, buildingId: str, resultSize: int = 100) -> List[BuildingLevel]:
        """Get list of building levels by building id

        Args:
            buildingId (str): A building id for the building levels
            resultSize (int): The size of the items in the result
        """

    @abstractmethod
    def buildingLevelById(
        self, id: str, include: List[str], tokenData: TokenData = None
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
