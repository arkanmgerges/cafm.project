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
from src.domain_model.resource.exception.BuildingLevelAlreadyExistException import (
    BuildingLevelAlreadyExistException,
)
from src.domain_model.resource.exception.BuildingLevelDoesNotExistException import (
    BuildingLevelDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger


class BuildingLevelService:
    def __init__(
        self,
        buildingLevelRepo: BuildingLevelRepository,
        buildingRepo: BuildingRepository,
    ):
        self._repo = buildingLevelRepo
        self._buildingRepo = buildingRepo

    @debugLogger
    def createBuildingLevel(
        self, obj: BuildingLevel, objectOnly: bool = False, tokenData: TokenData = None
    ):
        if objectOnly:
            return (
                BuildingLevel.createFromObject(obj=obj, generateNewId=True)
                if obj.id() is None
                else obj
            )
        else:
            obj = BuildingLevel.createFromObject(obj=obj, publishEvent=True)
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def bulkCreate(self, objList: List[dict]):
        self._repo.bulkSave(objList=objList)
        for obj in objList:
            BuildingLevel.createFromObject(obj=obj['buildingLevel'], publishEvent=True)

    @debugLogger
    def bulkDelete(self, objList: List[BuildingLevel]):
        self._repo.bulkDelete(objList=objList)
        for obj in objList:
            obj.publishDelete()

    @debugLogger
    def bulkUpdate(self, objList: List[Tuple]):
        newObjList = list(map(lambda x: {'buildingLevel': x[0]}, objList))
        self._repo.bulkSave(objList=newObjList)
        for obj in objList:
            newObj = obj[0]
            oldObj = obj[1]
            newObj.publishUpdate(oldObj)

    @debugLogger
    def addLevelToBuilding(
        self,
        buildingLevel: BuildingLevel,
        building: Building,
        tokenData: TokenData = None,
    ):
        building.addLevel(buildingLevel)
        self._buildingRepo.addLevelToBuilding(
            buildingLevel=buildingLevel, building=building
        )

    @debugLogger
    def updateBuildingLevel(
        self,
        oldObject: BuildingLevel,
        newObject: BuildingLevel,
        tokenData: TokenData = None,
    ):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def removeBuildingLevelFromBuilding(
        self,
        buildingLevel: BuildingLevel,
        building: Building,
        tokenData: TokenData = None,
    ):
        building.removeLevel(level=buildingLevel)
        self._buildingRepo.removeLevelFromBuilding(
            buildingLevel=buildingLevel, building=building
        )

    @debugLogger
    def removeBuildingLevel(self, obj: BuildingLevel, tokenData: TokenData = None, ignoreRelations: bool = False):
        obj.publishDelete()
        self._repo.removeBuildingLevel(buildingLevel=obj, tokenData=tokenData, ignoreRelations=ignoreRelations)

    @debugLogger
    def buildingLevels(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        include: List[str] = None,
        buildingId: str = None,
    ):
        include = [] if include is None else include
        # Convert to camel case
        result = include
        include = []
        for x in result:
            include.append(Util.snakeCaseToLowerCameCaseString(x))
        return self._repo.buildingLevels(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            include=include,
            buildingId=buildingId,
        )

    @debugLogger
    def buildingLevelById(
        self, id: str = None, include: List[str] = None, tokenData: TokenData = None
    ):
        include = [] if include is None else include
        # Convert to camel case
        result = include
        include = []
        for x in result:
            include.append(Util.snakeCaseToLowerCameCaseString(x))
        return self._repo.buildingLevelById(id=id, include=include, tokenData=tokenData)
