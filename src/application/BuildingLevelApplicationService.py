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
    def newId(self):
        return BuildingLevel.createFrom(skipValidation=True).id()

    @debugLogger
    def createBuildingLevel(self, id: str = None, name: str = '', buildingId: str = None, projectId: str = None,
                            objectOnly: bool = False, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            buildingLevel: BuildingLevel = self.constructObject(id=id, name=name, buildingIds=[], rooms=[])
            building: Building = self._buildingRepo.buildingById(id=buildingId,
                                                                 include=['buildingLevel', 'buildingLevelRoom'])
            if building.projectId() != projectId:
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Project id: {projectId} does not match project id of the building: {building.projectId()}')
            self._buildingRepo.addLevelToBuilding(buildingLevel=buildingLevel, building=building,
                                                          tokenData=tokenData)
            return buildingLevel
        except Exception as e:
            DomainPublishedEvents.cleanup()
            raise e

    @debugLogger
    def updateBuildingLevelRoomIndex(self, buildingLevelId: str = None,
                                     buildingLevelRoomId: str = None,
                                     index: int = None,
                                     token: str = ''):
        try:
            buildingLevel: BuildingLevel = self._repo.buildingLevelById(id=buildingLevelId,
                                                                        include=['buildingLevelRoom'])
            buildingLevel.updateRoomIndex(roomId=buildingLevelRoomId, index=index)
        except Exception as e:
            DomainPublishedEvents.cleanup()
            raise e

    @debugLogger
    def updateBuildingLevel(self, id: str, name: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: BuildingLevel = self._repo.buildingLevelById(id=id, include=['buildingLevelRoom'])
            obj: BuildingLevel = self.constructObject(id=id, name=name, buildingIds=oldObject.buildingIds(),
                                                      rooms=oldObject.rooms())
            self._buildingLevelService.updateBuildingLevel(oldObject=oldObject,
                                                           newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateBuildingLevelFailedException(message=str(e))

    @debugLogger
    def linkBuildingLevelToBuilding(self, buildingLevelId, buildingId, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        buildingLevel: BuildingLevel = self._repo.buildingLevelById(id=buildingLevelId, include=['buildingLevelRoom'])
        buildingLevel.linkBuildingById(buildingId=buildingId)

    @debugLogger
    def unlinkBuildingLevelFromBuilding(self, buildingLevelId, buildingId, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        buildingLevel: BuildingLevel = self._repo.buildingLevelById(id=buildingLevelId, include=['buildingLevelRoom'])
        buildingLevel.unlinkBuildingById(buildingId=buildingId)

    @debugLogger
    def deleteBuildingLevel(self, id: str, buildingId: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        building: Building = self._buildingRepo.buildingById(id=buildingId,
                                                             include=['buildingLevel', 'buildingLevelRoom'])
        buildingLevel: BuildingLevel = self._repo.buildingLevelById(id=id, include=['buildingLevelRoom'])
        if not buildingLevel.hasBuildingId(buildingId=buildingId):
            from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
            raise InvalidArgumentException(f'Building level does not have this building id: {buildingId}')
        self._buildingLevelService.removeBuildingLevelFromBuilding(buildingLevel=buildingLevel, building=building,
                                                                   tokenData=tokenData)

    @debugLogger
    def buildingLevels(self, resultFrom: int = 0, resultSize: int = 100, token: str = '',
                       order: List[dict] = None, include: List[str] = None, buildingId: str = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._buildingLevelService.buildingLevels(tokenData=tokenData,
                                                         resultFrom=resultFrom,
                                                         resultSize=resultSize,
                                                         order=order,
                                                         include=include,
                                                         buildingId=buildingId)

    @debugLogger
    def buildingLevelById(self, id: str = '', include: List[str] = None, token: str = '') -> BuildingLevel:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._buildingLevelService.buildingLevelById(id=id,
                                                            tokenData=tokenData,
                                                            include=include)

    @debugLogger
    def constructObject(self, id: str = None, name: str = '', buildingIds: List[str] = None,
                        rooms: List[BuildingLevelRoom] = None, publishEvent: bool = False) -> BuildingLevel:
        return BuildingLevel.createFrom(id=id, name=name, buildingIds=buildingIds, rooms=rooms,
                                        publishEvent=publishEvent)
