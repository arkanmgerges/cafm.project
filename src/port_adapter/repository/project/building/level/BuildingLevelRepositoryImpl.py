"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

from sqlalchemy import create_engine

from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.BuildingLevelRepository import BuildingLevelRepository
from src.domain_model.resource.exception.BuildingLevelDoesNotExistException import BuildingLevelDoesNotExistException
from src.domain_model.resource.exception.ObjectIdenticalException import ObjectIdenticalException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.BuildingLevel import BuildingLevel as DbBuildingLevel
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class BuildingLevelRepositoryImpl(BuildingLevelRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-building')}")
        except Exception as e:
            logger.warn(
                f'[{BuildingLevelRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def save(self, obj: BuildingLevel, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuildingLevel).filter_by(id=obj.id()).first()
            try:
                if dbObject is not None:
                    self.updateBuildingLevel(obj=obj, tokenData=tokenData)
                else:
                    self.createBuildingLevel(obj=obj, tokenData=tokenData)
            except Exception as e:
                logger.debug(e)
        finally:
            dbSession.close()

    @debugLogger
    def createBuildingLevel(self, obj: BuildingLevel, tokenData: TokenData):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = DbBuildingLevel(id=obj.id(), name=obj.name())
            dbSession.query(DbBuildingLevel).filter_by(id=obj.id()).first()
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteBuildingLevel(self, obj: BuildingLevel, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuildingLevel).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateBuildingLevel(self, obj: BuildingLevel, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuildingLevel).filter_by(id=obj.id()).first()
            if dbObject is None:
                raise BuildingLevelDoesNotExistException(f'building level id = {obj.id()}')
            savedObj: BuildingLevel = self.buildingLevelById(obj.id())
            if savedObj == obj:
                logger.debug(
                    f'[{BuildingLevelRepositoryImpl.updateBuildingLevel.__qualname__}] Object identical exception for old building level: {savedObj}\nbuilding level: {obj}')
                raise ObjectIdenticalException(f'building level id: {obj.id()}')
            dbObject.name = obj.name()
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def buildingLevelById(self, id: str) -> BuildingLevel:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuildingLevel).filter_by(id=id).first()
            if dbObject is None:
                raise BuildingLevelDoesNotExistException(f'id = {id}')
            from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
            return BuildingLevel.createFrom(id=dbObject.id, name=dbObject.name, buildingIds=dbObject.buildingIds,
                                            rooms=[BuildingLevelRoom.createFrom(
                                                id=x.id,
                                                name=x.name,
                                                index=x.index,
                                                description=x.description,
                                                buildingLevelId=x.buildingLevelId) for x in dbObject.rooms])
        finally:
            dbSession.close()
