"""
@author: Mohammad S. moso<moso@develoop.run>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from src.domain_model.resource.exception.ObjectIdenticalException import ObjectIdenticalException
from src.port_adapter.repository.DbSession import DbSession
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.logger import logger
from src.domain_model.subcontractor.SubcontractorRepository import SubcontractorRepository
from src.port_adapter.repository.db_model.Subcontractor import Subcontractor as DbSSubcontractor
from src.domain_model.resource.exception.SubcontractorDoesNotExistException import SubcontractorDoesNotExistException
from src.resource.logging.decorator import debugLogger


class SubcontractorRepositoryImpl(SubcontractorRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}")
        except Exception as e:
            logger.warn(
                f'[{SubcontractorRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def save(self, obj: Subcontractor, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbSSubcontractor).filter_by(id=obj.id()).first()
            if dbObject is not None:
                self.updateSubcontractor(obj=obj, tokenData=tokenData)
            else:
                self.createSubcontractor(obj=obj, tokenData=tokenData)
        finally:
            dbSession.close()

    @debugLogger
    def createSubcontractor(self, obj: Subcontractor, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = DbSSubcontractor(id=obj.id(), companyName=obj.companyName(),
                                        websiteUrl=obj.websiteUrl(),
                                        contactPerson=obj.contactPerson(),
                                        email=obj.email(),
                                        phoneNumber=obj.phoneNumber(),
                                        addressOne=obj.addressOne(),
                                        addressTwo=obj.addressTwo())

            result = dbSession.query(DbSSubcontractor).filter_by(id=obj.id()).first()
            if result is None:
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteSubcontractor(self, obj: Subcontractor, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbSSubcontractor).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateSubcontractor(self, obj: Subcontractor, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject: DbSSubcontractor = dbSession.query(DbSSubcontractor).filter_by(id=obj.id()).first()
            if dbObject is None:
                raise SubcontractorDoesNotExistException(f'id = {obj.id()}')
            oldSubcontractor = self._subcontractorFromDbObject(dbObject)
            if oldSubcontractor != obj:
                dbObject.companyName = dbObject.companyName if obj.companyName() is None else obj.companyName()
                dbObject.websiteUrl = dbObject.websiteUrl if obj.websiteUrl() is None else obj.websiteUrl()
                dbObject.contactPerson = dbObject.contactPerson if obj.contactPerson() is None else obj.contactPerson()
                dbObject.email = dbObject.email if obj.email() is None else obj.email()
                dbObject.phoneNumber = dbObject.phoneNumber if obj.phoneNumber() is None else obj.phoneNumber()
                dbObject.addressOne = dbObject.addressOne if obj.addressOne() is None else obj.addressOne()
                dbObject.addressTwo = dbObject.addressTwo if obj.addressTwo() is None else obj.addressTwo()
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def subcontractorById(self, id: str) -> Subcontractor:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbSSubcontractor).filter_by(id=id).first()
            if dbObject is None:
                raise SubcontractorDoesNotExistException(f'id = {id}')
            return self._subcontractorFromDbObject(dbObject=dbObject)
        finally:
            dbSession.close()

    @debugLogger
    def subcontractorByName(self, companyName: str) -> Subcontractor:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbSSubcontractor).filter_by(companyName=companyName).first()
            if dbObject is None:
                raise SubcontractorDoesNotExistException(f'companyName = {companyName}')
            return self._subcontractorFromDbObject(dbObject=dbObject)
        finally:
            dbSession.close()

    @debugLogger
    def subcontractors(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
                       order: List[dict] = None) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            sortData = ''
            if order is not None:
                for item in order:
                    sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
                sortData = sortData[2:]
            items = dbSession.query(DbSSubcontractor).order_by(text(sortData)).limit(resultSize).offset(
                resultFrom).all()
            itemsCount = dbSession.query(DbSSubcontractor).count()
            if items is None:
                return {"items": [], "itemCount": 0}
            return {"items": [self._subcontractorFromDbObject(x) for x in items],
                    "itemCount": itemsCount}
        finally:
            dbSession.close()

    @debugLogger
    def _subcontractorFromDbObject(self, dbObject: DbSSubcontractor):
        return Subcontractor(id=dbObject.id,
                             companyName=dbObject.companyName,
                             websiteUrl=dbObject.websiteUrl,
                             contactPerson=dbObject.contactPerson,
                             email=dbObject.email,
                             phoneNumber=dbObject.phoneNumber,
                             addressOne=dbObject.addressOne,
                             addressTwo=dbObject.addressTwo)
