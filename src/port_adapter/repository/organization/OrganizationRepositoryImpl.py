"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.resource.exception.ObjectIdenticalException import ObjectIdenticalException
from src.domain_model.resource.exception.OrganizationDoesNotExistException import OrganizationDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.Organization import Organization as DbOrganization
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class OrganizationRepositoryImpl(OrganizationRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-organization')}")
        except Exception as e:
            logger.warn(
                f'[{OrganizationRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def createOrganization(self, obj: Organization, tokenData: TokenData):
        dbObject = DbOrganization(id=obj.id(), name=obj.name(),
                                  websiteUrl=obj.websiteUrl(),
                                  organizationType=obj.organizationType(),
                                  addressOne=obj.addressOne(), addressTwo=obj.addressTwo(),
                                  postalCode=obj.postalCode(),
                                  countryId=obj.countryId(),
                                  cityId=obj.cityId(),
                                  countryStateName=obj.countryStateName(),
                                  managerFirstName=obj.managerFirstName(),
                                  managerLastName=obj.managerLastName(),
                                  managerEmail=obj.managerEmail(),
                                  managerPhoneNumber=obj.managerPhoneNumber(),
                                  managerAvatar=obj.managerAvatar()
                                  )
        dbSession = DbSession.newSession(dbEngine=self._db)
        result = dbSession.query(DbOrganization).filter_by(id=obj.id()).first()
        if result is None:
            dbSession.add(dbObject)
            dbSession.commit()

    @debugLogger
    def deleteOrganization(self, obj: Organization, tokenData: TokenData) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        dbObject = dbSession.query(DbOrganization).filter_by(id=obj.id()).first()
        if dbObject is not None:
            dbSession.delete(dbObject)
            dbSession.commit()

    @debugLogger
    def updateOrganization(self, obj: Organization, tokenData: TokenData) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        dbObject: DbOrganization = dbSession.query(DbOrganization).filter_by(id=obj.id()).first()
        if dbObject is None:
            raise OrganizationDoesNotExistException(f'id = {obj.id()}')
        oldOrganization = self._organizationFromDbObject(dbObject)
        if oldOrganization == obj:
            logger.debug(
                f'[{OrganizationRepositoryImpl.updateOrganization.__qualname__}] Object identical exception for old organization: {oldOrganization}\norganization: {obj}')
            raise ObjectIdenticalException(f'organization id: {obj.id()}')
        dbObject.name = obj.name()
        dbObject.websiteUrl = obj.websiteUrl()
        dbObject.organizationType = obj.organizationType()
        dbObject.addressOne = obj.addressOne()
        dbObject.addressTwo = obj.addressTwo()
        dbObject.postalCode = obj.postalCode()
        dbObject.countryId = obj.countryId()
        dbObject.cityId = obj.cityId()
        dbObject.countryStateName = obj.countryStateName()
        dbObject.managerFirstName = obj.managerFirstName()
        dbObject.managerLastName = obj.managerLastName()
        dbObject.managerEmail = obj.managerEmail()
        dbObject.managerPhoneNumber = obj.managerPhoneNumber()
        dbObject.managerAvatar = obj.managerAvatar()
        dbSession.add(dbObject)
        dbSession.commit()

    @debugLogger
    def organizationByName(self, name: str) -> Organization:
        dbSession = DbSession.newSession(dbEngine=self._db)
        dbObject = dbSession.query(DbOrganization).filter_by(name=name).first()
        if dbObject is None:
            raise OrganizationDoesNotExistException(f'name = {name}')
        return self._organizationFromDbObject(dbObject=dbObject)

    @debugLogger
    def organizationById(self, id: str) -> Organization:
        dbSession = DbSession.newSession(dbEngine=self._db)
        dbObject = dbSession.query(DbOrganization).filter_by(id=id).first()
        if dbObject is None:
            raise OrganizationDoesNotExistException(f'id = {id}')
        return self._organizationFromDbObject(dbObject=dbObject)

    @debugLogger
    def _organizationFromDbObject(self, dbObject: DbOrganization):
        return Organization(id=dbObject.id,
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
                            managerAvatar=dbObject.managerAvatar)

    @debugLogger
    def organizations(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
                      order: List[dict] = None) -> dict:
        sortData = ''
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]
        dbSession = DbSession.newSession(dbEngine=self._db)
        items = dbSession.query(DbOrganization).order_by(text(sortData)).limit(resultSize).offset(
            resultFrom).all()
        itemsCount = dbSession.query(DbOrganization).count()
        if items is None:
            return {"items": [], "itemCount": 0}
        return {"items": [self._organizationFromDbObject(x) for x in items],
                "itemCount": itemsCount}
