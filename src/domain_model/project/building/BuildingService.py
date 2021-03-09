"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.resource.exception.BuildingAlreadyExistException import BuildingAlreadyExistException
from src.domain_model.resource.exception.BuildingDoesNotExistException import BuildingDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger


class BuildingService:
    def __init__(self, buildingRepo: BuildingRepository):
        self._repo = buildingRepo

    @debugLogger
    def createBuilding(self, obj: Building, objectOnly: bool = False, tokenData: TokenData = None):
        if objectOnly:
            return Building.createFromObject(obj=obj, generateNewId=True) if obj.id() == '' else obj
        else:
            obj = Building.createFromObject(obj=obj, publishEvent=True)
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def deleteBuilding(self, obj: Building, tokenData: TokenData = None):
        obj.publishDelete()
        self._repo.deleteBuilding(obj=obj)

    @debugLogger
    def updateBuilding(self, oldObject: Building, newObject: Building, tokenData: TokenData = None):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def buildings(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
                  order: List[dict] = None, include: List[str] = None, projectId: str = None):
        include = [] if include is None else include
        # Convert to camel case
        result = include
        include = []
        for x in result:
            include.append(Util.snakeCaseToLowerCameCaseString(x))
        return self._repo.buildings(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order,
                                    include=include, projectId=projectId)

    @debugLogger
    def buildingById(self, id: str = None, include: List[str] = None, tokenData: TokenData = None):
        include = [] if include is None else include
        # Convert to camel case
        result = include
        include = []
        for x in result:
            include.append(Util.snakeCaseToLowerCameCaseString(x))
        return self._repo.buildingById(id=id, include=include, tokenData=tokenData)
