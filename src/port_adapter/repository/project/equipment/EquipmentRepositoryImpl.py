"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from src.domain_model.project.equipment.Equipment import Equipment
from src.domain_model.project.equipment.EquipmentRepository import EquipmentRepository
from src.domain_model.resource.exception.EquipmentDoesNotExistException import EquipmentDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.Equipment import Equipment as DbEquipment
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class EquipmentRepositoryImpl(EquipmentRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}")
        except Exception as e:
            logger.warn(f'[{EquipmentRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def save(self, obj: Equipment, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipment).filter_by(id=obj.id()).first()
            if dbObject is not None:
                self.updateEquipment(obj=obj, tokenData=tokenData)
            else:
                self.createEquipment(obj=obj, tokenData=tokenData)
        finally:
            dbSession.close()

    @debugLogger
    def createEquipment(self, obj: Equipment, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = DbEquipment(
                id=obj.id(),
                name=obj.name(),
                projectId=obj.projectId(),
                manufacturerId=obj.manufacturerId(),
                equipmentModelId=obj.equipmentModelId(),
                equipmentProjectCategoryId=obj.equipmentProjectCategoryId(),
                equipmentCategoryId=obj.equipmentCategoryId(),
                equipmentCategoryGroupId=obj.equipmentCategoryGroupId(),
                buildingId=obj.buildingId(),
                buildingLevelId=obj.buildingLevelId(),
                buildingLevelRoomId=obj.buildingLevelRoomId(),
                quantity=obj.quantity()
            )
            result = dbSession.query(DbEquipment).filter_by(id=obj.id()).first()
            if result is None:
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteEquipment(self, obj: Equipment, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipment).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateEquipment(self, obj: Equipment, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipment).filter_by(id=obj.id()).first()
            if dbObject is None:
                raise EquipmentDoesNotExistException(f'id = {obj.id()}')
            savedObj: Equipment = self.equipmentById(obj.id())
            if savedObj != obj:
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
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def equipmentById(self, id: str) -> Equipment:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipment).filter_by(id=id).first()
            if dbObject is None:
                raise EquipmentDoesNotExistException(f'id = {id}')
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
                quantity=dbObject.quantity
            )
        finally:
            dbSession.close()

    @debugLogger
    def equipments(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
                   order: List[dict] = None) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            sortData = ''
            if order is not None:
                for item in order:
                    sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
                sortData = sortData[2:]
            items = dbSession.query(DbEquipment).order_by(text(sortData)).limit(resultSize).offset(resultFrom).all()
            itemsCount = dbSession.query(DbEquipment).count()
            if items is None:
                return {"items": [], "itemCount": 0}
            return {"items": [
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
                    quantity=x.quantity
                )
                for x in items],
                "itemCount": itemsCount}
        finally:
            dbSession.close()
