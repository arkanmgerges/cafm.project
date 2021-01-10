"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.resource.exception.OrganizationAlreadyExistException import OrganizationAlreadyExistException
from src.domain_model.resource.exception.OrganizationDoesNotExistException import OrganizationDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class OrganizationService:
    def __init__(self, organizationRepo: OrganizationRepository):
        self._repo = organizationRepo

    @debugLogger
    def createOrganization(self, id: str = None, name: str = '', websiteUrl: str = '', organizationType: str = '',
                           addressOne: str = '', addressTwo: str = '', postalCode: str = '',
                           countryId: int = None, cityId: int = None,
                           stateName: str = '', managerFirstName: str = '', managerLastName: str = '',
                           managerEmail: str = '', managerPhoneNumber: str = '', managerAvatar: str = '',
                           objectOnly: bool = False, tokenData: TokenData = None):
        try:
            if id == '':
                raise OrganizationDoesNotExistException()
            self._repo.organizationById(id=id)
            raise OrganizationAlreadyExistException(name)
        except OrganizationDoesNotExistException:
            if objectOnly:
                if id == '':
                    id = None
                return Organization.createFrom(id=id, name=name,
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
                                               managerAvatar=managerAvatar)
            else:
                obj: Organization = Organization.createFrom(id=id, name=name,
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
                                                            managerAvatar=managerAvatar, publishEvent=True)
                self._repo.createOrganization(organization=obj, tokenData=tokenData)
                return obj

    @debugLogger
    def deleteOrganization(self, organization: Organization, tokenData: TokenData = None):
        self._repo.deleteOrganization(organization, tokenData=tokenData)
        organization.publishDelete()

    @debugLogger
    def updateOrganization(self, oldObject: Organization, newObject: Organization, tokenData: TokenData = None):
        self._repo.updateOrganization(newObject, tokenData=tokenData)
        newObject.publishUpdate(oldObject)

    @debugLogger
    def organizations(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
                      order: List[dict] = None):
        return self._repo.organizations(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
