"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.project.building.BuildingService import BuildingService
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.resource.exception.UpdateBuildingFailedException import UpdateBuildingFailedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class BuildingApplicationService:
    def __init__(self, repo: BuildingRepository, buildingService: BuildingService):
        self._repo = repo
        self._buildingService = buildingService

    @debugLogger
    def createBuilding(self, id: str = None, name: str = '', projectId: str = None, levels: List[BuildingLevel] = None,
                       objectOnly: bool = False, token: str = ''):
        obj: Building = self.constructObject(id=id, name=name, projectId=projectId, levels=levels)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._buildingService.createBuilding(obj=obj,
                                                    objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateBuilding(self, id: str, name: str, projectId: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Building = self._repo.buildingById(id=id)
            obj: Building = self.constructObject(id=id, name=name, projectId=projectId, levels=oldObject.levels())
            self._buildingService.updateBuilding(oldObject=oldObject,
                                                 newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateBuildingFailedException(message=str(e))

    @debugLogger
    def deleteBuilding(self, id: str, projectId: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj: Building = self._repo.buildingById(id=id)
        if obj.projectId() != projectId:
            from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
            raise InvalidArgumentException(
                f'Project id: {projectId} does not match project id of the building: {obj.projectId()}')
        self._buildingService.deleteBuilding(obj=obj, tokenData=tokenData)

    @debugLogger
    def constructObject(self, id: str = None, name: str = '', projectId: str = None,
                        levels: List[BuildingLevel] = None) -> Building:
        return Building.createFrom(id=id, name=name, projectId=projectId, buildingLevels=levels)
