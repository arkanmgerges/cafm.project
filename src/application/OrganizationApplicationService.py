"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from logging import Logger
from src.application.ProjectApplicationService import ProjectApplicationService
from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.application.lifecycle.decorator.readOnly import readOnly
from src.application.lifecycle.decorator.transactional import transactional
from src.application.model.BaseApplicationServiceBulkData import BaseApplicationServiceBulkData
from src.application.model.BaseApplicationServiceModelData import BaseApplicationServiceModelData
from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.project.building.level.BuildingLevelRepository import BuildingLevelRepository
from src.domain_model.project.building.level.room.BuildingLevelRoomRepository import BuildingLevelRoomRepository



from src.domain_model.organization.OrganizationService import OrganizationService
from src.domain_model.resource.exception.UpdateOrganizationFailedException import (
    UpdateOrganizationFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger



class OrganizationApplicationService(BaseApplicationService):
    def __init__(self,
            repo: OrganizationRepository,
            buildingRepo: BuildingRepository,
            buildingLevelRepo: BuildingLevelRepository,
            buildingLevelRoomRepo: BuildingLevelRoomRepository,
            projectAppService: ProjectApplicationService,
            domainService: OrganizationService):
        self._repo = repo
        self._buildingRepo = buildingRepo
        self._buildingLevelRepo = buildingLevelRepo
        self._buildingLevelRoomRepo = buildingLevelRoomRepo
        self._projectAppService = projectAppService
        self._organizationService = domainService

    @debugLogger
    def newId(self):
        return Organization.createFrom(skipValidation=True).id()

    @transactional
    @debugLogger
    def createOrganization(self, token: str = None, objectOnly: bool = False, **kwargs):
        obj: Organization = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._organizationService.createOrganization(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @transactional
    @debugLogger
    def createOrganization(self, token: str = None, objectOnly: bool = False, **kwargs):
        obj: Organization = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._organizationService.createOrganization(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @readOnly
    @debugLogger
    def organizationByEmail(self, name: str, token: str = "", **_kwargs) -> Organization:
        obj = self._repo.organizationByName(name=name)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        return obj

    @transactional
    @debugLogger
    def updateOrganization(
        self,
        token: str = None,
        **kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Organization = self._repo.organizationById(
                id=kwargs["id"])
            super().callFunction(
                modelData=BaseApplicationServiceModelData(
                    function=self._organizationService.updateOrganization,
                    kwargs={
                        "oldObject": oldObject,
                        "newObject": self._constructObject(_sourceObject=oldObject, **kwargs),
                        "tokenData": tokenData,
                    },
                )
            )

        except Exception as e:
            raise UpdateOrganizationFailedException(message=str(e))

    @transactional
    @debugLogger
    def deleteOrganization(self, id: str, token: str = None, **_kwargs):
        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._organizationService.deleteOrganization,
                kwargs={
                    "obj": self._repo.organizationById(id=id),
                    "tokenData": TokenService.tokenDataFromToken(token=token),
                },
            )
        )

    @transactional
    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = ""):
        super()._bulkCreate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="organization_id",
                domainService=self._organizationService,
            )
        )

    @transactional
    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = ""):
        super()._bulkDelete(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="organization_id",
                domainService=self._organizationService,
            )
        )

    @transactional
    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = ""):
        super()._bulkUpdate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="organization_id",
                domainService=self._organizationService,
                repositoryCallbackFunction=self._repo.organizationById,
            )
        )

    @readOnly
    @debugLogger
    def organizationById(self, id: str, token: str = None, **_kwargs) -> Organization:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._repo.organizationById, kwargs={"id": id})
        )

    @readOnly
    @debugLogger
    def organizationsByType(
        self,
        type: str,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
        **_kwargs,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._organizationService.organizationsByType, kwargs={"resultFrom": resultFrom, "resultSize": resultSize,
                        "order": order, "tokenData": tokenData, "type": type})
        )

    @readOnly
    @debugLogger
    def organizations(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
        **_kwargs,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._organizationService.organizations,
                kwargs={"resultFrom": resultFrom, "resultSize": resultSize,
                        "order": order, "tokenData": tokenData},
            )
        )

    @transactional
    @debugLogger
    def linkOrganizationToBuilding(self, id, buildingId, buildingLevelId, buildingLevelRoomId, token: str = "", **_kwargs):
        _tokenData = TokenService.tokenDataFromToken(token=token)
        organization = self._repo.organizationById(id=id)

        building = self._buildingRepo.buildingById(id=buildingId)
        if building.projectId() != building.projectId():
            raise InvalidArgumentException(f'source organization project id: {building.projectId()} is not the same as destination building project id: {building.projectId()}')

        buildingLevel = self._buildingLevelRepo.buildingLevelById(id=buildingLevelId)
        buildingLevelRoom = self._buildingLevelRoomRepo.buildingLevelRoomById(id=buildingLevelRoomId)

        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._organizationService.linkOrganizationToBuilding,
                kwargs={
                    "organization": organization,
                    "building": building,
                    "buildingLevel": buildingLevel,
                    "buildingLevelRoom": buildingLevelRoom,
                    "tokenData": _tokenData,
                },
            )
        )

    @transactional
    @debugLogger
    def unlinkOrganizationToBuilding(self, id, buildingId, buildingLevelId, buildingLevelRoomId, token: str = "", **_kwargs):
        _tokenData = TokenService.tokenDataFromToken(token=token)
        organization = self._repo.organizationById(id=id)

        building = self._buildingRepo.buildingById(id=buildingId)
        if building.projectId() != building.projectId():
            raise InvalidArgumentException(f'source organization project id: {building.projectId()} is not the same as destination building project id: {building.projectId()}')

        buildingLevel = self._buildingLevelRepo.buildingLevelById(id=buildingLevelId)
        buildingLevelRoom = self._buildingLevelRoomRepo.buildingLevelRoomById(id=buildingLevelRoomId)

        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._organizationService.unlinkOrganizationToBuilding,
                kwargs={
                    "organization": organization,
                    "building": building,
                    "buildingLevel": buildingLevel,
                    "buildingLevelRoom": buildingLevelRoom,
                    "tokenData": _tokenData,
                },
            )
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> Organization:
        kwargs[BaseApplicationService.DOMAIN_MODEL_CLASS] = Organization
        return super()._constructObject(*args, **kwargs)
