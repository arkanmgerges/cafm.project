"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import os

from sqlalchemy import create_engine

from src.domain_model.city.City import City
from src.domain_model.city.CityRepository import CityRepository
from src.domain_model.resource.exception.CityDoesNotExistException import CityDoesNotExistException
from src.port_adapter.repository.DbSession import DbSession
from src.port_adapter.repository.db_model.City import City as DbCity
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class CityRepositoryImpl(CityRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}"
            )
        except Exception as e:
            logger.warn(f"[{CityRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}")
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def cityById(self, id: int) -> City:
        dbSession = DbSession.newSession(dbEngine=self._db)
        try:
            dbObject = dbSession.query(DbCity).filter_by(geoNameId=id).first()
            if dbObject is None:
                raise CityDoesNotExistException(f"id = {id}")
            return City.createFrom(id=dbObject.geoNameId, name=dbObject.cityName)
        finally:
            dbSession.close()

    def _updateDbObjectByObj(self, dbObject: DbCity, obj: City):
        dbObject.name = obj.name() if obj.name() is not None else dbObject.name
        return dbObject

    def _createDbObjectByObj(self, obj: City):
        return DbCity(id=obj.id(), name=obj.name())
