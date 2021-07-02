"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.lifecycle.decorator.readOnly import readOnly
from src.application.lookup.organization.OrganizationLookupRepository import OrganizationLookupRepository
from src.domain_model.organization.OrganizationService import OrganizationService
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class OrganizationLookupApplicationService:
    def __init__(self, domainService: OrganizationService):
        self._domainService = domainService

    @readOnly
    @debugLogger
    def lookup(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
        filter: List[dict] = None
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._domainService.organizationsIncludeUsersIncludeRoles(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            filter=filter
        )
