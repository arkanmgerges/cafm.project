"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroup import (
    StandardEquipmentCategoryGroup,
)
from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroupRepository import (
    StandardEquipmentCategoryGroupRepository,
)
from src.domain_model.resource.exception.ObjectIdenticalException import (
    ObjectIdenticalException,
)
from src.domain_model.resource.exception.StandardEquipmentCategoryGroupDoesNotExistException import (
    StandardEquipmentCategoryGroupDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.StandardEquipmentCategoryGroup import (
    StandardEquipmentCategoryGroup as DbStandardEquipmentCategoryGroup,
)
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class StandardEquipmentCategoryGroupRepositoryImpl(
    StandardEquipmentCategoryGroupRepository
):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}"
            )
        except Exception as e:
            logger.warn(
                f"[{StandardEquipmentCategoryGroupRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def save(self, obj: StandardEquipmentCategoryGroup, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = (
                dbSession.query(DbStandardEquipmentCategoryGroup)
                .filter_by(id=obj.id())
                .first()
            )
            if dbObject is not None:
                self.updateStandardEquipmentCategoryGroup(obj=obj, dbObject=dbObject, tokenData=tokenData)
            else:
                self.createStandardEquipmentCategoryGroup(obj=obj, tokenData=tokenData)
        finally:
            dbSession.close()

    @debugLogger
    def createStandardEquipmentCategoryGroup(
        self, obj: StandardEquipmentCategoryGroup, tokenData: TokenData = None
    ):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = self._createDbObjectByObj(obj=obj)
            result = (
                dbSession.query(DbStandardEquipmentCategoryGroup)
                .filter_by(id=obj.id())
                .first()
            )
            if result is None:
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteStandardEquipmentCategoryGroup(
        self, obj: StandardEquipmentCategoryGroup, tokenData: TokenData = None
    ) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = (
                dbSession.query(DbStandardEquipmentCategoryGroup)
                .filter_by(id=obj.id())
                .first()
            )
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateStandardEquipmentCategoryGroup(
        self, obj: StandardEquipmentCategoryGroup, dbObject: StandardEquipmentCategoryGroup = None, tokenData: TokenData = None
    ) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            if dbObject is None:
                raise StandardEquipmentCategoryGroupDoesNotExistException(
                    f"id = {obj.id()}"
                )
            dbObject = self._updateDbObjectByObj(dbObject=dbObject, obj=obj)
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def bulkSave(self, objList: List[StandardEquipmentCategoryGroup], tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            for obj in objList:
                dbObject = dbSession.query(DbStandardEquipmentCategoryGroup).filter_by(id=obj.id()).first()
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
            self, objList: List[StandardEquipmentCategoryGroup], tokenData: TokenData = None
    ) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            for obj in objList:
                dbObject = dbSession.query(DbStandardEquipmentCategoryGroup).filter_by(id=obj.id()).first()
                if dbObject is not None:
                    dbSession.delete(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def standardEquipmentCategoryGroupById(
        self, id: str
    ) -> StandardEquipmentCategoryGroup:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = (
                dbSession.query(DbStandardEquipmentCategoryGroup)
                .filter_by(id=id)
                .first()
            )
            if dbObject is None:
                raise StandardEquipmentCategoryGroupDoesNotExistException(f"id = {id}")
            return StandardEquipmentCategoryGroup.createFrom(
                id=dbObject.id,
                name=dbObject.name,
                standardEquipmentCategoryId=dbObject.standardEquipmentCategoryId,
            )
        finally:
            dbSession.close()

    @debugLogger
    def standardEquipmentCategoryGroups(
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
                dbSession.query(DbStandardEquipmentCategoryGroup)
                .order_by(text(sortData))
                .limit(resultSize)
                .offset(resultFrom)
                .all()
            )
            itemsCount = dbSession.query(DbStandardEquipmentCategoryGroup).count()
            if items is None:
                return {"items": [], "itemCount": 0}
            return {
                "items": [
                    StandardEquipmentCategoryGroup.createFrom(
                        id=x.id,
                        name=x.name,
                        standardEquipmentCategoryId=x.standardEquipmentCategoryId,
                    )
                    for x in items
                ],
                "itemCount": itemsCount,
            }
        finally:
            dbSession.close()

    def _updateDbObjectByObj(self, dbObject: DbStandardEquipmentCategoryGroup, obj: StandardEquipmentCategoryGroup):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        dbObject.standardEquipmentCategoryId = obj.standardEquipmentCategoryId() if obj.standardEquipmentCategoryId() is not None else dbObject.standardEquipmentCategoryId
        return dbObject


    def _createDbObjectByObj(self, obj: StandardEquipmentCategoryGroup):
        return DbStandardEquipmentCategoryGroup(id=obj.id(), name=obj.name(),
                                            standardEquipmentCategoryId=obj.standardEquipmentCategoryId())
