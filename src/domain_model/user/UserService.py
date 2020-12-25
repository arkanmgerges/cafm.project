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
    def createUser(self, id: str = '', name: str = '', firstName: str = '', lastName: str = '',
                   addressOne: str = '', addressTwo: str = '', postalCode: str = '', avatarImage: str = '',
                   objectOnly: bool = False, tokenData: TokenData = None):
        try:
            if id == '':
                raise UserDoesNotExistException()
            self._repo.userById(id=id)
            raise UserAlreadyExistException(name)
        except UserDoesNotExistException:
            if objectOnly:
                if id == '':
                    id = None
                return User.createFrom(id=id, name=name, firstName=firstName,
                                       lastName=lastName, addressOne=addressOne, addressTwo=addressTwo,
                                       avatarImage=avatarImage, postalCode=postalCode)
            else:
                user: User = User.createFrom(id=id, name=name, firstName=firstName,
                                       lastName=lastName, addressOne=addressOne, addressTwo=addressTwo,
                                       postalCode=postalCode, avatarImage=avatarImage, publishEvent=True)
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
