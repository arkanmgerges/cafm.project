"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.token.TokenService import TokenService
from src.domain_model.user.User import User
from src.domain_model.user.UserRepository import UserRepository
from src.domain_model.user.UserService import UserService
from src.resource.logging.decorator import debugLogger


class UserApplicationService:
    def __init__(self, repo: UserRepository, userService: UserService):
        self._repo = repo
        self._domainService = userService

    @debugLogger
    def createUser(self, id: str = '', name: str = '', password: str = '', firstName: str = '', lastName: str = '',
                   addressOne: str = '', addressTwo: str = '', postalCode: str = '', objectOnly: bool = False,
                   token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._domainService.createUser(id=id, name=name, password=password, firstName=firstName,
                                              lastName=lastName,
                                              addressOne=addressOne, addressTwo=addressTwo,
                                              postalCode=postalCode, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateProject(self, id: str = '', name: str = '', password: str = '', firstName: str = '', lastName: str = '',
                      addressOne: str = '', addressTwo: str = '', postalCode: str = '', objectOnly: bool = False,
                      token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        user: User = self._repo.userById(id=id)
        self._domainService.updateUser(oldObject=user,
                                       newObject=User.createFrom(id=id, name=name, password=password,
                                                                 firstName=firstName,
                                                                 lastName=lastName,
                                                                 addressOne=addressOne, addressTwo=addressTwo,
                                                                 postalCode=postalCode),
                                       tokenData=tokenData)

    @debugLogger
    def deleteUser(self, id: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        user = self._repo.userById(id=id)
        self._domainService.deleteUser(user=user, tokenData=tokenData)

    @debugLogger
    def userByName(self, name: str, token: str = '') -> User:
        user = self._repo.userByName(name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return user

    @debugLogger
    def userById(self, id: str, token: str = '') -> User:
        user = self._repo.userById(id=id)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return user

    @debugLogger
    def users(self, resultFrom: int = 0, resultSize: int = 100, token: str = '',
              order: List[dict] = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._domainService.users(tokenData=tokenData,
                                         resultFrom=resultFrom,
                                         resultSize=resultSize,
                                         order=order)
