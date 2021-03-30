"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.BuildingLevelRepository import BuildingLevelRepository
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.domain_model.project.building.level.room.BuildingLevelRoomRepository import BuildingLevelRoomRepository
from src.domain_model.project.building.level.room.BuildingLevelRoomService import BuildingLevelRoomService
from src.domain_model.resource.exception.UpdateBuildingLevelFailedException import UpdateBuildingLevelFailedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class BuildingLevelRoomApplicationService:
    def __init__(self, repo: BuildingLevelRoomRepository, buildingLevelRoomService: BuildingLevelRoomService,
                 buildingLevelRepository: BuildingLevelRepository):
        self._repo = repo
        self._buildingLevelRepo = buildingLevelRepository
        self._buildingLevelRoomService: BuildingLevelRoomService = buildingLevelRoomService

    @debugLogger
    def newId(self):
        return BuildingLevelRoom.createFrom(skipValidation=True).id()

    @debugLogger
    def createBuildingLevelRoom(self, id: str = None, name: str = '', description: str = None,
                                buildingLevelId: str = None, objectOnly: bool = False, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            buildingLevel: BuildingLevel = self._buildingLevelRepo.buildingLevelById(id=buildingLevelId, include=['buildingLevelRoom'])
            room = BuildingLevelRoom.createFrom(id=id, name=name, description=description,
                                                buildingLevelId=buildingLevelId)
            self._buildingLevelRoomService.addRoomToLevel(room=room, level=buildingLevel, tokenData=tokenData)
            return room
        except Exception as e:
            DomainPublishedEvents.cleanup()
            raise e

    @debugLogger
    def updateBuildingLevelRoom(self, id: str, name: str, description: str = '', token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: BuildingLevelRoom = self._repo.buildingLevelRoomById(id=id)
            obj: BuildingLevelRoom = self.constructObject(id=id, name=name, description=description,
                                                          buildingLevelId=oldObject.buildingLevelId(), _sourceObject=oldObject)
            self._buildingLevelRoomService.updateBuildingLevelRoom(oldObject=oldObject,
                                                                   newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateBuildingLevelFailedException(message=str(e))

    @debugLogger
    def deleteBuildingLevelRoom(self, id: str, buildingLevelId: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        level: BuildingLevel = self._buildingLevelRepo.buildingLevelById(id=buildingLevelId, include=['buildingLevelRoom'])
        room: BuildingLevelRoom = self._repo.buildingLevelRoomById(id=id)
        if not level.hasRoom(roomId=id):
            from src.domain_model.resource.exception.BuildingLevelDoesNotHaveRoomException import \
                BuildingLevelDoesNotHaveRoomException
            raise BuildingLevelDoesNotHaveRoomException(f'building level: {level}, room: {room}')
        self._buildingLevelRoomService.removeRoomFromLevel(room=room, level=level, tokenData=tokenData)

    @debugLogger
    def buildingLevelRooms(self, resultFrom: int = 0, resultSize: int = 100, token: str = '',
                           order: List[dict] = None, buildingLevelId: str = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._repo.buildingLevelRooms(tokenData=tokenData,
                                             resultFrom=resultFrom,
                                             resultSize=resultSize,
                                             order=order,
                                             buildingLevelId=buildingLevelId)

    @debugLogger
    def buildingLevelRoomById(self, id: str = '', token: str = '') -> BuildingLevelRoom:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._repo.buildingLevelRoomById(id=id, tokenData=tokenData)

    @debugLogger
    def constructObject(self, id: str = None, name: str = '', buildingLevelId: str = None,
                        description: str = '', publishEvent: bool = False, _sourceObject: BuildingLevelRoom = None) -> BuildingLevelRoom:
        if _sourceObject is not None:
            return BuildingLevelRoom.createFrom(id=id,
                                                name=name if name is not None else _sourceObject.name(),
                                                buildingLevelId=buildingLevelId if buildingLevelId is not None else _sourceObject.buildingLevelId(),
                                                description=description if description is not None else _sourceObject.description(),
                                                publishEvent=publishEvent)
        else:
            return BuildingLevelRoom.createFrom(id=id, name=name, buildingLevelId=buildingLevelId,
                                            description=description, publishEvent=publishEvent)
