"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from sqlalchemy.sql.expression import text

from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from src.domain_model.resource.exception.UserDoesNotExistException import (
    UserDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.domain_model.user.User import User
from src.domain_model.user.UserRepository import UserRepository
from src.port_adapter.repository.db_model.User import User as DbUser
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class UserRepositoryImpl(UserRepository):
    @debugLogger
    def createUser(self, obj: User, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
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
            countryStateIsoCode=obj.countryStateIsoCode(),
            startDate=DateTimeHelper.intToDateTime(obj.startDate())
            if obj.startDate() is not None and obj.startDate() > 0
            else None,
        )
        result = dbSession.query(DbUser).filter_by(id=obj.id()).first()
        if result is None:
            dbSession.add(dbObject)
    

    @debugLogger
    def deleteUser(self, obj: User, tokenData: TokenData = None) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbUser).filter_by(id=obj.id()).first()
        if dbObject is not None:
            dbSession.delete(dbObject)
    

    @debugLogger
    def updateUser(self, obj: User, tokenData: TokenData = None) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
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
            dbObject.countryStateIsoCode = (
                dbObject.countryStateIsoCode
                if obj.countryStateIsoCode() is None
                else obj.countryStateIsoCode()
            )
            if obj.startDate() is not None:
                dbObject.startDate = (
                    DateTimeHelper.intToDateTime(obj.startDate())
                    if obj.startDate() is not None and obj.startDate() > 0
                    else None
                )
            dbSession.add(dbObject)
    

    @debugLogger
    def save(self, obj: User, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbUser).filter_by(id=obj.id()).first()
        if dbObject is not None:
            self.updateUser(obj=obj, tokenData=tokenData)
        else:
            self.createUser(obj=obj, tokenData=tokenData)


    @debugLogger
    def userByEmail(self, email: str) -> User:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbUser).filter_by(email=email).first()
        if dbObject is None:
            raise UserDoesNotExistException(f"email = {email}")
        return self._userFromDbObject(dbObject=dbObject)


    @debugLogger
    def userById(self, id: str) -> User:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbUser).filter_by(id=id).first()
        if dbObject is None:
            raise UserDoesNotExistException(f"id = {id}")
        return self._userFromDbObject(dbObject=dbObject)


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
            countryStateIsoCode=dbObject.countryStateIsoCode,
            startDate=DateTimeHelper.datetimeToInt(dbObject.startDate),
        )

    @debugLogger
    def users(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
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
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [self._userFromDbObject(x) for x in items],
            "totalItemCount": itemsCount,
        }


    @debugLogger
    def usersByOrganizationId(
        self,
        tokenData: TokenData,
        organizationId: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        sortData = ""
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]

        userListQuery = text(
            """select distinct (user_id) from user
                join user__role__junction on user.id = user__role__junction.user_id
                join role__organization__junction roj on user__role__junction.role_id = roj.role_id
            where organization_id=:organizationId""")
        userListResult = dbSession.execute(userListQuery, {"organizationId": organizationId})
        userIds = []
        for row in userListResult:
            userIds.append(row['user_id'])

        logger.debug(userIds.__len__())
        if userIds.__len__() == 0:
            return {"items": [], "totalItemCount": 0}

        items = (
            dbSession.query(DbUser)
            .filter(DbUser.id.in_(userIds))
            .order_by(text(sortData))
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )

        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [self._userFromDbObject(x) for x in items],
            "totalItemCount": userIds.__len__(),
        }

