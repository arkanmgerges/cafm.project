"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.resource.exception.UpdateUserFailedException import UpdateUserFailedException
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
    def newId(self):
        return User.createFrom().id()

    @debugLogger
    def createUser(self, id: str = None, email: str = '', firstName: str = '', lastName: str = '',
                   addressOne: str = '', addressTwo: str = '', postalCode: str = '', phoneNumber: str = '',
                   avatarImage: str = '', countryId: int = None, cityId: int = None,
                   countryStateName: str = '', startDate: float = None,
                   objectOnly: bool = False,
                   token: str = '') -> User:
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj: User = self.constructObject(id=id, email=email, firstName=firstName, lastName=lastName,
                                         addressOne=addressOne, addressTwo=addressTwo, postalCode=postalCode,
                                         phoneNumber=phoneNumber, avatarImage=avatarImage, countryId=countryId,
                                         cityId=cityId,
                                         startDate=startDate, countryStateName=countryStateName)
        return self._domainService.createUser(obj=obj,
                                              objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateUser(self, id: str = None, email: str = None, firstName: str = None, lastName: str = None,
                   addressOne: str = None, addressTwo: str = None, postalCode: str = None, phoneNumber: str = None,
                   avatarImage: str = None, countryId: int = None, cityId: int = None,
                   countryStateName: str = None, startDate: float = None,
                   token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            user: User = self._repo.userById(id=id)
            obj: User = self.constructObject(id=id, email=email, firstName=firstName, lastName=lastName,
                                             addressOne=addressOne, addressTwo=addressTwo, postalCode=postalCode,
                                             phoneNumber=phoneNumber, avatarImage=avatarImage, countryId=countryId,
                                             cityId=cityId,
                                             startDate=startDate, countryStateName=countryStateName, _sourceObject=user)
            self._domainService.updateUser(oldObject=user,
                                           newObject=obj,
                                           tokenData=tokenData)
        except Exception as e:
            raise UpdateUserFailedException(message=str(e))

    @debugLogger
    def deleteUser(self, id: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        user = self._repo.userById(id=id)
        self._domainService.deleteUser(obj=user, tokenData=tokenData)

    @debugLogger
    def userByEmail(self, email: str, token: str = '') -> User:
        user = self._repo.userByEmail(email=email)
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

    @debugLogger
    def constructObject(self, id: str = None, email: str = None, firstName: str = None, lastName: str = None,
                        addressOne: str = None, addressTwo: str = None, postalCode: str = None, phoneNumber: str = None,
                        avatarImage: str = None, countryId: int = None, cityId: int = None,
                        countryStateName: str = None, startDate: float = None, _sourceObject: User = None) -> User:
        if _sourceObject is not None:
            return User.createFrom(id=id,
                                   email=email if email is not None else _sourceObject.email(),
                                   firstName=firstName if firstName is not None else _sourceObject.firstName(),
                                   lastName=lastName if lastName is not None else _sourceObject.lastName(),
                                   addressOne=addressOne if addressOne is not None else _sourceObject.addressOne(),
                                   addressTwo=addressTwo if addressTwo is not None else _sourceObject.addressTwo(),
                                   postalCode=postalCode if postalCode is not None else _sourceObject.postalCode(),
                                   phoneNumber=phoneNumber if phoneNumber is not None else _sourceObject.phoneNumber(),
                                   avatarImage=avatarImage if avatarImage is not None else _sourceObject.avatarImage(),
                                   countryId=countryId if countryId is not None else _sourceObject.countryId(),
                                   cityId=cityId if cityId is not None else _sourceObject.cityId(),
                                   startDate=startDate if startDate is not None else _sourceObject.startDate(),
                                   countryStateName=countryStateName if countryStateName is not None else _sourceObject.countryStateName()
                                   )
        else:
            return User.createFrom(id=id, email=email, firstName=firstName, lastName=lastName,
                               addressOne=addressOne, addressTwo=addressTwo, postalCode=postalCode,
                               phoneNumber=phoneNumber, avatarImage=avatarImage, countryId=countryId, cityId=cityId,
                               startDate=startDate, countryStateName=countryStateName)
