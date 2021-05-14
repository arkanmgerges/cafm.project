"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.domain_model.resource.exception.UpdateUserFailedException import (
    UpdateUserFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.domain_model.user.User import User
from src.domain_model.user.UserRepository import UserRepository
from src.domain_model.user.UserService import UserService
from src.resource.logging.decorator import debugLogger


class UserApplicationService(BaseApplicationService):
    def __init__(self, repo: UserRepository, userService: UserService):
        self._repo = repo
        self._domainService = userService

    @debugLogger
    def newId(self):
        return User.createFrom().id()

    @debugLogger
    def createUser(self, token: str = None, objectOnly: bool = False, **kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj: User = self._constructObject(**kwargs)
        return self._domainService.createUser(
            obj=obj, objectOnly=objectOnly, tokenData=tokenData
        )

    @debugLogger
    def updateUser(self, token: str = None, **kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: User = self._repo.userById(id=kwargs["id"])
            obj: User = self._constructObject(_sourceObject=oldObject, **kwargs)
            self._domainService.updateUser(
                oldObject=oldObject, newObject=obj, tokenData=tokenData
            )
        except Exception as e:
            raise UpdateUserFailedException(message=str(e))

    @debugLogger
    def deleteUser(self, id: str, token: str = ""):
        tokenData = TokenService.tokenDataFromToken(token=token)
        user = self._repo.userById(id=id)
        self._domainService.deleteUser(obj=user, tokenData=tokenData)

    @debugLogger
    def userByEmail(self, email: str, token: str = "") -> User:
        user = self._repo.userByEmail(email=email)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        return user

    @debugLogger
    def userById(self, id: str, token: str = "") -> User:
        user = self._repo.userById(id=id)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        return user

    @debugLogger
    def users(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._domainService.users(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> User:
        kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS] = User
        return super()._constructObject(*args, **kwargs)
