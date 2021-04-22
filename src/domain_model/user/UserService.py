"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.resource.exception.UserAlreadyExistException import (
    UserAlreadyExistException,
)
from src.domain_model.resource.exception.UserDoesNotExistException import (
    UserDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.domain_model.user.User import User
from src.domain_model.user.UserRepository import UserRepository
from src.resource.logging.decorator import debugLogger


class UserService:
    def __init__(self, userRepo: UserRepository):
        self._repo = userRepo

    @debugLogger
    def createUser(
        self, obj: User, objectOnly: bool = False, tokenData: TokenData = None
    ):
        if objectOnly:
            return (
                User.createFromObject(obj=obj, generateNewId=True)
                if obj.id() == ""
                else obj
            )
        else:
            obj: User = User.createFromObject(obj=obj, publishEvent=True)
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def deleteUser(self, obj: User, tokenData: TokenData = None):
        obj.publishDelete()
        self._repo.deleteUser(obj=obj)

    @debugLogger
    def updateUser(self, oldObject: User, newObject: User, tokenData: TokenData = None):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def users(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.users(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )
