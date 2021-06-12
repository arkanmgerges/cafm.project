"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import text

from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from src.domain_model.manufacturer.Manufacturer import Manufacturer
from src.domain_model.manufacturer.ManufacturerRepository import ManufacturerRepository
from src.domain_model.resource.exception.ManufacturerDoesNotExistException import (
    ManufacturerDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.db_model.Manufacturer import (
    Manufacturer as DbManufacturer,
)
from src.port_adapter.repository.resource.exception.IntegrityErrorRepositoryException import \
    IntegrityErrorRepositoryException
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class ManufacturerRepositoryImpl(ManufacturerRepository):
    

    @debugLogger
    def bulkSave(self, objList: List[Manufacturer], tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbManufacturer).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
            else:
                dbObject = self._createDbObjectByObj(obj=obj)
            dbSession.add(dbObject)

    @debugLogger
    def bulkDelete(
        self, objList: List[Manufacturer], tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbManufacturer).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)

    @debugLogger
    def save(self, obj: Manufacturer, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbManufacturer).filter_by(id=obj.id()).first()
        if dbObject is not None:
            self.updateManufacturer(obj=obj, dbObject=dbObject, tokenData=tokenData)
        else:
            self.createManufacturer(obj=obj, tokenData=tokenData)

    @debugLogger
    def createManufacturer(self, obj: Manufacturer, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = self._createDbObjectByObj(obj=obj)
        dbSession.add(dbObject)

    @debugLogger
    def deleteManufacturer(
        self, obj: Manufacturer, tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbManufacturer).filter_by(id=obj.id()).first()
        if dbObject is not None:
            dbSession.delete(dbObject)

    @debugLogger
    def updateManufacturer(
        self, obj: Manufacturer, dbObject: DbManufacturer = None, tokenData: TokenData = None
    ) -> None:
        from sqlalchemy import inspect
        dbSession = inspect(dbObject).session
        if dbObject is None:
            raise ManufacturerDoesNotExistException(f"id = {obj.id()}")
        dbSession.add(self._updateDbObjectByObj(dbObject=dbObject, obj=obj))

    @debugLogger
    def manufacturerByName(self, name: str) -> Manufacturer:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbManufacturer).filter_by(name=name).first()
        if dbObject is None:
            raise ManufacturerDoesNotExistException(f"name = {name}")
        return Manufacturer(id=dbObject.id, name=dbObject.name)

    @debugLogger
    def manufacturerById(self, id: str) -> Manufacturer:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbManufacturer).filter_by(id=id).first()
        if dbObject is None:
            raise ManufacturerDoesNotExistException(f"id = {id}")
        return Manufacturer(id=dbObject.id, name=dbObject.name)

    @debugLogger
    def manufacturers(
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
            dbSession.query(DbManufacturer)
            .order_by(text(sortData))
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = dbSession.query(DbManufacturer).count()
        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [Manufacturer.createFrom(id=x.id, name=x.name) for x in items],
            "totalItemCount": itemsCount,
        }

    def _updateDbObjectByObj(self, dbObject: DbManufacturer, obj: Manufacturer):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        return dbObject

    def _createDbObjectByObj(self, obj: Manufacturer):
        return DbManufacturer(id=obj.id(), name=obj.name())