"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.BuildingLevelRepository import BuildingLevelRepository
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.domain_model.project.building.level.room.BuildingLevelRoomRepository import BuildingLevelRoomRepository
from src.domain_model.resource.exception.BuildingLevelAlreadyExistException import BuildingLevelAlreadyExistException
from src.domain_model.resource.exception.BuildingLevelDoesNotExistException import BuildingLevelDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class BuildingLevelRoomService:
    def __init__(self, buildingLevelRoomRepo: BuildingLevelRoomRepository, buildingLevelRepo: BuildingLevelRepository):
        self._repo = buildingLevelRoomRepo
        self._buildingLevelRepo = buildingLevelRepo

    @debugLogger
    def createBuildingLevel(self, obj: BuildingLevelRoom, objectOnly: bool = False, tokenData: TokenData = None):
        if objectOnly:
            return BuildingLevelRoom.createFromObject(obj=obj, generateNewId=True) if obj.id() is None else obj
        else:
            obj = BuildingLevelRoom.createFromObject(obj=obj, publishEvent=True)
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def updateBuildingLevelRoom(self, oldObject: BuildingLevelRoom, newObject: BuildingLevelRoom, tokenData: TokenData = None):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def addRoomToLevel(self, room: BuildingLevelRoom, level: BuildingLevel, tokenData):
        level.addRoom(room=room)
        self._buildingLevelRepo.addBuildingLevelRoomToBuildingLevel(buildingLevelRoom=room, buildingLevel=level)

    @debugLogger
    def removeRoomFromLevel(self, room: BuildingLevelRoom, level: BuildingLevel, tokenData):
        level.removeRoom(room=room)
        self._buildingLevelRepo.removeBuildingLevelRoomFromBuildingLevel(buildingLevelRoom=room, buildingLevel=level)


    # @debugLogger
    # def buildingLevels(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
    #              order: List[dict] = None):
    #     return self._repo.buildingLevels(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)

