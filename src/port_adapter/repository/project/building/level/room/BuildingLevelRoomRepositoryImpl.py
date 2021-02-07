"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

from sqlalchemy import create_engine

from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.domain_model.project.building.level.room.BuildingLevelRoomRepository import BuildingLevelRoomRepository
from src.domain_model.resource.exception.BuildingLevelDoesNotExistException import BuildingLevelDoesNotExistException
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
            dbObject = DbBuildingLevelRoom(id=obj.id(), name=obj.name(), description=obj.description(),
                                           buildingLevelId=obj.buildingLevelId())
            dbSession.query(DbBuildingLevelRoom).filter_by(id=obj.id()).first()
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
    def buildingLevelRoomById(self, id: str) -> BuildingLevelRoom:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuildingLevelRoom).filter_by(id=id).first()
            if dbObject is None:
                raise BuildingLevelRoomDoesNotExistException(f'id = {id}')
            return BuildingLevelRoom.createFrom(id=dbObject.id, name=dbObject.name, description=dbObject.description,
                                                buildingLevelId=dbObject.buildingLevelId)
        finally:
            dbSession.close()
