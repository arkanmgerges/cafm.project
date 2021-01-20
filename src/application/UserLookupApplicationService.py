"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.application.user_lookup.UserLookup import UserLookup
from src.application.user_lookup.UserLookupRepository import UserLookupRepository
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class UserLookupApplicationService:
    def __init__(self, repo: UserLookupRepository):
        self._repo = repo

    @debugLogger
    def userLookupByUserId(self, id: str, token: str = '') -> UserLookup:
        userLookup: UserLookup = self._repo.userLookupByUserId(id=id)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return userLookup
