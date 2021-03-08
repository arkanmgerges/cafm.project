"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import EquipmentCategoryGroup
from src.domain_model.project.equipment.project_category.EquipmentProjectCategory import EquipmentProjectCategory
from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryRepository import EquipmentProjectCategoryRepository
from src.domain_model.resource.exception.ObjectIdenticalException import ObjectIdenticalException
from src.domain_model.resource.exception.EquipmentProjectCategoryDoesNotExistException import EquipmentProjectCategoryDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.EquipmentProjectCategory import EquipmentProjectCategory as DbEquipmentProjectCategory
from src.port_adapter.repository.db_model.EquipmentCategoryGroup import EquipmentCategoryGroup as DbEquipmentCategoryGroup
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class EquipmentProjectCategoryRepositoryImpl(EquipmentProjectCategoryRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}")
        except Exception as e:
            logger.warn(f'[{EquipmentProjectCategoryRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def save(self, obj: EquipmentProjectCategory, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentProjectCategory).filter_by(id=obj.id()).first()
            try:
                if dbObject is not None:
                    self.updateEquipmentProjectCategory(obj=obj, tokenData=tokenData)
                else:
                    self.createEquipmentProjectCategory(obj=obj, tokenData=tokenData)
            except Exception as e:
                logger.debug(e)
        finally:
            dbSession.close()

    @debugLogger
    def createEquipmentProjectCategory(self, obj: EquipmentProjectCategory, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = DbEquipmentProjectCategory(id=obj.id(), name=obj.name())
            result = dbSession.query(DbEquipmentProjectCategory).filter_by(id=obj.id()).first()
            if result is None:
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteEquipmentProjectCategory(self, obj: EquipmentProjectCategory, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentProjectCategory).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateEquipmentProjectCategory(self, obj: EquipmentProjectCategory, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentProjectCategory).filter_by(id=obj.id()).first()
            if dbObject is None:
                raise EquipmentProjectCategoryDoesNotExistException(f'id = {obj.id()}')
            savedObj: EquipmentProjectCategory = self.equipmentProjectCategoryById(obj.id())
            if savedObj == obj:
                logger.debug(
                    f'[{EquipmentProjectCategoryRepositoryImpl.updateEquipmentProjectCategory.__qualname__}] Object identical exception for old equipment project category: {savedObj}\nequipment project category: {obj}')
                raise ObjectIdenticalException(f'equipment project category id: {obj.id()}')
            dbObject.name = obj.name() if obj.name() is not None else dbObject.name
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def equipmentProjectCategoryByName(self, name: str) -> EquipmentProjectCategory:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentProjectCategory).filter_by(name=name).first()
            if dbObject is None:
                raise EquipmentProjectCategoryDoesNotExistException(f'name = {name}')
            return EquipmentProjectCategory(id=dbObject.id, name=dbObject.name)
        finally:
            dbSession.close()

    @debugLogger
    def equipmentProjectCategoryById(self, id: str) -> EquipmentProjectCategory:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentProjectCategory).filter_by(id=id).first()
            if dbObject is None:
                raise EquipmentProjectCategoryDoesNotExistException(f'id = {id}')
            return EquipmentProjectCategory(id=dbObject.id, name=dbObject.name)
        finally:
            dbSession.close()

    @debugLogger
    def equipmentProjectCategorys(self, tokenData: TokenData, resultFrom: int = 0, resultSize: int = 100,
                 order: List[dict] = None) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            sortData = ''
            if order is not None:
                for item in order:
                    sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
                sortData = sortData[2:]
            items = dbSession.query(DbEquipmentProjectCategory).order_by(text(sortData)).limit(resultSize).offset(resultFrom).all()
            itemsCount = dbSession.query(DbEquipmentProjectCategory).count()
            if items is None:
                return {"items": [], "itemCount": 0}
            return {"items": [EquipmentProjectCategory.createFrom(id=x.id, name=x.name) for x in items],
                    "itemCount": itemsCount}
        finally:
            dbSession.close()

    @debugLogger
    def linkEquipmentProjectCategoryGroup(self, category: EquipmentProjectCategory,
                                          group: EquipmentCategoryGroup) -> None:
        pass

    @debugLogger
    def unLinkEquipmentProjectCategoryGroup(self, category: EquipmentProjectCategory,
                                            group: EquipmentCategoryGroup) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbCategoryObject = dbSession.query(DbEquipmentProjectCategory).filter_by(id=category.id()).first()
            if dbCategoryObject is not None:
                dbGroupObject = dbSession.query(DbEquipmentCategoryGroup).filter_by(id=group.id()).first()
                if dbGroupObject is not None:
                    # TODO: moso moso
                    for obj in dbCategoryObject.organizations:
                        if obj.id == organization.id():
                            dbUserObject.organizations.remove(obj)
                    dbSession.commit()
        finally:
            dbSession.close()
