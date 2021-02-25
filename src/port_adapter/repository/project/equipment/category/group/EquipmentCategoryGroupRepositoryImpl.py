"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text, desc

from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import EquipmentCategoryGroup
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupRepository import \
    EquipmentCategoryGroupRepository
from src.domain_model.resource.exception.EquipmentCategoryGroupDoesNotExistException import \
    EquipmentCategoryGroupDoesNotExistException
from src.domain_model.resource.exception.ObjectIdenticalException import ObjectIdenticalException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.EquipmentCategoryGroup import \
    EquipmentCategoryGroup as DbEquipmentCategoryGroup
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class EquipmentCategoryGroupRepositoryImpl(EquipmentCategoryGroupRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}")
        except Exception as e:
            logger.warn(
                f'[{EquipmentCategoryGroupRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def save(self, obj: EquipmentCategoryGroup, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentCategoryGroup).filter_by(id=obj.id()).first()
            try:
                if dbObject is not None:
                    self.updateEquipmentCategoryGroup(obj=obj, tokenData=tokenData)
                else:
                    self.createEquipmentCategoryGroup(obj=obj, tokenData=tokenData)
            except Exception as e:
                logger.debug(e)
        finally:
            dbSession.close()

    @debugLogger
    def createEquipmentCategoryGroup(self, obj: EquipmentCategoryGroup, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = DbEquipmentCategoryGroup(id=obj.id(), name=obj.name(),
                                                equipmentCategoryId=obj.equipmentCategoryId())
            result = dbSession.query(DbEquipmentCategoryGroup).filter_by(id=obj.id()).first()
            if result is None:
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteEquipmentCategoryGroup(self, obj: EquipmentCategoryGroup, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentCategoryGroup).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateEquipmentCategoryGroup(self, obj: EquipmentCategoryGroup, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentCategoryGroup).filter_by(id=obj.id()).first()
            if dbObject is None:
                raise EquipmentCategoryGroupDoesNotExistException(f'id = {obj.id()}')
            savedObj: EquipmentCategoryGroup = self.equipmentCategoryGroupById(obj.id())
            if savedObj == obj:
                logger.debug(
                    f'[{EquipmentCategoryGroupRepositoryImpl.updateEquipmentCategoryGroup.__qualname__}] Object identical exception for old equipment model: {savedObj}\nequipment model: {obj}')
                raise ObjectIdenticalException(f'equipment model id: {obj.id()}')
            dbObject.name = obj.name() if obj.name() is not None else dbObject.name
            dbObject.equipmentCategoryId = obj.equipmentCategoryId() if obj.equipmentCategoryId() is not None else dbObject.equipmentCategoryId
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def equipmentCategoryGroupByName(self, name: str) -> EquipmentCategoryGroup:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentCategoryGroup).filter_by(name=name).first()
            if dbObject is None:
                raise EquipmentCategoryGroupDoesNotExistException(f'name = {name}')
            return EquipmentCategoryGroup(id=dbObject.id, name=dbObject.name)
        finally:
            dbSession.close()

    @debugLogger
    def equipmentCategoryGroupById(self, id: str) -> EquipmentCategoryGroup:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentCategoryGroup).filter_by(id=id).first()
            if dbObject is None:
                raise EquipmentCategoryGroupDoesNotExistException(f'id = {id}')
            return EquipmentCategoryGroup(id=dbObject.id, name=dbObject.name)
        finally:
            dbSession.close()

    @debugLogger
    def equipmentCategoryGroups(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
                                order: List[dict] = None) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            sortData = ''
            if order is not None:
                for item in order:
                    sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
                sortData = sortData[2:]
            items = dbSession.query(DbEquipmentCategoryGroup).order_by(text(sortData)).limit(resultSize).offset(
                resultFrom).all()
            itemsCount = dbSession.query(DbEquipmentCategoryGroup).count()
            if items is None:
                return {"items": [], "itemCount": 0}
            return {"items": [
                EquipmentCategoryGroup.createFrom(id=x.id, name=x.name, equipmentCategoryId=x.equipmentCategoryId) for x
                in items],
                    "itemCount": itemsCount}
        finally:
            dbSession.close()

    @debugLogger
    def equipmentCategoryGroupsByCategoryId(self, equipmentCategoryId: str = None,
                                            resultFrom: int = 0, resultSize: int = 100,
                                            order: List[dict] = None, tokenData: TokenData = None) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            q = dbSession.query(DbEquipmentCategoryGroup)
            if order is not None:
                for item in order:
                    if item['orderBy'] == 'id':
                        if item['direction'] == 'desc':
                            q = q.order_by(desc(DbEquipmentCategoryGroup.id))
                        else:
                            q = q.order_by(DbEquipmentCategoryGroup.id)
                    if item['orderBy'] == 'name':
                        if item['direction'] == 'desc':
                            q = q.order_by(desc(DbEquipmentCategoryGroup.name))
                        else:
                            q = q.order_by(DbEquipmentCategoryGroup.name)

            items = q.filter(DbEquipmentCategoryGroup.category.any(id=equipmentCategoryId)).limit(resultSize).offset(
                resultFrom).all()
            itemsCount = dbSession.query(DbEquipmentCategoryGroup).filter(
                DbEquipmentCategoryGroup.category.any(id=equipmentCategoryId)).count()
            if items is None:
                return {"items": [], "itemCount": 0}

            result = []
            for level in items:
                result.append(
                    EquipmentCategoryGroup.createFrom(id=level.id, name=level.name,
                                                      equipmentCategoryId=equipmentCategoryId))

            return {"items": result, "itemCount": itemsCount}
        finally:
            dbSession.close()