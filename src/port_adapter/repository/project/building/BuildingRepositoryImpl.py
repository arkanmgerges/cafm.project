"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

from sqlalchemy import create_engine

from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.BuildingLevelRepository import BuildingLevelRepository
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.domain_model.resource.exception.BuildingDoesNotExistException import BuildingDoesNotExistException
from src.domain_model.resource.exception.ObjectIdenticalException import ObjectIdenticalException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.Building import Building as DbBuilding
from src.port_adapter.repository.db_model.BuildingLevel import BuildingLevel as DbBuildingLevel
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class BuildingRepositoryImpl(BuildingRepository):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi
        self._buildingLevelRepo: BuildingLevelRepository = AppDi.instance.get(BuildingLevelRepository)
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-building')}")
        except Exception as e:
            logger.warn(f'[{BuildingRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}')
            raise Exception(f'Could not connect to the db, message: {e}')

    @debugLogger
    def addLevelToBuilding(self, buildingLevel: BuildingLevel, building: Building, tokenData: TokenData = None):
        self._buildingLevelRepo.save(obj=buildingLevel)
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuildingLevel).filter_by(id=buildingLevel.id()).first()
            try:
                buildingHasLevel = False
                for dbBuilding in dbObject.buildings:
                    if dbBuilding.id == building.id():
                        buildingHasLevel = True
                        break

                if not buildingHasLevel:
                    dbBuilding = dbSession.query(DbBuilding).filter_by(id=building.id()).first()
                    dbObject.buildings.append(dbBuilding)
                    dbSession.add(dbObject)
                    dbSession.commit()
            except Exception as e:
                logger.debug(e)
        finally:
            dbSession.close()

    @debugLogger
    def removeLevelFromBuilding(self, buildingLevel: BuildingLevel, building: Building, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuildingLevel).filter_by(id=buildingLevel.id()).first()
            try:
                buildingHasLevel = False
                for dbBuilding in dbObject.buildings:
                    if dbBuilding.id == building.id():
                        buildingHasLevel = True
                        break

                if buildingHasLevel:
                    dbSession.delete(dbObject)
                    dbSession.commit()
            except Exception as e:
                logger.debug(e)
        finally:
            dbSession.close()

    @debugLogger
    def save(self, obj: Building, tokenData: TokenData = None):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
            try:
                if dbObject is not None:
                    self.updateBuilding(obj=obj, tokenData=tokenData)
                else:
                    self.createBuilding(obj=obj, tokenData=tokenData)
            except Exception as e:
                logger.debug(e)
        finally:
            dbSession.close()

    @debugLogger
    def createBuilding(self, obj: Building, tokenData: TokenData):
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = DbBuilding(id=obj.id(), name=obj.name(), projectId=obj.projectId())
            dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def deleteBuilding(self, obj: Building, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
            if dbObject is not None:
                dbSession.delete(dbObject)
                dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def updateBuilding(self, obj: Building, tokenData: TokenData = None) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
            if dbObject is None:
                raise BuildingDoesNotExistException(f'id = {obj.id()}')
            savedObj: Building = self.buildingById(obj.id())
            if savedObj == obj:
                logger.debug(
                    f'[{BuildingRepositoryImpl.updateBuilding.__qualname__}] Object identical exception for old building: {savedObj}\nbuilding: {obj}')
                raise ObjectIdenticalException(f'building id: {obj.id()}')
            dbObject.name = obj.name()
            dbSession.add(dbObject)
            dbSession.commit()
        finally:
            dbSession.close()

    @debugLogger
    def buildingById(self, id: str) -> Building:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbBuilding).filter_by(id=id).first()
            if dbObject is None:
                raise BuildingDoesNotExistException(f'id = {id}')
            return Building.createFrom(id=dbObject.id, name=dbObject.name, projectId=dbObject.projectId, buildingLevels=[
                BuildingLevel.createFrom(
                    id=dbLevel.id,
                    name=dbLevel.name,
                    rooms=[BuildingLevelRoom.createFrom(
                        id=dbRoom.id,
                        name=dbRoom.name,
                        index=dbRoom.index,
                        description=dbRoom.description,
                        buildingLevelId=dbRoom.buildingLevelId) for dbRoom in dbLevel.rooms],
                    buildingIds=[dbBuilding.id for dbBuilding in dbLevel.buildings]
                ) for dbLevel in dbObject.levels
            ])
        finally:
            dbSession.close()
