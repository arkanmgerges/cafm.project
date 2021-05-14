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
from src.resource.logging.decorator import debugLogger


class OrganizationApplicationService(BaseApplicationService):
    def __init__(self, repo: OrganizationRepository, domainService: OrganizationService):
        self._repo = repo
        self._organizationService = domainService

    @debugLogger
    def newId(self):
        return Organization.createFrom(skipValidation=True).id()

    @debugLogger
    def createOrganization(
        self,
        id: str = None,
        name: str = "",
        websiteUrl: str = "",
        organizationType: str = "",
        addressOne: str = "",
        addressTwo: str = "",
        postalCode: str = "",
        countryId: int = None,
        cityId: int = None,
        countryStateName: str = "",
        managerFirstName: str = "",
        managerLastName: str = "",
        managerEmail: str = "",
        managerPhoneNumber: str = "",
        managerAvatar: str = "",
        objectOnly: bool = False,
        token: str = "",
    ) -> Organization:
        obj: Organization = self._constructObject(
            id=id,
            name=name,
            websiteUrl=websiteUrl,
            organizationType=organizationType,
            addressOne=addressOne,
            addressTwo=addressTwo,
            postalCode=postalCode,
            countryId=countryId,
            cityId=cityId,
            countryStateName=countryStateName,
            managerFirstName=managerFirstName,
            managerLastName=managerLastName,
            managerEmail=managerEmail,
            managerPhoneNumber=managerPhoneNumber,
            managerAvatar=managerAvatar,
        )
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._organizationService.createOrganization(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateOrganization(
        self,
        id: str = None,
        name: str = None,
        websiteUrl: str = None,
        organizationType: str = None,
        addressOne: str = None,
        addressTwo: str = None,
        postalCode: str = None,
        countryId: int = None,
        cityId: int = None,
        countryStateName: str = None,
        managerFirstName: str = None,
        managerLastName: str = None,
        managerEmail: str = None,
        managerPhoneNumber: str = None,
        managerAvatar: str = None,
        token: str = "",
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Organization = self._repo.organizationById(id=id)
            obj: Organization = self._constructObject(
                id=id,
                name=name,
                websiteUrl=websiteUrl,
                organizationType=organizationType,
                addressOne=addressOne,
                addressTwo=addressTwo,
                postalCode=postalCode,
                countryId=countryId,
                cityId=cityId,
                countryStateName=countryStateName,
                managerFirstName=managerFirstName,
                managerLastName=managerLastName,
                managerEmail=managerEmail,
                managerPhoneNumber=managerPhoneNumber,
                managerAvatar=managerAvatar,
                _sourceObject=oldObject,
            )
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
                        id=objListParamsItem["organization_id"],
                        name=objListParamsItem["name"],
                        websiteUrl=objListParamsItem["website_url"],
                        organizationType=objListParamsItem["organization_type"],
                        addressOne=objListParamsItem["address_one"],
                        addressTwo=objListParamsItem["address_two"],
                        postalCode=objListParamsItem["postal_code"],
                        countryId=objListParamsItem["country_id"],
                        cityId=objListParamsItem["city_id"],
                        countryStateName=objListParamsItem["country_state_name"],
                        managerFirstName=objListParamsItem["manager_first_name"],
                        managerLastName=objListParamsItem["manager_last_name"],
                        managerEmail=objListParamsItem["manager_email"],
                        managerPhoneNumber=objListParamsItem["manager_phone_number"],
                        managerAvatar=objListParamsItem["manager_avatar"],
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
                    id=objListParamsItem["organization_id"],
                    name=objListParamsItem["name"] if "name" in objListParamsItem else None,
                    websiteUrl=objListParamsItem["website_url"] if "website_url" in objListParamsItem else None,
                    organizationType=objListParamsItem["organization_type"]
                    if "organization_type" in objListParamsItem
                    else None,
                    addressOne=objListParamsItem["address_one"] if "address_one" in objListParamsItem else None,
                    addressTwo=objListParamsItem["address_two"] if "address_two" in objListParamsItem else None,
                    postalCode=objListParamsItem["postal_code"] if "postal_code" in objListParamsItem else None,
                    countryId=objListParamsItem["country_id"] if "country_id" in objListParamsItem else None,
                    cityId=objListParamsItem["city_id"] if "city_id" in objListParamsItem else None,
                    countryStateName=objListParamsItem["country_state_name"]
                    if "country_state_name" in objListParamsItem
                    else None,
                    managerFirstName=objListParamsItem["manager_first_name"]
                    if "manager_first_name" in objListParamsItem
                    else None,
                    managerLastName=objListParamsItem["manager_last_name"]
                    if "manager_last_name" in objListParamsItem
                    else None,
                    managerEmail=objListParamsItem["manager_email"] if "manager_email" in objListParamsItem else None,
                    managerPhoneNumber=objListParamsItem["manager_phone_number"]
                    if "manager_phone_number" in objListParamsItem
                    else None,
                    managerAvatar=objListParamsItem["manager_avatar"]
                    if "manager_avatar" in objListParamsItem
                    else None,
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
