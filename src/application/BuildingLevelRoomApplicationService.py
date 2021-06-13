"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.lifecycle.decorator.readOnly import readOnly
from src.application.lifecycle.decorator.transactional import transactional
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
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
from src.domain_model.project.building.level.room.BuildingLevelRoomService import (
    BuildingLevelRoomService,
)
from src.domain_model.resource.exception.ArgumentNotFoundException import ArgumentNotFoundException
from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.resource.exception.UpdateBuildingLevelFailedException import (
    UpdateBuildingLevelFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.domain_model.util.DomainModelAttributeValidator import DomainModelAttributeValidator
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger


class BuildingLevelRoomApplicationService:
    def __init__(
        self,
        repo: BuildingLevelRoomRepository,
        buildingLevelRoomService: BuildingLevelRoomService,
        buildingLevelRepository: BuildingLevelRepository,
    ):
        self._repo = repo
        self._buildingLevelRepo = buildingLevelRepository
        self._buildingLevelRoomService: BuildingLevelRoomService = buildingLevelRoomService

    @debugLogger
    def newId(self):
        return BuildingLevelRoom.createFrom(skipValidation=True).id()

    @transactional
    @debugLogger
    def createBuildingLevelRoom(
        self,
        id: str = None,
        name: str = "",
        description: str = None,
        buildingLevelId: str = None,
        token: str = "",
        **_kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            buildingLevel: BuildingLevel = self._buildingLevelRepo.buildingLevelById(
                id=buildingLevelId, include=["buildingLevelRoom"]
            )
            room = BuildingLevelRoom.createFrom(
                id=id,
                name=name,
                description=description,
                buildingLevelId=buildingLevelId,
            )
            self._buildingLevelRoomService.addRoomToLevel(room=room, level=buildingLevel, tokenData=tokenData)
            return room
        except Exception as e:
            DomainPublishedEvents.cleanup()
            raise e

    @transactional
    @debugLogger
    def updateBuildingLevelRoom(self, id: str, name: str, description: str = "", token: str = "", **_kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: BuildingLevelRoom = self._repo.buildingLevelRoomById(id=id)
            obj: BuildingLevelRoom = self._constructObject(
                id=id,
                name=name,
                description=description,
                buildingLevelId=oldObject.buildingLevelId(),
                _sourceObject=oldObject,
            )
            self._buildingLevelRoomService.updateBuildingLevelRoom(
                oldObject=oldObject, newObject=obj, tokenData=tokenData
            )
        except Exception as e:
            raise UpdateBuildingLevelFailedException(message=str(e))

    @transactional
    @debugLogger
    def deleteBuildingLevelRoom(self, id: str, buildingLevelId: str, token: str = "", **_kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        level: BuildingLevel = self._buildingLevelRepo.buildingLevelById(
            id=buildingLevelId, include=["buildingLevelRoom"]
        )
        room: BuildingLevelRoom = self._repo.buildingLevelRoomById(id=id)
        if not level.hasRoom(roomId=id):
            from src.domain_model.resource.exception.BuildingLevelDoesNotHaveRoomException import (
                BuildingLevelDoesNotHaveRoomException,
            )

            raise BuildingLevelDoesNotHaveRoomException(f"building level: {level}, room: {room}")
        self._buildingLevelRoomService.removeRoomFromLevel(room=room, level=level, tokenData=tokenData)

    @transactional
    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = ""):
        objList = []
        objLevelDict = {}
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True), attributeDictionary=objListParamsItem
                )
                objList.append(
                    self._constructObject(
                        id=objListParamsItem["building_level_room_id"],
                        name=objListParamsItem["name"],
                        description=objListParamsItem["description"],
                        buildingLevelId=objListParamsItem["building_level_id"],
                    )
                )
                if objListParamsItem["building_level_id"] not in objLevelDict:
                    buildingLevel: BuildingLevel = self._buildingLevelRepo.buildingLevelById(
                        id=objListParamsItem["building_level_id"], include=["buildingLevelRoom"]
                    )
                    objLevelDict[objListParamsItem["building_level_id"]] = buildingLevel
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._buildingLevelRoomService.bulkCreate(objList=objList, objLevelDict=objLevelDict)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @transactional
    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = ""):
        objList = []
        objLevelDict = {}
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True), attributeDictionary=objListParamsItem
                )
                objList.append(
                    self._constructObject(id=objListParamsItem["building_level_room_id"], skipValidation=True)
                )
                if "building_level_id" not in objListParamsItem:
                    raise ArgumentNotFoundException(
                        message=f'building_level_id not found for room id: {objListParamsItem["building_level_room_id"]}'
                    )
                if objListParamsItem["building_level_id"] not in objLevelDict:
                    buildingLevel: BuildingLevel = self._buildingLevelRepo.buildingLevelById(
                        id=objListParamsItem["building_level_id"], include=["buildingLevelRoom"]
                    )
                    objLevelDict[objListParamsItem["building_level_id"]] = buildingLevel
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._buildingLevelRoomService.bulkDelete(objList=objList, objLevelDict=objLevelDict)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @transactional
    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True), attributeDictionary=objListParamsItem
                )
                oldObject: BuildingLevelRoom = self._repo.buildingLevelRoomById(
                    id=objListParamsItem["building_level_room_id"]
                )
                newObject = self._constructObject(
                    id=objListParamsItem["building_level_room_id"],
                    buildingLevelId=oldObject.buildingLevelId(),
                    _sourceObject=oldObject,
                    **{Util.snakeCaseToLowerCameCaseString(k): v for k, v in objListParamsItem.items()}
                )
                objList.append(
                    (newObject, oldObject),
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._buildingLevelRoomService.bulkUpdate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @transactional
    @debugLogger
    def deleteBuildingLevelRoomsByBuildingLevelId(self, buildingLevelId: str, token: str = "", **_kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        result: List[BuildingLevelRoom] = self._repo.buildingLevelRoomsByBuildingLevelId(buildingLevelId=buildingLevelId, resultSize=1000000)
        if len(result) > 0:
            for buildingLevelRoom in result:
                self._buildingLevelRoomService.removeBuildingLevelRoom(obj=buildingLevelRoom, tokenData=tokenData, ignoreRelations=True)

    @readOnly
    @debugLogger
    def buildingLevelRooms(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
        buildingLevelId: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._repo.buildingLevelRooms(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            buildingLevelId=buildingLevelId,
        )

    @readOnly
    @debugLogger
    def buildingLevelRoomById(self, id: str = "", token: str = "", **_kwargs) -> BuildingLevelRoom:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._repo.buildingLevelRoomById(id=id, tokenData=tokenData)

    @debugLogger
    def _constructObject(
        self,
        id: str = None,
        name: str = None,
        buildingLevelId: str = None,
        description: str = None,
        publishEvent: bool = False,
        _sourceObject: BuildingLevelRoom = None,
        skipValidation: bool = False,
        **_kwargs
    ) -> BuildingLevelRoom:
        if _sourceObject is not None:
            return BuildingLevelRoom.createFrom(
                id=id,
                name=name if name is not None else _sourceObject.name(),
                buildingLevelId=buildingLevelId if buildingLevelId is not None else _sourceObject.buildingLevelId(),
                description=description if description is not None else _sourceObject.description(),
                publishEvent=publishEvent,
                skipValidation=skipValidation,
            )
        else:
            return BuildingLevelRoom.createFrom(
                id=id,
                name=name,
                buildingLevelId=buildingLevelId,
                description=description,
                publishEvent=publishEvent,
                skipValidation=skipValidation,
            )
