"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.user.UserRepository import UserRepository

from src.domain_model.resource.exception.UserAlreadyExistException import UserAlreadyExistException
from src.domain_model.resource.exception.UserDoesNotExistException import UserDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.domain_model.user.User import User
from src.resource.logging.decorator import debugLogger


class UserService:
    def __init__(self, userRepo: UserRepository):
        self._repo = userRepo

    @debugLogger
    def createUser(self, obj: User,
                   objectOnly: bool = False, tokenData: TokenData = None):
        try:
            if obj.id() == '':
                raise UserDoesNotExistException()
            self._repo.userById(id=obj.id())
            raise UserAlreadyExistException(obj.email())
        except UserDoesNotExistException:
            if objectOnly:
                return obj
            else:
                user: User = User.createFromObject(obj=obj, publishEvent=True)
                self._repo.createUser(user=user, tokenData=tokenData)
                return user

    @debugLogger
    def deleteUser(self, user: User, tokenData: TokenData = None):
        self._repo.deleteUser(user, tokenData=tokenData)
        user.publishDelete()

    @debugLogger
    def updateUser(self, oldObject: User, newObject: User, tokenData: TokenData = None):
        self._repo.updateUser(newObject, tokenData=tokenData)
        newObject.publishUpdate(oldObject)

    @debugLogger
    def users(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
              order: List[dict] = None):
        return self._repo.users(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
