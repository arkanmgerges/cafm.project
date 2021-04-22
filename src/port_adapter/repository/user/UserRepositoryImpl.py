"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from datetime import datetime
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from src.domain_model.resource.exception.ObjectIdenticalException import (
    ObjectIdenticalException,
)
from src.domain_model.resource.exception.UserDoesNotExistException import (
    UserDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.domain_model.user.User import User
from src.domain_model.user.UserRepository import UserRepository
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.User import User as DbUser
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class UserRepositoryImpl(UserRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-user')}"
            )
        except Exception as e:
            logger.warn(
                f"[{UserRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def createUser(self, obj: User, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = DbUser(
                id=obj.id(),
                email=obj.email(),
                firstName=obj.firstName(),
                lastName=obj.lastName(),
                addressOne=obj.addressOne(),
                addressTwo=obj.addressTwo(),
                postalCode=obj.postalCode(),
                phoneNumber=obj.phoneNumber(),
                avatarImage=obj.avatarImage(),
                countryId=obj.countryId(),
                cityId=obj.cityId(),
                countryStateName=obj.countryStateName(),
                startDate=datetime.utcfromtimestamp(obj.startDate())
                if obj.startDate() is not None
                else None,
            )
            result = dbSession.query(DbUser).filter_by(id=obj.id()).first()
            if result is None:
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteUser(self, obj: User, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbUser).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateUser(self, obj: User, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbUser).filter_by(id=obj.id()).first()
            if dbObject is None:
                raise UserDoesNotExistException(f"id = {obj.id()}")
            oldUser = self._userFromDbObject(dbObject)
            if oldUser != obj:
                dbObject.email = dbObject.email if obj.email() is None else obj.email()
                dbObject.firstName = (
                    dbObject.firstName if obj.firstName() is None else obj.firstName()
                )
                dbObject.lastName = (
                    dbObject.lastName if obj.lastName() is None else obj.lastName()
                )
                dbObject.addressOne = (
                    dbObject.addressOne
                    if obj.addressOne() is None
                    else obj.addressOne()
                )
                dbObject.addressTwo = (
                    dbObject.addressTwo
                    if obj.addressTwo() is None
                    else obj.addressTwo()
                )
                dbObject.postalCode = (
                    dbObject.postalCode
                    if obj.postalCode() is None
                    else obj.postalCode()
                )
                dbObject.phoneNumber = (
                    dbObject.phoneNumber
                    if obj.phoneNumber() is None
                    else obj.phoneNumber()
                )
                dbObject.avatarImage = (
                    dbObject.avatarImage
                    if obj.avatarImage() is None
                    else obj.avatarImage()
                )
                dbObject.countryId = (
                    dbObject.countryId if obj.countryId() is None else obj.countryId()
                )
                dbObject.cityId = (
                    dbObject.cityId if obj.cityId() is None else obj.cityId()
                )
                dbObject.countryStateName = (
                    dbObject.countryStateName
                    if obj.countryStateName() is None
                    else obj.countryStateName()
                )
                if obj.startDate() is not None:
                    dbObject.startDate = (
                        obj.startDate() if obj.startDate() > 0 else None
                    )
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def save(self, obj: User, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbUser).filter_by(id=obj.id()).first()
            if dbObject is not None:
                self.updateUser(obj=obj, tokenData=tokenData)
            else:
                self.createUser(obj=obj, tokenData=tokenData)
        finally:
            dbSession.close()

    @debugLogger
    def userByEmail(self, email: str) -> User:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbUser).filter_by(email=email).first()
            if dbObject is None:
                raise UserDoesNotExistException(f"email = {email}")
            return self._userFromDbObject(dbObject=dbObject)
        finally:
            dbSession.close()

    @debugLogger
    def userById(self, id: str) -> User:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbUser).filter_by(id=id).first()
            if dbObject is None:
                raise UserDoesNotExistException(f"id = {id}")
            return self._userFromDbObject(dbObject=dbObject)
        finally:
            dbSession.close()

    @debugLogger
    def _userFromDbObject(self, dbObject):
        return User.createFrom(
            id=dbObject.id,
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
            countryStateName=dbObject.countryStateName,
            startDate=dbObject.startDate.timestamp()
            if dbObject.startDate != None
            else None,
        )

    @debugLogger
    def users(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            sortData = ""
            if order is not None:
                for item in order:
                    sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
                sortData = sortData[2:]
            items = (
                dbSession.query(DbUser)
                .order_by(text(sortData))
                .limit(resultSize)
                .offset(resultFrom)
                .all()
            )
            itemsCount = dbSession.query(DbUser).count()
            if items is None:
                return {"items": [], "itemCount": 0}
            return {
                "items": [self._userFromDbObject(x) for x in items],
                "itemCount": itemsCount,
            }
        finally:
            dbSession.close()
