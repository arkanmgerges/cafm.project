"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import os

from elasticsearch_dsl import UpdateByQuery, Q, Search
from elasticsearch_dsl.connections import connections
from sqlalchemy import create_engine

from src.application.lookup.equipment.BuildingLevelRepository import BuildingLevelRepository
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.port_adapter.repository.es_model.lookup.equipment.Equipment import (Equipment as EsEquipment,)
from src.port_adapter.repository.lookup.common.es.UpdateByQueryValidator import UpdateByQueryValidator
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class BuildingLevelRepositoryImpl(BuildingLevelRepository):
    def __init__(self):
        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}"
            )
            self._es = connections.create_connection(
                hosts=[
                    f'{os.getenv("CAFM_PROJECT_ELASTICSEARCH_HOST", "elasticsearch")}:{os.getenv("CAFM_PROJECT_ELASTICSEARCH_PORT", 9200)}'
                ]
            )
        except Exception as e:
            logger.warn(
                f"[{BuildingLevelRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def delete(self, obj: BuildingLevel):
        if obj is not None:
            Search(index=EsEquipment.alias()).using(self._es).filter('nested', path="building_level", query=Q("term", **{"building_level.id": obj.id()})).delete()


    @debugLogger
    def save(self, obj: BuildingLevel):
        if obj is not None:
            UpdateByQueryValidator.validate(UpdateByQuery(index=EsEquipment.alias()).using(self._es) \
             .filter('nested', path="building_level",
                     query=Q("term",
                             **{"building_level.id": obj.id()})) \
             .script(source="""
             if (params.name != null) {
                            ctx._source.building_level.name = params.name;
                        }
             
             if (params.is_sub_level != null) {
                            ctx._source.building_level.is_sub_level = params.is_sub_level;
                        }
             """, params={
                 "name": obj.name(),
                 "is_sub_level": obj.isSubLevel(),
                 }) \
            .execute())
