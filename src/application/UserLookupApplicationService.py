"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.user_lookup.UserLookup import UserLookup
from src.application.user_lookup.UserLookupRepository import UserLookupRepository
from src.domain_model.token.TokenData import TokenData
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class UserLookupApplicationService:
    def __init__(self, repo: UserLookupRepository):
        self._repo = repo

    @debugLogger
    def userLookupByUserId(self, id: str, token: str = "") -> UserLookup:
        tokenData = TokenService.tokenDataFromToken(token=token)
        userLookup: UserLookup = self._repo.userLookupByUserId(id=id)
        return userLookup

    @debugLogger
    def userLookupByUserEmail(self, email: str, token: str = "") -> UserLookup:
        tokenData = TokenService.tokenDataFromToken(token=token)
        userLookup: UserLookup = self._repo.userLookupByUserEmail(email=email)
        return userLookup

    @debugLogger
    def userLookups(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._repo.userLookups(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )
