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

from src.domain_model.project.daily_check.procedure.operation.label.DailyCheckProcedureOperationLabel import DailyCheckProcedureOperationLabel
from src.domain_model.project.daily_check.procedure.operation.label.DailyCheckProcedureOperationLabelRepository import DailyCheckProcedureOperationLabelRepository
from src.domain_model.resource.exception.DailyCheckProcedureOperationLabelDoesNotExistException import DailyCheckProcedureOperationLabelDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.db_model.DailyCheckProcedureOperationLabel import DailyCheckProcedureOperationLabel as DbDailyCheckProcedureOperationLabel
from src.port_adapter.repository.resource.exception.IntegrityErrorRepositoryException import \
    IntegrityErrorRepositoryException
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class DailyCheckProcedureOperationLabelRepositoryImpl(DailyCheckProcedureOperationLabelRepository):
    @debugLogger
    def save(self, obj: DailyCheckProcedureOperationLabel, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbDailyCheckProcedureOperationLabel).filter_by(id=obj.id()).first()
        if dbObject is not None:
            self.updateDailyCheckProcedureOperationLabel(obj=obj, dbObject=dbObject, tokenData=tokenData)
        else:
            self.createDailyCheckProcedureOperationLabel(obj=obj, tokenData=tokenData)

    @debugLogger
    def bulkSave(self, objList: List[DailyCheckProcedureOperationLabel], tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbDailyCheckProcedureOperationLabel).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
            else:
                dbObject = self._createDbObjectByObj(obj=obj)
            dbSession.add(dbObject)

    @debugLogger
    def bulkDelete(
        self, objList: List[DailyCheckProcedureOperationLabel], tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbDailyCheckProcedureOperationLabel).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)

    @debugLogger
    def createDailyCheckProcedureOperationLabel(self, obj: DailyCheckProcedureOperationLabel, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = self._createDbObjectByObj(obj=obj)
        dbSession.add(dbObject)

    @debugLogger
    def deleteDailyCheckProcedureOperationLabel(self, obj: DailyCheckProcedureOperationLabel, tokenData: TokenData = None) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbDailyCheckProcedureOperationLabel).filter_by(id=obj.id()).first()
        if dbObject is not None:
            dbSession.delete(dbObject)

    @debugLogger
    def updateDailyCheckProcedureOperationLabel(self, obj: DailyCheckProcedureOperationLabel, dbObject: DbDailyCheckProcedureOperationLabel = None, tokenData: TokenData = None) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        if dbObject is None:
            raise DailyCheckProcedureOperationLabelDoesNotExistException(f'id = {obj.id()}')
        dbSession.add(self._updateDbObjectByObj(dbObject=dbObject, obj=obj))

    @debugLogger
    def dailyCheckProcedureOperationLabelById(self, id: str) -> DailyCheckProcedureOperationLabel:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbDailyCheckProcedureOperationLabel).filter_by(id=id).first()
        if dbObject is None:
            raise DailyCheckProcedureOperationLabelDoesNotExistException(f'id = {id}')
        return DailyCheckProcedureOperationLabel.createFrom(id=dbObject.id,
			label=dbObject.label,
			generateAlert=dbObject.generateAlert,
			dailyCheckProcedureOperationId=dbObject.dailyCheckProcedureOperationId)

    @debugLogger
    def dailyCheckProcedureOperationLabels(self, resultFrom: int = 0, resultSize: int = 100, order: List[dict] = None, tokenData: TokenData = None) -> dict:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        sortData = ''
        if order is not None:
            for item in order:
                sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
            sortData = sortData[2:]
        items = dbSession.query(DbDailyCheckProcedureOperationLabel).order_by(text(sortData)).limit(resultSize).offset(resultFrom).all()
        itemsCount = dbSession.query(DbDailyCheckProcedureOperationLabel).count()
        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {"items": [DailyCheckProcedureOperationLabel.createFrom(id=x.id,
			label=x.label,
			generateAlert=x.generateAlert,
			dailyCheckProcedureOperationId=x.dailyCheckProcedureOperationId) for x in items],
                "totalItemCount": itemsCount}

    @debugLogger
    def dailyCheckProcedureOperationLabelsByDailyCheckProcedureOperationId(self, dailyCheckProcedureOperationId: str, tokenData: TokenData = None) -> list:
        dbSession = ApplicationServiceLifeCycle.dbContext()

        items = dbSession.query(DbDailyCheckProcedureOperationLabel).filter_by(dailyCheckProcedureOperationId=dailyCheckProcedureOperationId).all()

        if items is None:
            return []

        return [DailyCheckProcedureOperationLabel.createFrom(id=x.id,
			label=x.label,
			generateAlert=x.generateAlert,
			dailyCheckProcedureOperationId=x.dailyCheckProcedureOperationId) for x in items]

    def _updateDbObjectByObj(self, dbObject: DbDailyCheckProcedureOperationLabel, obj: DailyCheckProcedureOperationLabel):
        dbObject.label = obj.label() if obj.label() is not None else dbObject.label
        dbObject.generateAlert = obj.generateAlert() if obj.generateAlert() is not None else dbObject.generateAlert
        dbObject.dailyCheckProcedureOperationId = obj.dailyCheckProcedureOperationId() if obj.dailyCheckProcedureOperationId() is not None else dbObject.dailyCheckProcedureOperationId
        return dbObject

    def _createDbObjectByObj(self, obj: DailyCheckProcedureOperationLabel):
        return DbDailyCheckProcedureOperationLabel(id=obj.id(),
			label=obj.label(),
			generateAlert=obj.generateAlert(),
			dailyCheckProcedureOperationId=obj.dailyCheckProcedureOperationId())
