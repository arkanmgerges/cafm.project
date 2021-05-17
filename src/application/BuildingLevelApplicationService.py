"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.BuildingLevelRepository import (
    BuildingLevelRepository,
)
from src.domain_model.project.building.level.BuildingLevelService import (
    BuildingLevelService,
)
from src.domain_model.project.building.level.room.BuildingLevelRoom import (
    BuildingLevelRoom,
)
from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.resource.exception.UpdateBuildingLevelFailedException import (
    UpdateBuildingLevelFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.domain_model.util.DomainModelAttributeValidator import DomainModelAttributeValidator
from src.resource.logging.decorator import debugLogger


class BuildingLevelApplicationService:
    def __init__(
        self,
        repo: BuildingLevelRepository,
        buildingLevelService: BuildingLevelService,
        buildingRepo: BuildingRepository,
    ):
        self._repo = repo
        self._buildingRepo = buildingRepo
        self._buildingLevelService: BuildingLevelService = buildingLevelService

    @debugLogger
    def newId(self):
        return BuildingLevel.createFrom(skipValidation=True).id()

    @debugLogger
    def createBuildingLevel(
        self,
        id: str = None,
        name: str = "",
        isSubLevel: bool = False,
        buildingId: str = None,
        projectId: str = None,
        token: str = "",
        **_kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            buildingLevel: BuildingLevel = self._constructObject(
                id=id, name=name, isSubLevel=isSubLevel, buildingIds=[], rooms=[]
            )
            building: Building = self._buildingRepo.buildingById(
                id=buildingId, include=["buildingLevel", "buildingLevelRoom"]
            )
            if building.projectId() != projectId:
                from src.domain_model.resource.exception.InvalidArgumentException import (
                    InvalidArgumentException,
                )

                raise InvalidArgumentException(
                    f"Project id: {projectId} does not match project id of the building: {building.projectId()}"
                )
            self._buildingRepo.addLevelToBuilding(buildingLevel=buildingLevel, building=building, tokenData=tokenData)
            return buildingLevel
        except Exception as e:
            DomainPublishedEvents.cleanup()
            raise e

    @debugLogger
    def updateBuildingLevelRoomIndex(
        self,
        buildingLevelId: str = None,
        buildingLevelRoomId: str = None,
        index: int = None,
        **_kwargs,
    ):
        try:
            buildingLevel: BuildingLevel = self._repo.buildingLevelById(
                id=buildingLevelId, include=["buildingLevelRoom"]
            )
            buildingLevel.updateRoomIndex(roomId=buildingLevelRoomId, index=index)
            self._repo.save(buildingLevel)
        except Exception as e:
            DomainPublishedEvents.cleanup()
            raise e

    @debugLogger
    def updateBuildingLevel(self, id: str, name: str, isSubLevel: bool = False, token: str = "", **_kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: BuildingLevel = self._repo.buildingLevelById(id=id, include=["buildingLevelRoom"])
            obj: BuildingLevel = self._constructObject(
                id=id,
                name=name,
                isSubLevel=isSubLevel,
                buildingIds=oldObject.buildingIds(),
                rooms=oldObject.rooms(),
                _sourceObject=oldObject,
            )
            self._buildingLevelService.updateBuildingLevel(oldObject=oldObject, newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateBuildingLevelFailedException(message=str(e))

    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True), attributeDictionary=objListParamsItem
                )
                objList.append(
                    self._constructObject(
                        id=objListParamsItem["building_level_id"],
                        name=objListParamsItem["name"],
                        isSubLevel=objListParamsItem["is_sub_level"] if "is_sub_level" in objListParamsItem else False,
                        buildingIds=[],
                        rooms=[],
                    )
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._buildingLevelService.bulkCreate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True), attributeDictionary=objListParamsItem
                )
                objList.append(self._constructObject(id=objListParamsItem["building_level_id"], skipValidation=True))
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._buildingLevelService.bulkDelete(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True), attributeDictionary=objListParamsItem
                )
                oldObject: BuildingLevel = self._repo.buildingLevelById(
                    id=objListParamsItem["building_level_id"], include=[]
                )
                newObject = self._constructObject(
                    id=objListParamsItem["building_level_id"],
                    name=objListParamsItem["name"],
                    _sourceObject=oldObject,
                )
                objList.append(
                    (newObject, oldObject),
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._buildingLevelService.bulkUpdate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def linkBuildingLevelToBuilding(self, buildingLevelId, buildingId, token: str = "", **_kwargs):
        _tokenData = TokenService.tokenDataFromToken(token=token)
        buildingLevel: BuildingLevel = self._repo.buildingLevelById(id=buildingLevelId, include=["buildingLevelRoom"])
        buildingLevel.linkBuildingById(buildingId=buildingId)
        building: Building = self._buildingRepo.buildingById(id=buildingId, include=[])
        self._repo.linkBuildingLevelToBuilding(buildingLevel=buildingLevel, building=building)

    @debugLogger
    def unlinkBuildingLevelFromBuilding(self, buildingLevelId, buildingId, token: str = "", **_kwargs):
        _tokenData = TokenService.tokenDataFromToken(token=token)
        buildingLevel: BuildingLevel = self._repo.buildingLevelById(id=buildingLevelId, include=["buildingLevelRoom"])
        buildingLevel.unlinkBuildingById(buildingId=buildingId)
        building: Building = self._buildingRepo.buildingById(id=buildingId, include=[])
        self._repo.unlinkBuildingLevelFromBuilding(buildingLevel=buildingLevel, building=building)

    @debugLogger
    def deleteBuildingLevel(self, id: str, buildingId: str, token: str = "", **_kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        building: Building = self._buildingRepo.buildingById(
            id=buildingId, include=["buildingLevel", "buildingLevelRoom"]
        )
        buildingLevel: BuildingLevel = self._repo.buildingLevelById(id=id, include=["buildingLevelRoom"])
        if not buildingLevel.hasBuildingId(buildingId=buildingId):
            from src.domain_model.resource.exception.InvalidArgumentException import (
                InvalidArgumentException,
            )

            raise InvalidArgumentException(f"Building level does not have this building id: {buildingId}")
        self._buildingLevelService.removeBuildingLevelFromBuilding(
            buildingLevel=buildingLevel, building=building, tokenData=tokenData
        )

    @debugLogger
    def buildingLevels(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
        include: List[str] = None,
        buildingId: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._buildingLevelService.buildingLevels(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            include=include,
            buildingId=buildingId,
        )

    @debugLogger
    def buildingLevelById(self, id: str = "", include: List[str] = None, token: str = "") -> BuildingLevel:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._buildingLevelService.buildingLevelById(id=id, tokenData=tokenData, include=include)

    @debugLogger
    def _constructObject(
        self,
        id: str = None,
        name: str = "",
        isSubLevel: bool = False,
        buildingIds: List[str] = None,
        rooms: List[BuildingLevelRoom] = None,
        publishEvent: bool = False,
        _sourceObject: BuildingLevel = None,
        skipValidation: bool = False,
    ) -> BuildingLevel:
        if _sourceObject is not None:
            return BuildingLevel.createFrom(
                id=id,
                name=name if name is not None else _sourceObject.name(),
                isSubLevel=isSubLevel if isSubLevel is not None else _sourceObject.isSubLevel(),
                buildingIds=buildingIds if buildingIds is not None else _sourceObject.buildingIds(),
                rooms=rooms if rooms is not None else _sourceObject.rooms(),
                publishEvent=publishEvent,
                skipValidation=skipValidation,
            )
        else:
            return BuildingLevel.createFrom(
                id=id,
                name=name,
                isSubLevel=isSubLevel,
                buildingIds=buildingIds,
                rooms=rooms,
                publishEvent=publishEvent,
                skipValidation=skipValidation,
            )
