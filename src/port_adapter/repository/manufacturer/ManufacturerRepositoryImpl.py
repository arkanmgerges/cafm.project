"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from src.domain_model.manufacturer.Manufacturer import Manufacturer
from src.domain_model.manufacturer.ManufacturerRepository import ManufacturerRepository
from src.domain_model.resource.exception.ObjectIdenticalException import ObjectIdenticalException
from src.domain_model.resource.exception.ManufacturerDoesNotExistException import ManufacturerDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.Manufacturer import Manufacturer as DbManufacturer
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class ManufacturerRepositoryImpl(ManufacturerRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}")
        except Exception as e:
            logger.warn(f'[{ManufacturerRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def save(self, obj: Manufacturer, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbManufacturer).filter_by(id=obj.id()).first()
            try:
                if dbObject is not None:
                    self.updateManufacturer(obj=obj, tokenData=tokenData)
                else:
                    self.createManufacturer(obj=obj, tokenData=tokenData)
            except Exception as e:
                logger.debug(e)
        finally:
            dbSession.close()

    @debugLogger
    def createManufacturer(self, obj: Manufacturer, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = DbManufacturer(id=obj.id(), name=obj.name())
            result = dbSession.query(DbManufacturer).filter_by(id=obj.id()).first()
            if result is None:
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteManufacturer(self, obj: Manufacturer, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbManufacturer).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateManufacturer(self, obj: Manufacturer, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbManufacturer).filter_by(id=obj.id()).first()
            if dbObject is None:
                raise ManufacturerDoesNotExistException(f'id = {obj.id()}')
            savedObj: Manufacturer = self.manufacturerById(obj.id())
            if savedObj == obj:
                logger.debug(
                    f'[{ManufacturerRepositoryImpl.updateManufacturer.__qualname__}] Object identical exception for old manufacturer: {savedObj}\nmanufacturer: {obj}')
                raise ObjectIdenticalException(f'manufacturer id: {obj.id()}')
            dbObject.name = obj.name() if obj.name() is not None else dbObject.name
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def manufacturerByName(self, name: str) -> Manufacturer:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbManufacturer).filter_by(name=name).first()
            if dbObject is None:
                raise ManufacturerDoesNotExistException(f'name = {name}')
            return Manufacturer(id=dbObject.id, name=dbObject.name)
        finally:
            dbSession.close()

    @debugLogger
    def manufacturerById(self, id: str) -> Manufacturer:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbManufacturer).filter_by(id=id).first()
            if dbObject is None:
                raise ManufacturerDoesNotExistException(f'id = {id}')
            return Manufacturer(id=dbObject.id, name=dbObject.name)
        finally:
            dbSession.close()

    @debugLogger
    def manufacturers(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
                 order: List[dict] = None) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            sortData = ''
            if order is not None:
                for item in order:
                    sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
                sortData = sortData[2:]
            items = dbSession.query(DbManufacturer).order_by(text(sortData)).limit(resultSize).offset(resultFrom).all()
            itemsCount = dbSession.query(DbManufacturer).count()
            if items is None:
                return {"items": [], "itemCount": 0}
            return {"items": [Manufacturer.createFrom(id=x.id, name=x.name) for x in items],
                    "itemCount": itemsCount}
        finally:
            dbSession.close()