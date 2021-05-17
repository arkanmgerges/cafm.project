"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.resource.exception.OrganizationDoesNotExistException import (
    OrganizationDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.Organization import (
    Organization as DbOrganization,
)
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class OrganizationRepositoryImpl(OrganizationRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-organization')}"
            )
        except Exception as e:
            logger.warn(
                f"[{OrganizationRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def bulkSave(self, objList: List[Organization], tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            for obj in objList:
                dbObject = (
                    dbSession.query(DbOrganization).filter_by(id=obj.id()).first()
                )
                if dbObject is not None:
                    dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
                else:
                    dbObject = self._createDbObjectByObj(obj=obj)
                dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def bulkDelete(
        self, objList: List[Organization], tokenData: TokenData = None
    ) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            for obj in objList:
                dbObject = (
                    dbSession.query(DbOrganization).filter_by(id=obj.id()).first()
                )
                if dbObject is not None:
                    dbSession.delete(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def save(self, obj: Organization, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbOrganization).filter_by(id=obj.id()).first()
            if dbObject is not None:
                self.updateOrganization(obj=obj, dbObject=dbObject, tokenData=tokenData)
            else:
                self.createOrganization(obj=obj, tokenData=tokenData)
        finally:
            dbSession.close()

    @debugLogger
    def createOrganization(self, obj: Organization, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = self._createDbObjectByObj(obj=obj)
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteOrganization(
        self, obj: Organization, tokenData: TokenData = None
    ) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbOrganization).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateOrganization(
        self, obj: Organization, dbObject: DbOrganization, tokenData: TokenData = None
    ) -> None:
        from sqlalchemy import inspect

        dbSession = inspect(dbObject).session
        if dbObject is None:
            raise OrganizationDoesNotExistException(f"id = {obj.id()}")
        dbSession.add(self._updateDbObjectByObj(dbObject=dbObject, obj=obj))
        dbSession.commit()

    @debugLogger
    def organizationByName(self, name: str) -> Organization:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbOrganization).filter_by(name=name).first()
            if dbObject is None:
                raise OrganizationDoesNotExistException(f"name = {name}")
            return self._organizationFromDbObject(dbObject=dbObject)
        finally:
            dbSession.close()

    @debugLogger
    def organizationById(self, id: str) -> Organization:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbOrganization).filter_by(id=id).first()
            if dbObject is None:
                raise OrganizationDoesNotExistException(f"id = {id}")
            return self._organizationFromDbObject(dbObject=dbObject)
        finally:
            dbSession.close()

    @debugLogger
    def _organizationFromDbObject(self, dbObject: DbOrganization):
        return Organization(
            id=dbObject.id,
            name=dbObject.name,
            websiteUrl=dbObject.websiteUrl,
            organizationType=dbObject.organizationType,
            addressOne=dbObject.addressOne,
            addressTwo=dbObject.addressTwo,
            postalCode=dbObject.postalCode,
            countryId=dbObject.countryId,
            cityId=dbObject.cityId,
            countryStateName=dbObject.countryStateName,
            managerFirstName=dbObject.managerFirstName,
            managerLastName=dbObject.managerLastName,
            managerEmail=dbObject.managerEmail,
            managerPhoneNumber=dbObject.managerPhoneNumber,
            managerAvatar=dbObject.managerAvatar,
        )

    @debugLogger
    def organizations(
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
                dbSession.query(DbOrganization)
                .order_by(text(sortData))
                .limit(resultSize)
                .offset(resultFrom)
                .all()
            )
            itemsCount = dbSession.query(DbOrganization).count()
            if items is None:
                return {"items": [], "totalItemCount": 0}
            return {
                "items": [self._organizationFromDbObject(x) for x in items],
                "totalItemCount": itemsCount,
            }
        finally:
            dbSession.close()

    # @debugLogger
    # def organizationsByOrganizationType(
    #     self,
    #     organizationType: str,
    #     tokenData: TokenData,
    #     resultFrom: int = 0,
    #     resultSize: int = 100,
    #     order: List[dict] = None,
    # ) -> dict:
    #     dbSession = DbSession.newSession(dbEngine=self._db)
    #     try:
    #         sortData = ""
    #         if order is not None:
    #             for item in order:
    #                 sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
    #             sortData = sortData[2:]
    #         items = (
    #             dbSession.query(DbOrganization)
    #             .filter(DbOrganization.organizationType == organizationType)
    #             .order_by(text(sortData))
    #             .limit(resultSize)
    #             .offset(resultFrom)
    #             .all()
    #         )
    #         itemsCount = dbSession.query(DbOrganization).count()
    #         if items is None:
    #             return {"items": [], "totalItemCount": 0}
    #         return {
    #             "items": [self._organizationFromDbObject(x) for x in items],
    #             "totalItemCount": itemsCount,
    #         }
    #     finally:
    #         dbSession.close()

    def _updateDbObjectByObj(self, dbObject: DbOrganization, obj: Organization):
        dbObject.name = dbObject.name if obj.name() is None else obj.name()
        dbObject.websiteUrl = (
            dbObject.websiteUrl if obj.websiteUrl() is None else obj.websiteUrl()
        )
        dbObject.organizationType = (
            dbObject.organizationType
            if obj.organizationType() is None
            else obj.organizationType()
        )
        dbObject.addressOne = (
            dbObject.addressOne if obj.addressOne() is None else obj.addressOne()
        )
        dbObject.addressTwo = (
            dbObject.addressTwo if obj.addressTwo() is None else obj.addressTwo()
        )
        dbObject.postalCode = (
            dbObject.postalCode if obj.postalCode() is None else obj.postalCode()
        )
        dbObject.countryId = (
            dbObject.countryId if obj.countryId() is None else obj.countryId()
        )
        dbObject.cityId = dbObject.cityId if obj.cityId() is None else obj.cityId()
        dbObject.countryStateName = (
            dbObject.countryStateName
            if obj.countryStateName() is None
            else obj.countryStateName()
        )
        dbObject.managerFirstName = (
            dbObject.managerFirstName
            if obj.managerFirstName() is None
            else obj.managerFirstName()
        )
        dbObject.managerLastName = (
            dbObject.managerLastName
            if obj.managerLastName() is None
            else obj.managerLastName()
        )
        dbObject.managerEmail = (
            dbObject.managerEmail if obj.managerEmail() is None else obj.managerEmail()
        )
        dbObject.managerPhoneNumber = (
            dbObject.managerPhoneNumber
            if obj.managerPhoneNumber() is None
            else obj.managerPhoneNumber()
        )
        dbObject.managerAvatar = (
            dbObject.managerAvatar
            if obj.managerAvatar() is None
            else obj.managerAvatar()
        )
        return dbObject

    def _createDbObjectByObj(self, obj: Organization):
        return DbOrganization(
            id=obj.id(),
            name=obj.name(),
            websiteUrl=obj.websiteUrl(),
            organizationType=obj.organizationType(),
            addressOne=obj.addressOne(),
            addressTwo=obj.addressTwo(),
            postalCode=obj.postalCode(),
            countryId=obj.countryId(),
            cityId=obj.cityId(),
            countryStateName=obj.countryStateName(),
            managerFirstName=obj.managerFirstName(),
            managerLastName=obj.managerLastName(),
            managerEmail=obj.managerEmail(),
            managerPhoneNumber=obj.managerPhoneNumber(),
            managerAvatar=obj.managerAvatar(),
        )
