"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from src.domain_model.project.standard_equipment.StandardEquipment import (
    StandardEquipment,
)
from src.domain_model.project.standard_equipment.StandardEquipmentRepository import (
    StandardEquipmentRepository,
)
from src.domain_model.resource.exception.ObjectIdenticalException import (
    ObjectIdenticalException,
)
from src.domain_model.resource.exception.StandardEquipmentDoesNotExistException import (
    StandardEquipmentDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.StandardEquipment import (
    StandardEquipment as DbStandardEquipment,
)
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class StandardEquipmentRepositoryImpl(StandardEquipmentRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}"
            )
        except Exception as e:
            logger.warn(
                f"[{StandardEquipmentRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def save(self, obj: StandardEquipment, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = (
                dbSession.query(DbStandardEquipment).filter_by(id=obj.id()).first()
            )
            if dbObject is not None:
                self.updateStandardEquipment(obj=obj, dbObject=dbObject, tokenData=tokenData)
            else:
                self.createStandardEquipment(obj=obj, tokenData=tokenData)
        finally:
            dbSession.close()

    @debugLogger
    def createStandardEquipment(
        self, obj: StandardEquipment, tokenData: TokenData = None
    ):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = self._createDbObjectByObj(obj=obj)
            result = dbSession.query(DbStandardEquipment).filter_by(id=obj.id()).first()
            if result is None:
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteStandardEquipment(
        self, obj: StandardEquipment, tokenData: TokenData = None
    ) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = (
                dbSession.query(DbStandardEquipment).filter_by(id=obj.id()).first()
            )
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateStandardEquipment(
        self, obj: StandardEquipment, dbObject: DbStandardEquipment = None, tokenData: TokenData = None
    ) -> None:
        from sqlalchemy import inspect
        dbSession = inspect(dbObject).session
        if dbObject is None:
            raise StandardEquipmentDoesNotExistException(f"id = {obj.id()}")
        dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
        dbSession.add(dbObject)
        dbSession.commit()

    @debugLogger
    def bulkSave(self, objList: List[StandardEquipment], tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            for obj in objList:
                dbObject = dbSession.query(DbStandardEquipment).filter_by(id=obj.id()).first()
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
            self, objList: List[StandardEquipment], tokenData: TokenData = None
    ) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            for obj in objList:
                dbObject = dbSession.query(DbStandardEquipment).filter_by(id=obj.id()).first()
                if dbObject is not None:
                    dbSession.delete(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def standardEquipmentById(self, id: str) -> StandardEquipment:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbStandardEquipment).filter_by(id=id).first()
            if dbObject is None:
                raise StandardEquipmentDoesNotExistException(f"id = {id}")
            return StandardEquipment.createFrom(
                id=dbObject.id,
                name=dbObject.name,
                standardEquipmentCategoryId=dbObject.standardEquipmentCategoryId,
                standardEquipmentCategoryGroupId=dbObject.standardEquipmentCategoryGroupId,
                manufacturerId=dbObject.manufacturerId,
                equipmentModelId=dbObject.equipmentModelId,
            )
        finally:
            dbSession.close()

    @debugLogger
    def standardEquipments(
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
                dbSession.query(DbStandardEquipment)
                .order_by(text(sortData))
                .limit(resultSize)
                .offset(resultFrom)
                .all()
            )
            itemsCount = dbSession.query(DbStandardEquipment).count()
            if items is None:
                return {"items": [], "totalItemCount": 0}
            return {
                "items": [
                    StandardEquipment.createFrom(
                        id=x.id,
                        name=x.name,
                        standardEquipmentCategoryId=x.standardEquipmentCategoryId,
                        standardEquipmentCategoryGroupId=x.standardEquipmentCategoryGroupId,
                        manufacturerId=x.manufacturerId,
                        equipmentModelId=x.equipmentModelId,
                    )
                    for x in items
                ],
                "totalItemCount": itemsCount,
            }
        finally:
            dbSession.close()

    def _updateDbObjectByObj(self, dbObject: DbStandardEquipment, obj: StandardEquipment):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        dbObject.standardEquipmentCategoryId = obj.standardEquipmentCategoryId() if obj.standardEquipmentCategoryId() is not None else dbObject.standardEquipmentCategoryId
        dbObject.standardEquipmentCategoryGroupId = obj.standardEquipmentCategoryGroupId() if obj.standardEquipmentCategoryGroupId() is not None else dbObject.standardEquipmentCategoryGroupId
        dbObject.manufacturerId = obj.manufacturerId() if obj.manufacturerId() is not None else dbObject.manufacturerId
        dbObject.equipmentModelId = obj.equipmentModelId() if obj.equipmentModelId() is not None else dbObject.equipmentModelId
        return dbObject


    def _createDbObjectByObj(self, obj: StandardEquipment):
        return DbStandardEquipment(id=obj.id(), name=obj.name(),
                               standardEquipmentCategoryId=obj.standardEquipmentCategoryId(),
                               standardEquipmentCategoryGroupId=obj.standardEquipmentCategoryGroupId(),
                               manufacturerId=obj.manufacturerId(),
                               equipmentModelId=obj.equipmentModelId())