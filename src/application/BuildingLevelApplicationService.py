"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.BuildingLevelRepository import BuildingLevelRepository
from src.domain_model.project.building.level.BuildingLevelService import BuildingLevelService
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.domain_model.resource.exception.UpdateBuildingLevelFailedException import UpdateBuildingLevelFailedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class BuildingLevelApplicationService:
    def __init__(self, repo: BuildingLevelRepository, buildingLevelService: BuildingLevelService,
                 buildingRepo: BuildingRepository):
        self._repo = repo
        self._buildingRepo = buildingRepo
        self._buildingLevelService: BuildingLevelService = buildingLevelService

    @debugLogger
    def createBuildingLevel(self, id: str = None, name: str = '', buildingId: str = None, projectId: str = None,
                            objectOnly: bool = False, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            obj: BuildingLevel = self.constructObject(id=id, name=name, buildingIds=[], rooms=[])
            obj2: Building = self._buildingRepo.buildingById(id=buildingId)
            if obj2.projectId() != projectId:
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Project id: {projectId} does not match project id of the building: {obj2.projectId()}')
            self._buildingLevelService.addLevelToBuilding(obj=obj, obj2=obj2, tokenData=tokenData)
        except Exception as e:
            DomainPublishedEvents.cleanup()
            raise e

    @debugLogger
    def updateBuildingLevel(self, id: str, name: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: BuildingLevel = self._repo.buildingLevelById(id=id)
            obj: BuildingLevel = self.constructObject(id=id, name=name, buildingIds=oldObject.buildingIds(),
                                                      rooms=oldObject.rooms())
            self._buildingLevelService.updateBuildingLevel(oldObject=oldObject,
                                                           newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateBuildingLevelFailedException(message=str(e))

    @debugLogger
    def deleteBuildingLevel(self, id: str, buildingId: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj: BuildingLevel = self._repo.buildingLevelById(id=id)
        if not obj.hasBuildingId(buildingId=buildingId):
            from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
            raise InvalidArgumentException(f'Building level does not have this building id: {buildingId}')
        self._buildingLevelService.deleteBuildingLevel(obj=obj, tokenData=tokenData)

    @debugLogger
    def constructObject(self, id: str = None, name: str = '', buildingIds: List[str] = None,
                        rooms: List[BuildingLevelRoom] = None, publishEvent: bool = False) -> BuildingLevel:
        return BuildingLevel.createFrom(id=id, name=name, buildingIds=buildingIds, rooms=rooms,
                                        publishEvent=publishEvent)
