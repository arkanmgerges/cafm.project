"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.organization.OrganizationService import OrganizationService
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class OrganizationApplicationService:
    def __init__(self, repo: OrganizationRepository, domainService: OrganizationService):
        self._repo = repo
        self._domainService = domainService

    @debugLogger
    def createOrganization(self, id: str = None, name: str = '', websiteUrl: str = '', organizationType: str = '',
                           addressOne: str = '', addressTwo: str = '', postalCode: str = '',
                           countryId: int = None, cityId: int = None,
                           stateName: str = '', managerFirstName: str = '', managerLastName: str = '',
                           managerEmail: str = '', managerPhoneNumber: str = '', managerAvatar: str = '',
                           objectOnly: bool = False,
                           token: str = '') -> Organization:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._domainService.createOrganization(id=id,
                                                      name=name,
                                                      websiteUrl=websiteUrl,
                                                      organizationType=organizationType,
                                                      addressOne=addressOne,
                                                      addressTwo=addressTwo,
                                                      postalCode=postalCode,
                                                      countryId=countryId,
                                                      cityId=cityId,
                                                      stateName=stateName,
                                                      managerFirstName=managerFirstName,
                                                      managerLastName=managerLastName,
                                                      managerEmail=managerEmail,
                                                      managerPhoneNumber=managerPhoneNumber,
                                                      managerAvatar=managerAvatar,
                                                      objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateOrganization(self, id: str = None, name: str = '', websiteUrl: str = '', organizationType: str = '',
                           addressOne: str = '', addressTwo: str = '', postalCode: str = '',
                           countryId: int = None, cityId: int = None,
                           stateName: str = '', managerFirstName: str = '', managerLastName: str = '',
                           managerEmail: str = '', managerPhoneNumber: str = '', managerAvatar: str = '',
                           token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj: Organization = self._repo.organizationById(id=id)
        self._domainService.updateOrganization(oldObject=obj,
                                               newObject=Organization.createFrom(id=id, name=name,
                                                                                 websiteUrl=websiteUrl,
                                                                                 organizationType=organizationType,
                                                                                 addressOne=addressOne,
                                                                                 addressTwo=addressTwo,
                                                                                 postalCode=postalCode,
                                                                                 countryId=countryId,
                                                                                 cityId=cityId,
                                                                                 stateName=stateName,
                                                                                 managerFirstName=managerFirstName,
                                                                                 managerLastName=managerLastName,
                                                                                 managerEmail=managerEmail,
                                                                                 managerPhoneNumber=managerPhoneNumber,
                                                                                 managerAvatar=managerAvatar),
                                               tokenData=tokenData)

    @debugLogger
    def deleteOrganization(self, id: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.organizationById(id=id)
        self._domainService.deleteOrganization(organization=obj, tokenData=tokenData)

    @debugLogger
    def organizationByEmail(self, name: str, token: str = '') -> Organization:
        obj = self._repo.organizationByName(name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return obj

    @debugLogger
    def organizationById(self, id: str, token: str = '') -> Organization:
        obj = self._repo.organizationById(id=id)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return obj

    @debugLogger
    def organizations(self, resultFrom: int = 0, resultSize: int = 100, token: str = '',
                      order: List[dict] = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._domainService.organizations(tokenData=tokenData,
                                                 resultFrom=resultFrom,
                                                 resultSize=resultSize,
                                                 order=order)
