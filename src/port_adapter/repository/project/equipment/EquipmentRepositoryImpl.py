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
from src.port_adapter.repository.common.DbUtil import DbUtil
from src.port_adapter.repository.db_model.Equipment import Equipment as DbEquipment
from src.port_adapter.repository.db_model.equipment__equipment__junction import EQUIPMENT__EQUIPMENT__JUNCTION
from src.resource.common.Util import Util
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
    def linkEquipmentToEquipment(self, srcObj: Equipment, dstObj:Equipment, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()

        sql = f"""FROM {EQUIPMENT__EQUIPMENT__JUNCTION} equip__equip__junc
                            WHERE equip__equip__junc.src_equipment_id = "{srcObj.id()}" AND equip__equip__junc.dst_equipment_id = "{dstObj.id()}"
                        """
        dbObjectsCount = dbSession.execute(
            text(f"SELECT count(1) {sql}")
        ).scalar()

        if dbObjectsCount == 0:
            dbSession.execute(
                text(f"""
                    INSERT INTO {EQUIPMENT__EQUIPMENT__JUNCTION} (`src_equipment_id`, `dst_equipment_id`)
                    VALUES ("{srcObj.id()}", "{dstObj.id()}")
                """)
            )

    @debugLogger
    def unlinkEquipmentToEquipment(self, srcObj: Equipment, dstObj:Equipment, tokenData: TokenData = None):
        dbSession = ApplicationServiceLifeCycle.dbContext()
        dbSession.execute(
            text(f"""
                DELETE FROM {EQUIPMENT__EQUIPMENT__JUNCTION} equip__equip__junc
                WHERE equip__equip__junc.src_equipment_id = "{srcObj.id()}" AND equip__equip__junc.dst_equipment_id = "{dstObj.id()}"                
            """)
        )

    @debugLogger
    def deleteEquipment(self, obj: Equipment, tokenData: TokenData = None, ignoreRelations: bool = False) -> None:
        dbSession = ApplicationServiceLifeCycle.dbContext()
        # if ignoreRelations:
        DbUtil.enableForeignKeyChecks(dbSession=dbSession)
        # dbSession.execute(text(f'''
        #                     DELETE FROM equipment WHERE id = "{obj.id()}"
        #                 '''))
        dbObject = dbSession.query(DbEquipment).filter_by(id=obj.id()).first()
        if dbObject is not None:
            dbSession.delete(dbObject)
        # if ignoreRelations:
        #     DbUtil.disableForeignKeyChecks(dbSession=dbSession)


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
            equipmentCategoryGroupId=dbObject.equipmentCategoryGroupId,
            buildingId=dbObject.buildingId,
            buildingLevelId=dbObject.buildingLevelId,
            buildingLevelRoomId=dbObject.buildingLevelRoomId,
            quantity=dbObject.quantity,
        )

    @debugLogger
    def equipmentsByProjectId(
        self,
        tokenData: TokenData,
        projectId: str = None,
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
            .filter(DbEquipment.projectId == projectId)
            .order_by(text(sortData))
            .limit(resultSize)
            .offset(resultFrom)
            .all()
        )
        itemsCount = dbSession.query(DbEquipment.id).filter(DbEquipment.projectId == projectId).count()
        if items is None:
            return {"items": [], "totalItemCount": 0}
        attributes = [Util.snakeCaseToLowerCameCaseString(x) if x != 'equipment_id' else 'id'
                      for x in Equipment.createFrom(skipValidation=True).toMap().keys()]
        resultItems = []
        for v in items:
            objArgs = {x: getattr(v, x, None) for x in attributes}
            resultItems.append(Equipment.createFrom(**objArgs))
        return {
            "items": resultItems,
            "totalItemCount": itemsCount,
        }

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
        attributes = [Util.snakeCaseToLowerCameCaseString(x) if x != 'equipment_id' else 'id'
                      for x in Equipment.createFrom(skipValidation=True).toMap().keys()]

        resultItems = []
        for v in items:
            objArgs = {x: getattr(v, x, None) for x in attributes}
            resultItems.append(Equipment.createFrom(**objArgs))
        return {
            "items": resultItems,
            "totalItemCount": itemsCount,
        }

    def _updateDbObjectByObj(self, dbObject: DbEquipment, obj: Equipment):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        dbObject.projectId = obj.projectId() if obj.projectId() is not None else dbObject.projectId
        dbObject.manufacturerId = obj.manufacturerId() if obj.manufacturerId() is not None else dbObject.manufacturerId
        dbObject.equipmentModelId = obj.equipmentModelId() if obj.equipmentModelId() is not None else dbObject.equipmentModelId
        dbObject.equipmentProjectCategoryId = obj.equipmentProjectCategoryId() if obj.equipmentProjectCategoryId() is not None else dbObject.equipmentProjectCategoryId
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
                       equipmentCategoryGroupId=obj.equipmentCategoryGroupId(),
                       buildingId=obj.buildingId(),
                       buildingLevelId=obj.buildingLevelId(),
                       buildingLevelRoomId=obj.buildingLevelRoomId(),
                       quantity=obj.quantity())