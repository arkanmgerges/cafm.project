"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain_model.project.building.level.room.BuildingLevelRoom import (
    BuildingLevelRoom,
)
from src.domain_model.token.TokenData import TokenData


class BuildingLevelRoomRepository(ABC):
    @abstractmethod
    def bulkSave(self, objList: List[BuildingLevelRoom], tokenData: TokenData = None):
        """Bulk save building level room list

        Args:
            objList (List[BuildingLevelRoom]): The building level room list that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def bulkDelete(self, objList: List[BuildingLevelRoom], tokenData: TokenData = None):
        """Bulk delete building level room list

        Args:
            objList (List[BuildingLevelRoom]): The building level room list that needs to be deleted
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def save(self, obj: BuildingLevelRoom, tokenData: TokenData = None):
        """Save building level room

        Args:
            obj (BuildingLevelRoom): The building level room that needs to be saved
            tokenData (TokenData): Token data that has info about the token

        """

    @abstractmethod
    def buildingLevelRoomsByBuildingLevelId(self, buildingLevelId: str, resultSize: int = 100) -> List[BuildingLevelRoom]:
        """Get list of building level rooms by building level id

        Args:
            buildingLevelId (str): A building level id for the building level rooms
            resultSize (int): The size of the items in the result
        """

    @abstractmethod
    def removeBuildingLevelRoom(self,
                                buildingLevelRoom: BuildingLevelRoom,
                                tokenData: TokenData,
                                ignoreRelations: bool):
        """Remove a building level room

        Args:
            buildingLevelRoom (BuildingLevelRoom): The building level room that needs to be removed
            tokenData (TokenData): Token data that has info about the token
            ignoreRelations (bool): Ignore relational checks if it is true, else throw an error if there is any enforced relational checks
        """

    @abstractmethod
    def deleteBuildingLevelRoom(
        self, obj: BuildingLevelRoom, tokenData: TokenData
    ) -> None:
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
    def buildingLevelRooms(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        buildingLevelId: str = None,
    ) -> dict:
        """Get list of building level rooms based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'id', 'direction': 'desc'}]
            buildingLevelId (str): A building level id of the building level rooms

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """

    @abstractmethod
    def buildingLevelRoomById(self, id: str, tokenData: TokenData = None) -> BuildingLevelRoom:
        """Get building level room by id

        Args:
            id (str): The id of the building level room
            tokenData (TokenData): A token data object

        Returns:
            BuildingLevelRoom: building level room object

        :raises:
            `BuildingLevelRoomDoesNotExistException <src.domain_model.resource.exception.BuildingLevelRoomDoesNotExistException>`
            Raise an exception if the building level room does not exist
        """
