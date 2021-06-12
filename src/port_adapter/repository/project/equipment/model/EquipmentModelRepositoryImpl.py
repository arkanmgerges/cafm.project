"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from sqlalchemy.sql.expression import text

from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from src.domain_model.project.equipment.model.EquipmentModel import EquipmentModel
from src.domain_model.project.equipment.model.EquipmentModelRepository import (
    EquipmentModelRepository,
)
from src.domain_model.resource.exception.EquipmentModelDoesNotExistException import (
    EquipmentModelDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.db_model.EquipmentModel import (
    EquipmentModel as DbEquipmentModel,
)
from src.resource.logging.decorator import debugLogger


class EquipmentModelRepositoryImpl(EquipmentModelRepository):
    @debugLogger
    def save(self, obj: EquipmentModel, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbEquipmentModel).filter_by(id=obj.id()).first()
        if dbObject is not None:
            self.updateEquipmentModel(obj=obj, dbObject=dbObject, tokenData=tokenData)
        else:
            self.createEquipmentModel(obj=obj, tokenData=tokenData)

    @debugLogger
    def createEquipmentModel(self, obj: EquipmentModel, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = DbEquipmentModel(id=obj.id(), name=obj.name())
        result = dbSession.query(DbEquipmentModel).filter_by(id=obj.id()).first()
        if result is None:
            dbSession.add(dbObject)
    

    @debugLogger
    def deleteEquipmentModel(
        self, obj: EquipmentModel, tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbEquipmentModel).filter_by(id=obj.id()).first()
        if dbObject is not None:
            dbSession.delete(dbObject)
    

    @debugLogger
    def updateEquipmentModel(
        self, obj: EquipmentModel, dbObject: DbEquipmentModel = None, tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        if dbObject is None:
            raise EquipmentModelDoesNotExistException(f"id = {obj.id()}")
        dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
        dbSession.add(dbObject)

    @debugLogger
    def bulkSave(self, objList: List[EquipmentModel], tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbEquipmentModel).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
            else:
                dbObject = self._createDbObjectByObj(obj=obj)
            dbSession.add(dbObject)

    @debugLogger
    def bulkDelete(
            self, objList: List[EquipmentModel], tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbEquipmentModel).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)

    @debugLogger
    def equipmentModelByName(self, name: str) -> EquipmentModel:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbEquipmentModel).filter_by(name=name).first()
        if dbObject is None:
            raise EquipmentModelDoesNotExistException(f"name = {name}")
        return EquipmentModel(id=dbObject.id, name=dbObject.name)

    @debugLogger
    def equipmentModelById(self, id: str) -> EquipmentModel:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbEquipmentModel).filter_by(id=id).first()
        if dbObject is None:
            raise EquipmentModelDoesNotExistException(f"id = {id}")
        return EquipmentModel(id=dbObject.id, name=dbObject.name)

    @debugLogger
    def equipmentModels(
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
            dbSession.query(DbEquipmentModel)
            .order_by(text(sortData))
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = dbSession.query(DbEquipmentModel).count()
        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [
                EquipmentModel.createFrom(id=x.id, name=x.name) for x in items
            ],
            "totalItemCount": itemsCount,
        }

    def _updateDbObjectByObj(self, dbObject: DbEquipmentModel, obj: EquipmentModel):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        return dbObject

    def _createDbObjectByObj(self, obj: EquipmentModel):
        return DbEquipmentModel(id=obj.id(), name=obj.name())