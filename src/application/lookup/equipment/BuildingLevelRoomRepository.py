"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from abc import ABC, abstractmethod
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom


class BuildingLevelRoomRepository(ABC):
    @abstractmethod
    def save(self, obj: BuildingLevelRoom):
        """Save building level room

        Args:
            obj (BuildingLevelRoom): The building level room that needs to be saved

        """

    @abstractmethod
    def delete(self, obj: BuildingLevelRoom):
        """Delete building level room

        Args:
            obj (BuildingLevelRoom): The building level room that needs to be deleted

        """
