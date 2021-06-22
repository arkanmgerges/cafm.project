"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.lifecycle.decorator.readOnly import readOnly
from src.application.lookup.user.UserLookup import UserLookup
from src.application.lookup.user.UserLookupRepository import UserLookupRepository
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class UserLookupApplicationService:
    def __init__(self, repo: UserLookupRepository):
        self._repo = repo

    @readOnly
    @debugLogger
    def userLookupByUserId(self, id: str, token: str = "") -> UserLookup:
        _tokenData = TokenService.tokenDataFromToken(token=token)
        userLookup: UserLookup = self._repo.userLookupByUserId(id=id)
        return userLookup

    @readOnly
    @debugLogger
    def userLookupByUserEmail(self, email: str, token: str = "") -> UserLookup:
        _tokenData = TokenService.tokenDataFromToken(token=token)
        userLookup: UserLookup = self._repo.userLookupByUserEmail(email=email)
        return userLookup

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
