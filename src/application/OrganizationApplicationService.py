"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.organization.OrganizationService import OrganizationService
from src.domain_model.resource.exception.UpdateOrganizationFailedException import (
    UpdateOrganizationFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class OrganizationApplicationService:
    def __init__(
        self, repo: OrganizationRepository, domainService: OrganizationService
    ):
        self._repo = repo
        self._domainService = domainService

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
        obj: Organization = self.constructObject(
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
        return self._domainService.createOrganization(
            obj=obj, objectOnly=objectOnly, tokenData=tokenData
        )

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
            obj: Organization = self.constructObject(
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
            self._domainService.updateOrganization(
                oldObject=oldObject, newObject=obj, tokenData=tokenData
            )
        except Exception as e:
            raise UpdateOrganizationFailedException(message=str(e))

    @debugLogger
    def deleteOrganization(self, id: str, token: str = ""):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.organizationById(id=id)
        self._domainService.deleteOrganization(obj=obj, tokenData=tokenData)

    @debugLogger
    def organizationByEmail(self, name: str, token: str = "") -> Organization:
        obj = self._repo.organizationByName(name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return obj

    @debugLogger
    def organizationById(self, id: str, token: str = "") -> Organization:
        obj = self._repo.organizationById(id=id)
        tokenData = TokenService.tokenDataFromToken(token=token)
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
        return self._domainService.organizations(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def constructObject(
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
        _sourceObject: Organization = None,
    ) -> Organization:
        if _sourceObject is not None:
            return Organization.createFrom(
                id=id,
                name=name if name is not None else _sourceObject.name(),
                websiteUrl=websiteUrl
                if websiteUrl is not None
                else _sourceObject.websiteUrl(),
                organizationType=organizationType
                if organizationType is not None
                else _sourceObject.organizationType(),
                addressOne=addressOne
                if addressOne is not None
                else _sourceObject.addressOne(),
                addressTwo=addressTwo
                if addressTwo is not None
                else _sourceObject.addressTwo(),
                postalCode=postalCode
                if postalCode is not None
                else _sourceObject.postalCode(),
                countryId=countryId
                if countryId is not None
                else _sourceObject.countryId(),
                cityId=cityId if cityId is not None else _sourceObject.cityId(),
                countryStateName=countryStateName
                if countryStateName is not None
                else _sourceObject.countryStateName(),
                managerFirstName=managerFirstName
                if managerFirstName is not None
                else _sourceObject.managerFirstName(),
                managerLastName=managerLastName
                if managerLastName is not None
                else _sourceObject.managerLastName(),
                managerEmail=managerEmail
                if managerEmail is not None
                else _sourceObject.managerEmail(),
                managerPhoneNumber=managerPhoneNumber
                if managerPhoneNumber is not None
                else _sourceObject.managerPhoneNumber(),
                managerAvatar=managerAvatar
                if managerAvatar is not None
                else _sourceObject.managerAvatar(),
            )
        else:
            return Organization.createFrom(
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
