"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.token.TokenData import TokenData


class BuildingRepository(ABC):
    @abstractmethod
    def addLevelToBuilding(
        self, buildingLevel: BuildingLevel, building: Building, tokenData: TokenData
    ):
        """Add building level to building

        Args:
            buildingLevel (BuildingLevel): The building level that needs to be added to the building
            building (Building): The building that will contain the building level
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def removeLevelFromBuilding(
        self, buildingLevel: BuildingLevel, building: Building, tokenData: TokenData
    ):
        """Remove building level from building

        Args:
            buildingLevel (BuildingLevel): The building level that needs to be removed from the building
            building (Building): The building that contains the building level
            tokenData (TokenData): Token data that has info about the token
        """

    @abstractmethod
    def save(self, obj: Building, tokenData: TokenData):
        """Save building

        Args:
            obj (Building): The building that needs to be saved
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
    def buildings(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        include: List[str] = None,
        projectId: str = None,
    ) -> dict:
        """Get list of buildings based on the owned roles that the user has

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'age', 'direction': 'desc'}]
            include (List[str]): A list of string that is used to include inner data
            projectId (str): A project id of the buildings

        Returns:
            dict: A dict that has {"items": [], "itemCount": 0}
        """

    @abstractmethod
    def buildingById(
        self, id: str, include: List[str], tokenData: TokenData
    ) -> Building:
        """Get building by id

        Args:
            id (str): The id of the building
            include (List[str]): A list of string that is used to include inner data
            tokenData (TokenData): A token data object

        Returns:
            Building: building object

        :raises:
            `BuildingDoesNotExistException <src.domain_model.resource.exception.BuildingDoesNotExistException>`
            Raise an exception if the building does not exist
        """
