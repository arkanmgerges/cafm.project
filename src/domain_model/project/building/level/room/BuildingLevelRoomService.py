"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, Tuple

from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.BuildingLevelRepository import (
    BuildingLevelRepository,
)
from src.domain_model.project.building.level.room.BuildingLevelRoom import (
    BuildingLevelRoom,
)
from src.domain_model.project.building.level.room.BuildingLevelRoomRepository import (
    BuildingLevelRoomRepository,
)
from src.domain_model.resource.exception.BuildingLevelAlreadyExistException import (
    BuildingLevelAlreadyExistException,
)
from src.domain_model.resource.exception.BuildingLevelDoesNotExistException import (
    BuildingLevelDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class BuildingLevelRoomService:
    def __init__(
        self,
        buildingLevelRoomRepo: BuildingLevelRoomRepository,
        buildingLevelRepo: BuildingLevelRepository,
    ):
        self._repo = buildingLevelRoomRepo
        self._buildingLevelRepo = buildingLevelRepo

    @debugLogger
    def updateBuildingLevelRoom(
        self,
        oldObject: BuildingLevelRoom,
        newObject: BuildingLevelRoom,
        tokenData: TokenData = None,
    ):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def bulkCreate(self, objList: List[BuildingLevelRoom], objLevelDict: dict):
        for obj in objList:
            level = objLevelDict[obj.buildingLevelId()]
            level.addRoom(room=obj)

        self._buildingLevelRepo.bulkSave(objList=list(objLevelDict.values()))
        self._repo.bulkSave(objList=objList)

    @debugLogger
    def bulkDelete(self, objList: List[BuildingLevelRoom], objLevelDict: dict):
        for obj in objList:
            level = objLevelDict[obj.buildingLevelId()]
            level.removeRoom(room=obj)

        self._buildingLevelRepo.bulkSave(objList=list(objLevelDict.values()))
        self._repo.bulkDelete(objList=objList)

    @debugLogger
    def bulkUpdate(self, objList: List[Tuple]):
        newObjList = list(map(lambda x: x[0], objList))
        self._repo.bulkSave(objList=newObjList)
        for obj in objList:
            newObj = obj[0]
            oldObj = obj[1]
            newObj.publishUpdate(oldObj)

    @debugLogger
    def addRoomToLevel(self, room: BuildingLevelRoom, level: BuildingLevel, tokenData):
        level.addRoom(room=room)
        self._buildingLevelRepo.addBuildingLevelRoomToBuildingLevel(
            buildingLevelRoom=room, buildingLevel=level
        )

    @debugLogger
    def removeRoomFromLevel(
        self, room: BuildingLevelRoom, level: BuildingLevel, tokenData
    ):
        level.removeRoom(room=room)
        self._buildingLevelRepo.removeBuildingLevelRoomFromBuildingLevel(
            buildingLevelRoom=room, buildingLevel=level
        )

    # @debugLogger
    # def buildingLevels(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
    #              order: List[dict] = None):
    #     return self._repo.buildingLevels(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
