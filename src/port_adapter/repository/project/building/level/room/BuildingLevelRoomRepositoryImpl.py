"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine
from sqlalchemy.sql.expression import desc
from sqlalchemy.sql.functions import func

from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.domain_model.project.building.level.room.BuildingLevelRoomRepository import BuildingLevelRoomRepository
from src.domain_model.resource.exception.BuildingLevelRoomDoesNotExistException import \
    BuildingLevelRoomDoesNotExistException
from src.domain_model.resource.exception.ObjectIdenticalException import ObjectIdenticalException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.BuildingLevelRoom import BuildingLevelRoom as DbBuildingLevelRoom
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class BuildingLevelRoomRepositoryImpl(BuildingLevelRoomRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-building')}")
        except Exception as e:
            logger.warn(
                f'[{BuildingLevelRoomRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def save(self, obj: BuildingLevelRoom, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuildingLevelRoom).filter_by(id=obj.id()).first()
            try:
                if dbObject is not None:
                    self.updateBuildingLevelRoom(obj=obj, tokenData=tokenData)
                else:
                    self.createBuildingLevelRoom(obj=obj, tokenData=tokenData)
            except Exception as e:
                logger.debug(e)
        finally:
            dbSession.close()

    @debugLogger
    def createBuildingLevelRoom(self, obj: BuildingLevelRoom, tokenData: TokenData):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = DbBuildingLevelRoom(id=obj.id(),
                                           name=obj.name(),
                                           description=obj.description(),
                                           index=obj.index(),
                                           buildingLevelId=obj.buildingLevelId())
            count = dbSession.query(func.count(DbBuildingLevelRoom.id)).scalar()
            dbObject.index = count
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteBuildingLevelRoom(self, obj: BuildingLevelRoom, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuildingLevelRoom).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateBuildingLevelRoom(self, obj: BuildingLevelRoom, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuildingLevelRoom).filter_by(id=obj.id()).first()
            if dbObject is None:
                raise BuildingLevelRoomDoesNotExistException(f'building level room id = {obj.id()}')
            savedObj: BuildingLevelRoom = self.buildingLevelRoomById(obj.id())
            if savedObj == obj:
                logger.debug(
                    f'[{BuildingLevelRoomRepositoryImpl.updateBuildingLevelRoom.__qualname__}] Object identical exception for old building level room: {savedObj}\nbuilding level room: {obj}')
                raise ObjectIdenticalException(f'building level room id: {obj.id()}')
            dbObject.name = obj.name()
            dbObject.description = obj.description()
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def buildingLevelRooms(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
                           order: List[dict] = None, buildingLevelId: str = None) -> dict:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            db = DbBuildingLevelRoom
            q = dbSession.query(db)
            if order is not None:
                for item in order:
                    if item['orderBy'] == 'id':
                        if item['direction'] == 'desc':
                            q = q.order_by(desc(db.id))
                        else:
                            q = q.order_by(db.id)
                    if item['orderBy'] == 'name':
                        if item['direction'] == 'desc':
                            q = q.order_by(desc(db.name))
                        else:
                            q = q.order_by(db.name)
                    if item['orderBy'] == 'description':
                        if item['direction'] == 'desc':
                            q = q.order_by(desc(db.description))
                        else:
                            q = q.order_by(db.description)
                    if item['orderBy'] == 'index':
                        if item['direction'] == 'desc':
                            q = q.order_by(desc(db.index))
                        else:
                            q = q.order_by(db.index)

            items = q.filter(DbBuildingLevelRoom.buildingLevelId == buildingLevelId).limit(resultSize).offset(resultFrom).all()
            itemsCount = dbSession.query(DbBuildingLevelRoom).filter(DbBuildingLevelRoom.buildingLevelId == buildingLevelId).count()
            if items is None:
                return {"items": [], "itemCount": 0}

            result = []
            for room in items:
                result.append(BuildingLevelRoom.createFrom(id=room.id, name=room.name, index=room.index,
                                                           description=room.description,
                                                           buildingLevelId=room.buildingLevelId))

            return {"items": result, "itemCount": itemsCount}
        finally:
            dbSession.close()

    @debugLogger
    def buildingLevelRoomById(self, id: str, tokenData: TokenData = None) -> BuildingLevelRoom:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuildingLevelRoom).filter_by(id=id).first()
            if dbObject is None:
                raise BuildingLevelRoomDoesNotExistException(f'building level room id = {id}')
            return BuildingLevelRoom.createFrom(id=dbObject.id, name=dbObject.name, description=dbObject.description,
                                                buildingLevelId=dbObject.buildingLevelId)
        finally:
            dbSession.close()
