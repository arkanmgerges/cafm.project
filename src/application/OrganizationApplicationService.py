"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.application.model.BaseApplicationServiceBulkData import BaseApplicationServiceBulkData
from src.application.model.BaseApplicationServiceModelData import BaseApplicationServiceModelData
from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.organization.OrganizationService import OrganizationService
from src.domain_model.resource.exception.UpdateOrganizationFailedException import (
    UpdateOrganizationFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class OrganizationApplicationService(BaseApplicationService):
    def __init__(self, repo: OrganizationRepository, domainService: OrganizationService):
        self._repo = repo
        self._organizationService = domainService

    @debugLogger
    def newId(self):
        return Organization.createFrom(skipValidation=True).id()

    @debugLogger
    def createOrganization(self, token: str = None, objectOnly: bool = False, **kwargs):
        obj: Organization = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._organizationService.createOrganization(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def organizationByEmail(self, name: str, token: str = "") -> Organization:
        obj = self._repo.organizationByName(name=name)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        return obj

    @debugLogger
    def updateOrganization(
        self,
        token: str = None,
        **kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Organization = self._repo.organizationById(id=kwargs["id"])
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

    @debugLogger
    def deleteOrganization(self, id: str, token: str = None):
        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._organizationService.deleteOrganization,
                kwargs={
                    "obj": self._repo.organizationById(id=id),
                    "tokenData": TokenService.tokenDataFromToken(token=token),
                },
            )
        )

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

    @debugLogger
    def organizationById(self, id: str, token: str = None) -> Organization:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(getterFunction=self._repo.organizationById, kwargs={"id": id})
        )

    @debugLogger
    def organizations(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._organizationService.organizations,
                kwargs={"resultFrom": resultFrom, "resultSize": resultSize, "order": order, "tokenData": tokenData},
            )
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> Organization:
        kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS] = Organization
        return super()._constructObject(*args, **kwargs)
