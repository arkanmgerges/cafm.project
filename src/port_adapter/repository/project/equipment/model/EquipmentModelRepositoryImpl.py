"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import text

from src.domain_model.project.equipment.model.EquipmentModel import EquipmentModel
from src.domain_model.project.equipment.model.EquipmentModelRepository import EquipmentModelRepository
from src.domain_model.resource.exception.EquipmentModelDoesNotExistException import EquipmentModelDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.EquipmentModel import EquipmentModel as DbEquipmentModel
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class EquipmentModelRepositoryImpl(EquipmentModelRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}")
        except Exception as e:
            logger.warn(
                f'[{EquipmentModelRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def save(self, obj: EquipmentModel, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentModel).filter_by(id=obj.id()).first()
            if dbObject is not None:
                self.updateEquipmentModel(obj=obj, tokenData=tokenData)
            else:
                self.createEquipmentModel(obj=obj, tokenData=tokenData)
        finally:
            dbSession.close()

    @debugLogger
    def createEquipmentModel(self, obj: EquipmentModel, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = DbEquipmentModel(id=obj.id(), name=obj.name())
            result = dbSession.query(DbEquipmentModel).filter_by(id=obj.id()).first()
            if result is None:
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteEquipmentModel(self, obj: EquipmentModel, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentModel).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateEquipmentModel(self, obj: EquipmentModel, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentModel).filter_by(id=obj.id()).first()
            if dbObject is None:
                raise EquipmentModelDoesNotExistException(f'id = {obj.id()}')
            savedObj: EquipmentModel = self.equipmentModelById(obj.id())
            if savedObj != obj:
                dbObject.name = obj.name() if obj.name() is not None else dbObject.name
                dbSession.add(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def equipmentModelByName(self, name: str) -> EquipmentModel:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentModel).filter_by(name=name).first()
            if dbObject is None:
                raise EquipmentModelDoesNotExistException(f'name = {name}')
            return EquipmentModel(id=dbObject.id, name=dbObject.name)
        finally:
            dbSession.close()

    @debugLogger
    def equipmentModelById(self, id: str) -> EquipmentModel:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbEquipmentModel).filter_by(id=id).first()
            if dbObject is None:
                raise EquipmentModelDoesNotExistException(f'id = {id}')
            return EquipmentModel(id=dbObject.id, name=dbObject.name)
        finally:
            dbSession.close()

    @debugLogger
    def equipmentModels(self, resultFrom: int = 0, resultSize: int = 100,
                        order: List[dict] = None, tokenData: TokenData = None) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            sortData = ''
            if order is not None:
                for item in order:
                    sortData = f'{sortData}, {item["orderBy"]} {item["direction"]}'
                sortData = sortData[2:]
            items = dbSession.query(DbEquipmentModel).order_by(text(sortData)).limit(resultSize).offset(
                resultFrom).all()
            itemsCount = dbSession.query(DbEquipmentModel).count()
            if items is None:
                return {"items": [], "itemCount": 0}
            return {"items": [EquipmentModel.createFrom(id=x.id, name=x.name) for x in items],
                    "itemCount": itemsCount}
        finally:
            dbSession.close()
