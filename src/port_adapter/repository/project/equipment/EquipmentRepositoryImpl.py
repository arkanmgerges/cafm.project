"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from sqlalchemy.sql.expression import text

from src.application.lifecycle.ApplicationServiceLifeCycle import ApplicationServiceLifeCycle
from src.domain_model.project.equipment.Equipment import Equipment
from src.domain_model.project.equipment.EquipmentRepository import EquipmentRepository
from src.domain_model.resource.exception.EquipmentDoesNotExistException import (
    EquipmentDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.db_model.Equipment import Equipment as DbEquipment
from src.resource.logging.decorator import debugLogger


class EquipmentRepositoryImpl(EquipmentRepository):
    @debugLogger
    def save(self, obj: Equipment, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbEquipment).filter_by(id=obj.id()).first()
        if dbObject is not None:
            self.updateEquipment(obj=obj, dbObject=dbObject, tokenData=tokenData)
        else:
            self.createEquipment(obj=obj, tokenData=tokenData)

    @debugLogger
    def createEquipment(self, obj: Equipment, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = self._createDbObjectByObj(obj=obj)
        result = dbSession.query(DbEquipment).filter_by(id=obj.id()).first()
        if result is None:
            dbSession.add(dbObject)
    

    @debugLogger
    def deleteEquipment(self, obj: Equipment, tokenData: TokenData = None) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbEquipment).filter_by(id=obj.id()).first()
        if dbObject is not None:
            dbSession.delete(dbObject)
    

    @debugLogger
    def updateEquipment(self, obj: Equipment, dbObject: DbEquipment = None, tokenData: TokenData = None) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        if dbObject is None:
            raise EquipmentDoesNotExistException(f"id = {obj.id()}")
        dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
        dbSession.add(dbObject)

    @debugLogger
    def bulkSave(self, objList: List[Equipment], tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbEquipment).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
            else:
                dbObject = self._createDbObjectByObj(obj=obj)
            dbSession.add(dbObject)


    @debugLogger
    def bulkDelete(
            self, objList: List[Equipment], tokenData: TokenData = None
    ) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        for obj in objList:
            dbObject = dbSession.query(DbEquipment).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)


    @debugLogger
    def equipmentById(self, id: str) -> Equipment:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbObject = dbSession.query(DbEquipment).filter_by(id=id).first()
        if dbObject is None:
            raise EquipmentDoesNotExistException(f"id = {id}")
        return Equipment.createFrom(
            id=dbObject.id,
            name=dbObject.name,
            projectId=dbObject.projectId,
            manufacturerId=dbObject.manufacturerId,
            equipmentModelId=dbObject.equipmentModelId,
            equipmentProjectCategoryId=dbObject.equipmentProjectCategoryId,
            equipmentCategoryId=dbObject.equipmentCategoryId,
            equipmentCategoryGroupId=dbObject.equipmentCategoryGroupId,
            buildingId=dbObject.buildingId,
            buildingLevelId=dbObject.buildingLevelId,
            buildingLevelRoomId=dbObject.buildingLevelRoomId,
            quantity=dbObject.quantity,
        )

    @debugLogger
    def equipments(
        self,
        tokenData: TokenData = None,
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
            dbSession.query(DbEquipment)
            .order_by(text(sortData))
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = dbSession.query(DbEquipment).count()
        if items is None:
            return {"items": [], "totalItemCount": 0}
        return {
            "items": [
                Equipment.createFrom(
                    id=x.id,
                    name=x.name,
                    projectId=x.projectId,
                    manufacturerId=x.manufacturerId,
                    equipmentModelId=x.equipmentModelId,
                    equipmentProjectCategoryId=x.equipmentProjectCategoryId,
                    equipmentCategoryId=x.equipmentCategoryId,
                    equipmentCategoryGroupId=x.equipmentCategoryGroupId,
                    buildingId=x.buildingId,
                    buildingLevelId=x.buildingLevelId,
                    buildingLevelRoomId=x.buildingLevelRoomId,
                    quantity=x.quantity,
                )
                for x in items
            ],
            "totalItemCount": itemsCount,
        }

    def _updateDbObjectByObj(self, dbObject: DbEquipment, obj: Equipment):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        dbObject.projectId = obj.projectId() if obj.projectId() is not None else dbObject.projectId
        dbObject.manufacturerId = obj.manufacturerId() if obj.manufacturerId() is not None else dbObject.manufacturerId
        dbObject.equipmentModelId = obj.equipmentModelId() if obj.equipmentModelId() is not None else dbObject.equipmentModelId
        dbObject.equipmentProjectCategoryId = obj.equipmentProjectCategoryId() if obj.equipmentProjectCategoryId() is not None else dbObject.equipmentProjectCategoryId
        dbObject.equipmentCategoryId = obj.equipmentCategoryId() if obj.equipmentCategoryId() is not None else dbObject.equipmentCategoryId
        dbObject.equipmentCategoryGroupId = obj.equipmentCategoryGroupId() if obj.equipmentCategoryGroupId() is not None else dbObject.equipmentCategoryGroupId
        dbObject.buildingId = obj.buildingId() if obj.buildingId() is not None else dbObject.buildingId
        dbObject.buildingLevelId = obj.buildingLevelId() if obj.buildingLevelId() is not None else dbObject.buildingLevelId
        dbObject.buildingLevelRoomId = obj.buildingLevelRoomId() if obj.buildingLevelRoomId() is not None else dbObject.buildingLevelRoomId
        dbObject.quantity = obj.quantity() if obj.quantity() is not None else dbObject.quantity
        return dbObject


    def _createDbObjectByObj(self, obj: Equipment):
        return DbEquipment(id=obj.id(), name=obj.name(),
                       projectId=obj.projectId(),
                       manufacturerId=obj.manufacturerId(),
                       equipmentModelId=obj.equipmentModelId(),
                       equipmentProjectCategoryId=obj.equipmentProjectCategoryId(),
                       equipmentCategoryId=obj.equipmentCategoryId(),
                       equipmentCategoryGroupId=obj.equipmentCategoryGroupId(),
                       buildingId=obj.buildingId(),
                       buildingLevelId=obj.buildingLevelId(),
                       buildingLevelRoomId=obj.buildingLevelRoomId(),
                       quantity=obj.quantity())