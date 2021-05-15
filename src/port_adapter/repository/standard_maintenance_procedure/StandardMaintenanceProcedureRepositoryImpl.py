"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os
from datetime import datetime
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedure import (
    StandardMaintenanceProcedure,
)
from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedureRepository import (
    StandardMaintenanceProcedureRepository,
)
from src.domain_model.resource.exception.ObjectIdenticalException import (
    ObjectIdenticalException,
)
from src.domain_model.resource.exception.StandardMaintenanceProcedureDoesNotExistException import (
    StandardMaintenanceProcedureDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.StandardMaintenanceProcedure import (
    StandardMaintenanceProcedure as DbStandardMaintenanceProcedure,
)
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class StandardMaintenanceProcedureRepositoryImpl(
    StandardMaintenanceProcedureRepository
):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}"
            )
        except Exception as e:
            logger.warn(
                f"[{StandardMaintenanceProcedureRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def save(self, obj: StandardMaintenanceProcedure, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = (
                dbSession.query(DbStandardMaintenanceProcedure)
                .filter_by(id=obj.id())
                .first()
            )
            if dbObject is not None:
                self.updateStandardMaintenanceProcedure(obj=obj, dbObject=dbObject, tokenData=tokenData)
            else:
                self.createStandardMaintenanceProcedure(obj=obj, tokenData=tokenData)
        finally:
            dbSession.close()

    @debugLogger
    def createStandardMaintenanceProcedure(
        self, obj: StandardMaintenanceProcedure, tokenData: TokenData = None
    ):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = self._createDbObjectByObj(obj=obj)
            result = (
                dbSession.query(DbStandardMaintenanceProcedure)
                .filter_by(id=obj.id())
                .first()
            )
            if result is None:
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteStandardMaintenanceProcedure(
        self, obj: StandardMaintenanceProcedure, tokenData: TokenData = None
    ) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = (
                dbSession.query(DbStandardMaintenanceProcedure)
                .filter_by(id=obj.id())
                .first()
            )
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateStandardMaintenanceProcedure(
        self, obj: StandardMaintenanceProcedure, dbObject: DbStandardMaintenanceProcedure = None,
            tokenData: TokenData = None
    ) -> None:
        from sqlalchemy import inspect
        dbSession = inspect(dbObject).session
        if dbObject is None:
            raise StandardMaintenanceProcedureDoesNotExistException(
                f"id = {obj.id()}"
            )
        dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
        dbSession.add(dbObject)
        dbSession.commit()

    @debugLogger
    def bulkSave(self, objList: List[StandardMaintenanceProcedure], tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            for obj in objList:
                dbObject = dbSession.query(DbStandardMaintenanceProcedure).filter_by(id=obj.id()).first()
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
            self, objList: List[StandardMaintenanceProcedure], tokenData: TokenData = None
    ) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            for obj in objList:
                dbObject = dbSession.query(DbStandardMaintenanceProcedure).filter_by(id=obj.id()).first()
                if dbObject is not None:
                    dbSession.delete(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def standardMaintenanceProcedureById(self, id: str) -> StandardMaintenanceProcedure:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = (
                dbSession.query(DbStandardMaintenanceProcedure).filter_by(id=id).first()
            )
            if dbObject is None:
                raise StandardMaintenanceProcedureDoesNotExistException(f"id = {id}")
            return StandardMaintenanceProcedure.createFrom(
                id=dbObject.id,
                name=dbObject.name,
                type=dbObject.type,
                subtype=dbObject.subtype,
                frequency=dbObject.frequency,
                startDate=DateTimeHelper.datetimeToInt(dbObject.startDate)
                if DateTimeHelper.datetimeToInt(dbObject.startDate) is not None
                else 0,
                organizationId=dbObject.organizationId,
                standardEquipmentCategoryGroupId=dbObject.standardEquipmentCategoryGroupId,
            )
        finally:
            dbSession.close()

    @debugLogger
    def standardMaintenanceProcedures(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        tokenData: TokenData = None,
    ) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            sortData = ""
            if order is not None:
                for item in order:
                    sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
                sortData = sortData[2:]
            items = (
                dbSession.query(DbStandardMaintenanceProcedure)
                .order_by(text(sortData))
                .limit(resultSize)
                .offset(resultFrom)
                .all()
            )
            itemsCount = dbSession.query(DbStandardMaintenanceProcedure).count()
            if items is None:
                return {"items": [], "totalItemCount": 0}
            return {
                "items": [
                    StandardMaintenanceProcedure.createFrom(
                        id=x.id,
                        name=x.name,
                        type=x.type,
                        subtype=x.subtype,
                        frequency=x.frequency,
                        startDate=DateTimeHelper.datetimeToInt(x.startDate)
                        if DateTimeHelper.datetimeToInt(x.startDate) is not None
                        else 0,
                        organizationId=x.organizationId,
                        standardEquipmentCategoryGroupId=x.standardEquipmentCategoryGroupId,
                    )
                    for x in items
                ],
                "totalItemCount": itemsCount,
            }
        finally:
            dbSession.close()

    def _updateDbObjectByObj(self, dbObject: DbStandardMaintenanceProcedure, obj: StandardMaintenanceProcedure):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        dbObject.type = obj.type() if obj.type() is not None else dbObject.type
        dbObject.subtype = obj.subtype() if obj.subtype() is not None else dbObject.subtype
        dbObject.frequency = obj.frequency() if obj.frequency() is not None else dbObject.frequency
        dbObject.startDate = DateTimeHelper.intToDateTime(obj.startDate()) if obj.startDate() is not None and obj.startDate() > 0 else dbObject.startDate
        dbObject.organizationId = obj.organizationId() if obj.organizationId() is not None else dbObject.organizationId
        dbObject.standardEquipmentCategoryGroupId = obj.standardEquipmentCategoryGroupId() if obj.standardEquipmentCategoryGroupId() is not None else dbObject.standardEquipmentCategoryGroupId
        return dbObject

    def _createDbObjectByObj(self, obj: StandardMaintenanceProcedure):
        return DbStandardMaintenanceProcedure(id=obj.id(), name=obj.name(),
                                          type=obj.type(),
                                          subtype=obj.subtype(),
                                          frequency=obj.frequency(),
                                          startDate=DateTimeHelper.intToDateTime(obj.startDate()) if obj.startDate() > 0 else None,
                                          organizationId=obj.organizationId(),
                                          standardEquipmentCategoryGroupId=obj.standardEquipmentCategoryGroupId())
