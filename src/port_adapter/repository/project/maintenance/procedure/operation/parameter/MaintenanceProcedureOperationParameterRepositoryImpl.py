"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from src.domain_model.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameter import (
    MaintenanceProcedureOperationParameter,
)
from src.domain_model.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameterRepository import (
    MaintenanceProcedureOperationParameterRepository,
)
from src.domain_model.resource.exception.ObjectIdenticalException import (
    ObjectIdenticalException,
)
from src.domain_model.resource.exception.MaintenanceProcedureOperationParameterDoesNotExistException import (
    MaintenanceProcedureOperationParameterDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.MaintenanceProcedureOperationParameter import (
    MaintenanceProcedureOperationParameter as DbMaintenanceProcedureOperationParameter,
)
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class MaintenanceProcedureOperationParameterRepositoryImpl(
    MaintenanceProcedureOperationParameterRepository
):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}"
            )
        except Exception as e:
            logger.warn(
                f"[{MaintenanceProcedureOperationParameterRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def save(
        self, obj: MaintenanceProcedureOperationParameter, tokenData: TokenData = None
    ):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = (
                dbSession.query(DbMaintenanceProcedureOperationParameter)
                .filter_by(id=obj.id())
                .first()
            )
            if dbObject is not None:
                self.updateMaintenanceProcedureOperationParameter(
                    obj=obj, dbObject=dbObject, tokenData=tokenData
                )
            else:
                self.createMaintenanceProcedureOperationParameter(
                    obj=obj, tokenData=tokenData
                )
        finally:
            dbSession.close()

    @debugLogger
    def createMaintenanceProcedureOperationParameter(
        self, obj: MaintenanceProcedureOperationParameter, tokenData: TokenData = None
    ):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = self._createDbObjectByObj(obj=obj)
            result = (
                dbSession.query(DbMaintenanceProcedureOperationParameter)
                .filter_by(id=obj.id())
                .first()
            )
            if result is None:
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteMaintenanceProcedureOperationParameter(
        self, obj: MaintenanceProcedureOperationParameter, tokenData: TokenData = None
    ) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = (
                dbSession.query(DbMaintenanceProcedureOperationParameter)
                .filter_by(id=obj.id())
                .first()
            )
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateMaintenanceProcedureOperationParameter(
        self, obj: MaintenanceProcedureOperationParameter, dbObject: MaintenanceProcedureOperationParameter = None, tokenData: TokenData = None
    ) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            if dbObject is None:
                raise MaintenanceProcedureOperationParameterDoesNotExistException(
                    f"id = {obj.id()}"
                )
            dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def bulkSave(self, objList: List[MaintenanceProcedureOperationParameter], tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            for obj in objList:
                dbObject = dbSession.query(DbMaintenanceProcedureOperationParameter).filter_by(id=obj.id()).first()
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
            self, objList: List[MaintenanceProcedureOperationParameter], tokenData: TokenData = None
    ) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            for obj in objList:
                dbObject = dbSession.query(DbMaintenanceProcedureOperationParameter).filter_by(id=obj.id()).first()
                if dbObject is not None:
                    dbSession.delete(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def maintenanceProcedureOperationParameterById(
        self, id: str
    ) -> MaintenanceProcedureOperationParameter:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = (
                dbSession.query(DbMaintenanceProcedureOperationParameter)
                .filter_by(id=id)
                .first()
            )
            if dbObject is None:
                raise MaintenanceProcedureOperationParameterDoesNotExistException(
                    f"id = {id}"
                )
            return MaintenanceProcedureOperationParameter.createFrom(
                id=dbObject.id,
                name=dbObject.name,
                unitId=dbObject.unitId,
                maintenanceProcedureOperationId=dbObject.maintenanceProcedureOperationId,
                minValue=dbObject.minValue,
                maxValue=dbObject.maxValue,
            )
        finally:
            dbSession.close()

    @debugLogger
    def maintenanceProcedureOperationParameters(
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
                dbSession.query(DbMaintenanceProcedureOperationParameter)
                .order_by(text(sortData))
                .limit(resultSize)
                .offset(resultFrom)
                .all()
            )
            itemsCount = dbSession.query(
                DbMaintenanceProcedureOperationParameter
            ).count()
            if items is None:
                return {"items": [], "itemCount": 0}
            return {
                "items": [
                    MaintenanceProcedureOperationParameter.createFrom(
                        id=x.id,
                        name=x.name,
                        unitId=x.unitId,
                        maintenanceProcedureOperationId=x.maintenanceProcedureOperationId,
                        minValue=x.minValue,
                        maxValue=x.maxValue,
                    )
                    for x in items
                ],
                "itemCount": itemsCount,
            }
        finally:
            dbSession.close()

    @debugLogger
    def maintenanceProcedureOperationParametersByMaintenanceProcedureOperationId(
        self,
        maintenanceProcedureOperationId: str = None,
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
                dbSession.query(DbMaintenanceProcedureOperationParameter)
                .filter_by(
                    maintenanceProcedureOperationId=maintenanceProcedureOperationId
                )
                .order_by(text(sortData))
                .limit(resultSize)
                .offset(resultFrom)
                .all()
            )
            itemsCount = (
                dbSession.query(DbMaintenanceProcedureOperationParameter)
                .filter_by(
                    maintenanceProcedureOperationId=maintenanceProcedureOperationId
                )
                .count()
            )
            if items is None:
                return {"items": [], "itemCount": 0}
            return {
                "items": [
                    MaintenanceProcedureOperationParameter.createFrom(
                        id=x.id,
                        name=x.name,
                        unitId=x.unitId,
                        maintenanceProcedureOperationId=x.maintenanceProcedureOperationId,
                        minValue=x.minValue,
                        maxValue=x.maxValue,
                    )
                    for x in items
                ],
                "itemCount": itemsCount,
            }
        finally:
            dbSession.close()

    def _updateDbObjectByObj(self, dbObject: DbMaintenanceProcedureOperationParameter,
                             obj: MaintenanceProcedureOperationParameter):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        dbObject.unitId = obj.unitId() if obj.unitId() is not None else dbObject.unitId
        dbObject.maintenanceProcedureOperationId = obj.maintenanceProcedureOperationId() if obj.maintenanceProcedureOperationId() is not None else dbObject.maintenanceProcedureOperationId
        dbObject.minValue = obj.minValue() if obj.minValue() is not None else dbObject.minValue
        dbObject.maxValue = obj.maxValue() if obj.maxValue() is not None else dbObject.maxValue
        return dbObject


    def _createDbObjectByObj(self, obj: MaintenanceProcedureOperationParameter):
        return DbMaintenanceProcedureOperationParameter(id=obj.id(), name=obj.name(),
                                                    unitId=obj.unitId(),
                                                    maintenanceProcedureOperationId=obj.maintenanceProcedureOperationId(),
                                                    minValue=obj.minValue(),
                                                    maxValue=obj.maxValue())
