"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List

from sqlalchemy import create_engine

from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.BuildingRepository import BuildingRepository
from src.domain_model.project.building.level.BuildingLevelRepository import BuildingLevelRepository
from src.domain_model.resource.exception.BuildingDoesNotExistException import BuildingDoesNotExistException
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
    def createBuilding(self, obj: Building, tokenData: TokenData):
        dbObject = DbBuilding(id=obj.id(), name=obj.name(), projectId=obj.projectId())
        dbSession = DbSession.newSession(dbEngine=self._db)
        dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
        dbSession.add(dbObject)
        dbSession.commit()

    @debugLogger
    def deleteBuilding(self, obj: Building, tokenData: TokenData) -> None:
        dbSession = DbSession.newSession(dbEngine=self._db)
        dbObject = dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
        if dbObject is not None:
            dbSession.delete(dbObject)
            dbSession.commit()

    @debugLogger
    def save(self, obj: Building):
        dbSession = DbSession.newSession(dbEngine=self._db)
        dbObject: DbBuilding = dbSession.query(DbBuilding).filter_by(id=obj.id()).first()
        dbObject.id = obj.id()
        dbObject.name = obj.name()
        dbObject.projectId = obj.projectId()

        dbLevels = [self._buildingLevelRepo.buildingLevelById(x.id()) for x in obj.levels()]

        dbObject.levels.append()


    @debugLogger
    def buildingById(self, id: str) -> Building:
        dbSession = DbSession.newSession(dbEngine=self._db)
        dbObject = dbSession.query(DbBuilding).filter_by(id=id).first()
        if dbObject is None:
            raise BuildingDoesNotExistException(f'id = {id}')
        return Building(id=dbObject.id, name=dbObject.name, projectId=dbObject.projectId)