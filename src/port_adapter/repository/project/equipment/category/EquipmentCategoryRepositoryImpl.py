"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from src.domain_model.project.equipment.category.EquipmentCategory import EquipmentCategory
from src.domain_model.project.equipment.category.EquipmentCategoryRepository import EquipmentCategoryRepository
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import EquipmentCategoryGroup
from src.domain_model.resource.exception.ObjectIdenticalException import ObjectIdenticalException
from src.domain_model.resource.exception.EquipmentCategoryDoesNotExistException import \
    EquipmentCategoryDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.EquipmentCategory import EquipmentCategory as DbEquipmentCategory
from src.port_adapter.repository.db_model.EquipmentCategoryGroup import \
    EquipmentCategoryGroup as DbEquipmentCategoryGroup
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class EquipmentCategoryRepositoryImpl(EquipmentCategoryRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}")
        except Exception as e:
            logger.warn(
                f'[{EquipmentCategoryRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def save(self, obj: EquipmentCategory, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentCategory).filter_by(id=obj.id()).first()
            try:
                if dbObject is not None:
                    self.updateEquipmentCategory(obj=obj, tokenData=tokenData)
                else:
                    self.createEquipmentCategory(obj=obj, tokenData=tokenData)
            except Exception as e:
                logger.debug(e)
        finally:
            dbSession.close()

    @debugLogger
    def createEquipmentCategory(self, obj: EquipmentCategory, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = DbEquipmentCategory(id=obj.id(), name=obj.name())
            result = dbSession.query(DbEquipmentCategory).filter_by(id=obj.id()).first()
            if result is None:
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteEquipmentCategory(self, obj: EquipmentCategory, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentCategory).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateEquipmentCategory(self, obj: EquipmentCategory, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentCategory).filter_by(id=obj.id()).first()
            if dbObject is None:
                raise EquipmentCategoryDoesNotExistException(f'id = {obj.id()}')
            savedObj: EquipmentCategory = self.equipmentCategoryById(obj.id())
            if savedObj == obj:
                logger.debug(
                    f'[{EquipmentCategoryRepositoryImpl.updateEquipmentCategory.__qualname__}] Object identical exception for old equipment model: {savedObj}\nequipment model: {obj}')
                raise ObjectIdenticalException(f'equipment model id: {obj.id()}')
            dbObject.name = obj.name() if obj.name() is not None else dbObject.name
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def equipmentCategoryByName(self, name: str) -> EquipmentCategory:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentCategory).filter_by(name=name).first()
            if dbObject is None:
                raise EquipmentCategoryDoesNotExistException(f'name = {name}')
            return EquipmentCategory(id=dbObject.id, name=dbObject.name)
        finally:
            dbSession.close()

    @debugLogger
    def equipmentCategoryById(self, id: str) -> EquipmentCategory:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentCategory).filter_by(id=id).first()
            if dbObject is None:
                raise EquipmentCategoryDoesNotExistException(f'id = {id}')
            return EquipmentCategory(id=dbObject.id, name=dbObject.name)
        finally:
            dbSession.close()

    @debugLogger
    def equipmentCategorys(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
                           order: List[dict] = None) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            sortData = ''
            if order is not None:
                for item in order:
                    sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
                sortData = sortData[2:]
            items = dbSession.query(DbEquipmentCategory).order_by(text(sortData)).limit(resultSize).offset(
                resultFrom).all()
            itemsCount = dbSession.query(DbEquipmentCategory).count()
            if items is None:
                return {"items": [], "itemCount": 0}
            return {"items": [EquipmentCategory.createFrom(id=x.id, name=x.name) for x in items],
                    "itemCount": itemsCount}
        finally:
            dbSession.close()

    @debugLogger
    def equipmentCategoryGroupsByCategoryId(self, tokenData: TokenData, id: str, resultFrom: int = 0,
                                            resultSize: int = 100, order: List[dict] = None) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            sortData = ''
            if order is not None:
                for item in order:
                    sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
                sortData = sortData[2:]

            items = dbSession.query(DbEquipmentCategoryGroup).join(DbEquipmentCategoryGroup.category).filter(
                DbEquipmentCategory.id == id).order_by(text(sortData)).limit(resultSize).offset(resultFrom).all()
            itemsCount = dbSession.query(DbEquipmentCategoryGroup).join(DbEquipmentCategoryGroup.category).filter(
                DbEquipmentCategory.id == id).count()
            if items is None:
                return {"items": [], "itemCount": 0}
            return {"items": [
                EquipmentCategoryGroup.createFrom(id=x.id, name=x.name, equipmentCategoryId=x.equipmentCategoryId) for
                x in items],
                "itemCount": itemsCount}
        finally:
            dbSession.close()
