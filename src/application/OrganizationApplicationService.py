"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.organization.OrganizationService import OrganizationService
from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.resource.exception.UpdateOrganizationFailedException import (
    UpdateOrganizationFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.domain_model.util.DomainModelAttributeValidator import DomainModelAttributeValidator
from src.resource.common.Util import Util
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
    def updateOrganization(self, token: str = None, **kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Organization = self._repo.organizationById(id=kwargs["id"])
            obj: Organization = self._constructObject(_sourceObject=oldObject, **kwargs)
            self._organizationService.updateOrganization(oldObject=oldObject, newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateOrganizationFailedException(message=str(e))

    @debugLogger
    def deleteOrganization(self, id: str, token: str = ""):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.organizationById(id=id)
        self._organizationService.deleteOrganization(obj=obj, tokenData=tokenData)

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
                        **Util.snakeCaseToLowerCameCaseDict(
                            objListParamsItem, keyReplacements=[{"source": "organization_id", "target": "id"}]
                        )
                    )
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._organizationService.bulkCreate(objList=objList)
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
                objList.append(self._constructObject(id=objListParamsItem["organization_id"], skipValidation=True))
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._organizationService.bulkDelete(objList=objList)
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
                oldObject: Organization = self._repo.organizationById(id=objListParamsItem["organization_id"])
                newObject = self._constructObject(
                    **Util.snakeCaseToLowerCameCaseDict(
                        objListParamsItem, keyReplacements=[{"source": "organization_id", "target": "id"}]
                    ),
                    _sourceObject=oldObject,
                )
                objList.append(
                    (newObject, oldObject),
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._organizationService.bulkUpdate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def organizationByEmail(self, name: str, token: str = "") -> Organization:
        obj = self._repo.organizationByName(name=name)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        return obj

    @debugLogger
    def organizationById(self, id: str, token: str = "") -> Organization:
        obj = self._repo.organizationById(id=id)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        return obj

    @debugLogger
    def organizations(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._organizationService.organizations(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> Organization:
        kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS] = Organization
        return super()._constructObject(*args, **kwargs)
