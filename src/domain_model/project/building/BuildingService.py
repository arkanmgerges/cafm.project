"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.resource.exception.BuildingAlreadyExistException import BuildingAlreadyExistException
from src.domain_model.resource.exception.BuildingDoesNotExistException import BuildingDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class BuildingService:
    def __init__(self, buildingRepo: BuildingRepository):
        self._repo = buildingRepo

    @debugLogger
    def createBuilding(self, obj: Building, objectOnly: bool = False, tokenData: TokenData = None):
        try:
            if obj.id() == '':
                raise BuildingDoesNotExistException()
            self._repo.buildingById(id=obj.id())
            raise BuildingAlreadyExistException(obj.name())
        except BuildingDoesNotExistException:
            if objectOnly:
                return Building.createFromObject(obj=obj, generateNewId=True) if obj.id() == '' else obj
            else:
                obj = Building.createFromObject(obj=obj, publishEvent=True)
                self._repo.createBuilding(obj=obj, tokenData=tokenData)
                return obj

    @debugLogger
    def deleteBuilding(self, obj: Building, tokenData: TokenData = None):
        self._repo.deleteBuilding(obj=obj, tokenData=tokenData)
        obj.publishDelete()


    # @debugLogger
    # def buildings(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
    #              order: List[dict] = None):
    #     return self._repo.buildings(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
