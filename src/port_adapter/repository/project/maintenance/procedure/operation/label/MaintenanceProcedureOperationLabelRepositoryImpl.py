"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os
from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql.expression import text

from src.domain_model.project.maintenance.procedure.operation.label.MaintenanceProcedureOperationLabel import MaintenanceProcedureOperationLabel
from src.domain_model.project.maintenance.procedure.operation.label.MaintenanceProcedureOperationLabelRepository import MaintenanceProcedureOperationLabelRepository
from src.domain_model.resource.exception.MaintenanceProcedureOperationLabelDoesNotExistException import MaintenanceProcedureOperationLabelDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.db_model.MaintenanceProcedureOperationLabel import MaintenanceProcedureOperationLabel as DbMaintenanceProcedureOperationLabel
from src.port_adapter.repository.resource.exception.IntegrityErrorRepositoryException import \
    IntegrityErrorRepositoryException
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class MaintenanceProcedureOperationLabelRepositoryImpl(MaintenanceProcedureOperationLabelRepository):
    @debugLogger
    def save(self, obj: MaintenanceProcedureOperationLabel, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbMaintenanceProcedureOperationLabel).filter_by(id=obj.id()).first()
        if dbObject is not None:
            self.updateMaintenanceProcedureOperationLabel(obj=obj, dbObject=dbObject, tokenData=tokenData)
        else:
            self.createMaintenanceProcedureOperationLabel(obj=obj, tokenData=tokenData)

    @debugLogger
    def bulkSave(self, objList: List[MaintenanceProcedureOperationLabel], tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbMaintenanceProcedureOperationLabel).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
            else:
                dbObject = self._createDbObjectByObj(obj=obj)
            dbSession.add(dbObject)

    @debugLogger
    def bulkDelete(
        self, objList: List[MaintenanceProcedureOperationLabel], tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbMaintenanceProcedureOperationLabel).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)

    @debugLogger
    def createMaintenanceProcedureOperationLabel(self, obj: MaintenanceProcedureOperationLabel, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = self._createDbObjectByObj(obj=obj)
        dbSession.add(dbObject)

    @debugLogger
    def deleteMaintenanceProcedureOperationLabel(self, obj: MaintenanceProcedureOperationLabel, tokenData: TokenData = None) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbMaintenanceProcedureOperationLabel).filter_by(id=obj.id()).first()
        if dbObject is not None:
            dbSession.delete(dbObject)

    @debugLogger
    def updateMaintenanceProcedureOperationLabel(self, obj: MaintenanceProcedureOperationLabel, dbObject: DbMaintenanceProcedureOperationLabel = None, tokenData: TokenData = None) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        if dbObject is None:
            raise MaintenanceProcedureOperationLabelDoesNotExistException(f'id = {obj.id()}')
        dbSession.add(self._updateDbObjectByObj(dbObject=dbObject, obj=obj))

    @debugLogger
    def maintenanceProcedureOperationLabelById(self, id: str) -> MaintenanceProcedureOperationLabel:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbMaintenanceProcedureOperationLabel).filter_by(id=id).first()
        if dbObject is None:
            raise MaintenanceProcedureOperationLabelDoesNotExistException(f'id = {id}')
        return MaintenanceProcedureOperationLabel.createFrom(id=dbObject.id,
			label=dbObject.label,
			generateAlert=dbObject.generateAlert,
			maintenanceProcedureOperationId=dbObject.maintenanceProcedureOperationId)

    @debugLogger
    def maintenanceProcedureOperationLabels(self, resultFrom: int = 0, resultSize: int = 100, order: List[dict] = None, tokenData: TokenData = None) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        sortData = ''
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]
        items = dbSession.query(DbMaintenanceProcedureOperationLabel).order_by(text(sortData)).limit(resultSize).offset(resultFrom).all()
        itemsCount = dbSession.query(DbMaintenanceProcedureOperationLabel).count()
        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {"items": [MaintenanceProcedureOperationLabel.createFrom(id=x.id,
			label=x.label,
			generateAlert=x.generateAlert,
			maintenanceProcedureOperationId=x.maintenanceProcedureOperationId) for x in items],
                "totalItemCount": itemsCount}

    def _updateDbObjectByObj(self, dbObject: DbMaintenanceProcedureOperationLabel, obj: MaintenanceProcedureOperationLabel):
        dbObject.label = obj.label() if obj.label() is not None else dbObject.label
        dbObject.generateAlert = obj.generateAlert() if obj.generateAlert() is not None else dbObject.generateAlert
        dbObject.maintenanceProcedureOperationId = obj.maintenanceProcedureOperationId() if obj.maintenanceProcedureOperationId() is not None else dbObject.maintenanceProcedureOperationId
        return dbObject

    def _createDbObjectByObj(self, obj: MaintenanceProcedureOperationLabel):
        return DbMaintenanceProcedureOperationLabel(id=obj.id(),
			label=obj.label(),
			generateAlert=obj.generateAlert(),
			maintenanceProcedureOperationId=obj.maintenanceProcedureOperationId())