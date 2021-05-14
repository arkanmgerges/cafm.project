"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.project.building.BuildingService import BuildingService
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.resource.exception.UpdateBuildingFailedException import (
    UpdateBuildingFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.domain_model.util.DomainModelAttributeValidator import DomainModelAttributeValidator
from src.resource.logging.decorator import debugLogger


class BuildingApplicationService:
    def __init__(self, repo: BuildingRepository, buildingService: BuildingService):
        self._repo = repo
        self._buildingService = buildingService

    @debugLogger
    def newId(self):
        return Building.createFrom(skipValidation=True).id()

    @debugLogger
    def createBuilding(
        self,
        id: str = None,
        name: str = "",
        projectId: str = None,
        levels: List[BuildingLevel] = None,
        objectOnly: bool = False,
        token: str = "",
    ):
        obj: Building = self._constructObject(id=id, name=name, projectId=projectId, levels=levels)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._buildingService.createBuilding(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateBuilding(self, id: str, name: str, projectId: str, token: str = ""):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Building = self._repo.buildingById(id=id, include=["buildingLevel", "buildingLevelRoom"])
            obj: Building = self._constructObject(
                id=id,
                name=name,
                projectId=projectId,
                levels=oldObject.levels(),
                _sourceObject=oldObject,
            )
            self._buildingService.updateBuilding(oldObject=oldObject, newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateBuildingFailedException(message=str(e))

    @debugLogger
    def deleteBuilding(self, id: str, projectId: str, token: str = ""):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj: Building = self._repo.buildingById(id=id, include=["buildingLevel", "buildingLevelRoom"])
        if obj.projectId() != projectId:
            from src.domain_model.resource.exception.InvalidArgumentException import (
                InvalidArgumentException,
            )

            raise InvalidArgumentException(
                f"Project id: {projectId} does not match project id of the building: {obj.projectId()}"
            )
        self._buildingService.deleteBuilding(obj=obj, tokenData=tokenData)

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
                        id=objListParamsItem["building_id"],
                        name=objListParamsItem["name"],
                        projectId=objListParamsItem["project_id"],
                    )
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._buildingService.bulkCreate(objList=objList)
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
                objList.append(self._constructObject(id=objListParamsItem["building_id"], skipValidation=True))
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._buildingService.bulkDelete(objList=objList)
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
                oldObject: Building = self._repo.buildingById(id=objListParamsItem["building_id"], include=[])
                newObject = self._constructObject(
                    id=objListParamsItem["building_id"],
                    name=objListParamsItem["name"],
                    projectId=objListParamsItem["project_id"],
                    _sourceObject=oldObject,
                )
                objList.append(
                    (newObject, oldObject),
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._buildingService.bulkUpdate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def buildings(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
        include: List[str] = None,
        projectId: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._buildingService.buildings(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            include=include,
            projectId=projectId,
        )

    @debugLogger
    def buildingById(self, id: str = "", include: List[str] = None, token: str = "") -> Building:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._buildingService.buildingById(id=id, tokenData=tokenData, include=include)

    @debugLogger
    def _constructObject(
        self,
        id: str = None,
        name: str = "",
        projectId: str = None,
        levels: List[BuildingLevel] = None,
        _sourceObject: Building = None,
        skipValidation: bool = False,
    ) -> Building:
        if _sourceObject is not None:
            return Building.createFrom(
                id=id,
                name=name if name is not None else _sourceObject.name(),
                projectId=projectId if projectId is not None else _sourceObject.projectId(),
                buildingLevels=levels if levels is not None else _sourceObject.levels(),
                skipValidation=skipValidation,
            )
        else:
            return Building.createFrom(
                id=id, name=name, projectId=projectId, buildingLevels=levels, skipValidation=skipValidation
            )
