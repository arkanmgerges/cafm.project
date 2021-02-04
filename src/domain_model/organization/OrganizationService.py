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
    def createOrganization(self, obj: Organization, objectOnly: bool = False, tokenData: TokenData = None):
        try:
            if obj.id() == '':
                raise OrganizationDoesNotExistException()
            self._repo.organizationById(id=obj.id())
            raise OrganizationAlreadyExistException(obj.name())
        except OrganizationDoesNotExistException:
            if objectOnly:
                return Organization.createFromObject(obj=obj, generateNewId=True) if obj.id() == '' else obj
            else:
                obj: Organization = Organization.createFromObject(obj=obj, publishEvent=True)
                return obj

    @debugLogger
    def deleteOrganization(self, obj: Organization, tokenData: TokenData = None):
        obj.publishDelete()

    @debugLogger
    def updateOrganization(self, oldObject: Organization, newObject: Organization, tokenData: TokenData = None):
        newObject.publishUpdate(oldObject)

    @debugLogger
    def organizations(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
                      order: List[dict] = None):
        return self._repo.organizations(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
