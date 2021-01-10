"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from datetime import datetime
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from src.domain_model.resource.exception.ObjectIdenticalException import ObjectIdenticalException
from src.domain_model.resource.exception.UserDoesNotExistException import UserDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.domain_model.user.User import User
from src.domain_model.user.UserRepository import UserRepository
from src.port_adapter.repository.db_model.User import User as DbUser
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class UserRepositoryImpl(UserRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-user')}")
            SessionFactory = sessionmaker(bind=self._db)
            self._dbSession: Session = SessionFactory()
        except Exception as e:
            logger.warn(f'[{UserRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def createUser(self, user: User, tokenData: TokenData):
        dbObject = DbUser(id=user.id(), email=user.email(),
                          firstName=user.firstName(), lastName=user.lastName(),
                          addressOne=user.addressOne(), addressTwo=user.addressTwo(),
                          postalCode=user.postalCode(),
                          phoneNumber=user.phoneNumber(),
                          avatarImage=user.avatarImage(),
                          countryId=user.countryId(),
                          cityId=user.cityId(),
                          stateName=user.stateName(),
                          startDate=datetime.fromtimestamp(user.stateDate()) if user.stateDate() is not None else None)
        result = self._dbSession.query(DbUser).filter_by(id=user.id()).first()
        if result is None:
            self._dbSession.add(dbObject)
            self._dbSession.commit()

    @debugLogger
    def deleteUser(self, user: User, tokenData: TokenData) -> None:
        dbObject = self._dbSession.query(DbUser).filter_by(id=user.id()).first()
        if dbObject is not None:
            self._dbSession.delete(dbObject)
            self._dbSession.commit()

    @debugLogger
    def updateUser(self, user: User, tokenData: TokenData) -> None:
        dbObject = self._dbSession.query(DbUser).filter_by(id=user.id()).first()
        if dbObject is None:
            raise UserDoesNotExistException(f'id = {user.id()}')
        oldUser = self._userFromDbObject(dbObject)
        if oldUser == user:
            logger.debug(
                f'[{UserRepositoryImpl.updateUser.__qualname__}] Object identical exception for old user: {oldUser}\nuser: {user}')
            raise ObjectIdenticalException(f'user id: {user.id()}')
        dbObject.email = user.email()
        dbObject.firstName = user.firstName()
        dbObject.lastName = user.lastName()
        dbObject.addressOne = user.addressOne()
        dbObject.addressTwo = user.addressTwo()
        dbObject.postalCode = user.postalCode()
        dbObject.phoneNumber = user.phoneNumber()
        dbObject.avatarImage = user.avatarImage()
        dbObject.countryId = user.countryId()
        dbObject.cityId = user.cityId()
        dbObject.stateName = user.stateName()
        dbObject.startDate = user.stateDate()
        self._dbSession.add(dbObject)
        self._dbSession.commit()

    @debugLogger
    def userByEmail(self, email: str) -> User:
        dbObject = self._dbSession.query(DbUser).filter_by(email=email).first()
        if dbObject is None:
            raise UserDoesNotExistException(f'email = {email}')
        return self._userFromDbObject(dbObject=dbObject)

    @debugLogger
    def userById(self, id: str) -> User:
        dbObject = self._dbSession.query(DbUser).filter_by(id=id).first()
        if dbObject is None:
            raise UserDoesNotExistException(f'id = {id}')
        return self._userFromDbObject(dbObject=dbObject)

    @debugLogger
    def _userFromDbObject(self, dbObject):
        return User(id=dbObject.id,
                    email=dbObject.email,
                    firstName=dbObject.firstName,
                    lastName=dbObject.lastName,
                    addressOne=dbObject.addressOne,
                    addressTwo=dbObject.addressTwo,
                    postalCode=dbObject.postalCode,
                    phoneNumber=dbObject.phoneNumber,
                    avatarImage=dbObject.avatarImage,
                    countryId=dbObject.countryId,
                    cityId=dbObject.cityId,
                    stateName=dbObject.stateName,
                    startDate=dbObject.startDate.timestamp() if dbObject.startDate != None else None)

    @debugLogger
    def users(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
              order: List[dict] = None) -> dict:
        dbUsers = self._dbSession.query(DbUser).all()
        if dbUsers is None:
            return {"items": [], "itemCount": 0}
        items = dbUsers
        itemCount = len(items)
        items = items[resultFrom:resultFrom + resultSize]
        return {"items": [self._userFromDbObject(x) for x in items],
                "itemCount": itemCount}
