"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.lifecycle.decorator.readOnly import readOnly
from src.application.lookup.project.ProjectLookupRepository import ProjectLookupRepository
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class ProjectLookupApplicationService:
    def __init__(self, repo: ProjectLookupRepository):
        self._repo = repo

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
        return self._repo.lookup(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            filter=filter
        )
