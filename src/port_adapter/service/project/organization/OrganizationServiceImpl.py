"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.lookup.organization.OrganizationLookupRepository import OrganizationLookupRepository
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.organization.OrganizationService import OrganizationService
from src.domain_model.resource.exception.OrganizationDoesNotExistException import OrganizationDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.service.identity.IdentityAndAccessAdapter import IdentityAndAccessAdapter
from src.resource.logging.decorator import debugLogger


class OrganizationServiceImpl(OrganizationService):
    def __init__(self, organizationRepo: OrganizationRepository, lookupOrganizationRepo: OrganizationLookupRepository,
                 identityAndAccessAdapter: IdentityAndAccessAdapter):
        self._repo = organizationRepo
        self._lookupRepo = lookupOrganizationRepo
        self._identityAndAccessAdapter = identityAndAccessAdapter

    @debugLogger
    def organizationById(
            self,
            tokenData: TokenData = None,
            id: str = "",
    ):
        try:
            _ = self._identityAndAccessAdapter.organizationById(tokenData=tokenData, id=id)
        except:
            raise OrganizationDoesNotExistException(f'organization id: {id}')
        return self._repo.organizationById(id = id,)

    @debugLogger
    def organizations(
            self,
            tokenData: TokenData = None,
            resultFrom: int = 0,
            resultSize: int = 100,
            order: List[dict] = None,
    ):
        organizationList = self._identityAndAccessAdapter.organizations(tokenData=tokenData)["items"]
        return self._repo.organizationsFilteredByOrganizationList(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            organizationList=organizationList,
        )

    @debugLogger
    def organizationsByType(
            self,
            tokenData: TokenData = None,
            resultFrom: int = 0,
            resultSize: int = 100,
            order: List[dict] = None,
            type: str = None,
    ):
        organizationList = self._identityAndAccessAdapter.organizationsByType(tokenData=tokenData, type=type)["items"]
        return self._repo.organizationsFilteredByOrganizationList(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            organizationList=organizationList,
        )

    def organizationsIncludeUsersIncludeRoles(self,
        tokenData: TokenData = None,
        type: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        filter: List[dict] = None,) -> dict:

        response = self._identityAndAccessAdapter.organizationsIncludeUsersIncludeRoles(tokenData=tokenData)["items"]
        return self._lookupRepo.organizationsFilteredByOrganizationsIncludeUsersIncludeRoles(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            filter=filter,
            organizationsIncludeUsersIncludeRoles=response,
        )