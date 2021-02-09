"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.BuildingLevelRepository import BuildingLevelRepository
from src.domain_model.resource.exception.BuildingLevelAlreadyExistException import BuildingLevelAlreadyExistException
from src.domain_model.resource.exception.BuildingLevelDoesNotExistException import BuildingLevelDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class BuildingLevelService:
    def __init__(self, buildingLevelRepo: BuildingLevelRepository, buildingRepo: BuildingRepository):
        self._repo = buildingLevelRepo
        self._buildingRepo = buildingRepo

    @debugLogger
    def createBuildingLevel(self, obj: BuildingLevel, objectOnly: bool = False, tokenData: TokenData = None):
        try:
            if obj.id() == '':
                raise BuildingLevelDoesNotExistException()
            self._repo.buildingLevelById(id=obj.id())
            raise BuildingLevelAlreadyExistException(obj.name())
        except BuildingLevelDoesNotExistException:
            if objectOnly:
                return BuildingLevel.createFromObject(obj=obj, generateNewId=True) if obj.id() is None else obj
            else:
                obj = BuildingLevel.createFromObject(obj=obj, publishEvent=True)
                return obj

    @debugLogger
    def addLevelToBuilding(self, buildingLevel: BuildingLevel, building: Building, tokenData: TokenData = None):
        building.addLevel(buildingLevel)

    @debugLogger
    def updateBuildingLevel(self, oldObject: BuildingLevel, newObject: BuildingLevel, tokenData: TokenData = None):
        if oldObject == newObject:
            from src.domain_model.resource.exception.ObjectIdenticalException import ObjectIdenticalException
            raise ObjectIdenticalException(f'oldObject: {oldObject}, newObject: {newObject}')
        newObject.publishUpdate(oldObject)

    @debugLogger
    def removeBuildingLevelFromBuilding(self, buildingLevel: BuildingLevel, building: Building, tokenData: TokenData = None):
        building.removeLevel(level=buildingLevel)


    # @debugLogger
    # def buildingLevels(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
    #              order: List[dict] = None):
    #     return self._repo.buildingLevels(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
