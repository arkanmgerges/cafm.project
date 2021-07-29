"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.port_adapter.repository.common.DbUtil import DbUtil
from typing import List

from sqlalchemy.sql.expression import text

from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from src.domain_model.project.maintenance.procedure.operation.MaintenanceProcedureOperation import (
    MaintenanceProcedureOperation,
)
from src.domain_model.project.maintenance.procedure.operation.MaintenanceProcedureOperationRepository import (
    MaintenanceProcedureOperationRepository,
)
from src.domain_model.resource.exception.MaintenanceProcedureOperationDoesNotExistException import (
    MaintenanceProcedureOperationDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.db_model.MaintenanceProcedureOperation import (
    MaintenanceProcedureOperation as DbMaintenanceProcedureOperation,
)
from src.resource.logging.decorator import debugLogger


class MaintenanceProcedureOperationRepositoryImpl(MaintenanceProcedureOperationRepository):
    @debugLogger
    def save(self, obj: MaintenanceProcedureOperation, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbMaintenanceProcedureOperation).filter_by(id=obj.id()).first()
        if dbObject is not None:
            self.updateMaintenanceProcedureOperation(obj=obj, dbObject=dbObject, tokenData=tokenData)
        else:
            self.createMaintenanceProcedureOperation(obj=obj, tokenData=tokenData)

    @debugLogger
    def createMaintenanceProcedureOperation(self, obj: MaintenanceProcedureOperation, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = self._createDbObjectByObj(obj=obj)
        result = dbSession.query(DbMaintenanceProcedureOperation).filter_by(id=obj.id()).first()
        if result is None:
            dbSession.add(dbObject)

    @debugLogger
    def deleteMaintenanceProcedureOperation(
        self, obj: MaintenanceProcedureOperation, tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbMaintenanceProcedureOperation).filter_by(id=obj.id()).first()
        if dbObject is not None:
            dbSession.execute(text(f'''
                            DELETE FROM maintenance_procedure_operation WHERE id="{obj.id()}"
                            '''))
            # dbSession.delete(dbObject)
            DbUtil.enableForeignKeyChecks(dbSession=dbSession)

    @debugLogger
    def updateMaintenanceProcedureOperation(
        self,
        obj: MaintenanceProcedureOperation,
        dbObject: DbMaintenanceProcedureOperation = None,
        tokenData: TokenData = None,
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        if dbObject is None:
            raise MaintenanceProcedureOperationDoesNotExistException(f"id = {obj.id()}")
        dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
        dbSession.add(dbObject)

    @debugLogger
    def bulkSave(self, objList: List[MaintenanceProcedureOperation], tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbMaintenanceProcedureOperation).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
            else:
                dbObject = self._createDbObjectByObj(obj=obj)
            dbSession.add(dbObject)

    @debugLogger
    def bulkDelete(self, objList: List[MaintenanceProcedureOperation], tokenData: TokenData = None) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbMaintenanceProcedureOperation).filter_by(id=obj.id()).first()
            if dbObject is not None:
                DbUtil.disableForeignKeyChecks(dbSession=dbSession)
                dbSession.execute(text(f'''
                                DELETE FROM maintenance_procedure_operation WHERE id="{obj.id()}"
                                '''))
                # dbSession.delete(dbObject)
                DbUtil.enableForeignKeyChecks(dbSession=dbSession)

    def _updateDbObjectByObj(self, dbObject: DbMaintenanceProcedureOperation, obj: MaintenanceProcedureOperation):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        dbObject.description = obj.description() if obj.description() is not None else dbObject.description
        dbObject.type = obj.type() if obj.type() is not None else dbObject.type
        dbObject.maintenanceProcedureId = (
            obj.maintenanceProcedureId()
            if obj.maintenanceProcedureId() is not None
            else dbObject.maintenanceProcedureId
        )
        return dbObject

    def _createDbObjectByObj(self, obj: MaintenanceProcedureOperation):
        return DbMaintenanceProcedureOperation(
            id=obj.id(),
            name=obj.name(),
            description=obj.description(),
            type=obj.type(),
            maintenanceProcedureId=obj.maintenanceProcedureId(),
        )

    @debugLogger
    def maintenanceProcedureOperationById(self, id: str) -> MaintenanceProcedureOperation:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbMaintenanceProcedureOperation).filter_by(id=id).first()
        if dbObject is None:
            raise MaintenanceProcedureOperationDoesNotExistException(f"id = {id}")
        return MaintenanceProcedureOperation.createFrom(
            id=dbObject.id,
            name=dbObject.name,
            description=dbObject.description,
            type=dbObject.type,
            maintenanceProcedureId=dbObject.maintenanceProcedureId,
        )

    @debugLogger
    def maintenanceProcedureOperations(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        tokenData: TokenData = None,
    ) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        sortData = ""
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]
        items = (
            dbSession.query(DbMaintenanceProcedureOperation)
            .order_by(text(sortData))
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = dbSession.query(DbMaintenanceProcedureOperation).count()
        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [
                MaintenanceProcedureOperation.createFrom(
                    id=x.id,
                    name=x.name,
                    description=x.description,
                    type=x.type,
                    maintenanceProcedureId=x.maintenanceProcedureId,
                )
                for x in items
            ],
            "totalItemCount": itemsCount,
        }

    @debugLogger
    def maintenanceProcedureOperationsByMaintenanceProcedureId(
        self,
        maintenanceProcedureId: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        tokenData: TokenData = None,
    ) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        sortData = ""
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]
        items = (
            dbSession.query(DbMaintenanceProcedureOperation)
            .filter_by(maintenanceProcedureId=maintenanceProcedureId)
            .order_by(text(sortData))
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = (
            dbSession.query(DbMaintenanceProcedureOperation)
            .filter_by(maintenanceProcedureId=maintenanceProcedureId)
            .count()
        )
        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [
                MaintenanceProcedureOperation.createFrom(
                    id=x.id,
                    name=x.name,
                    description=x.description,
                    type=x.type,
                    maintenanceProcedureId=x.maintenanceProcedureId,
                )
                for x in items
            ],
            "totalItemCount": itemsCount,
        }
