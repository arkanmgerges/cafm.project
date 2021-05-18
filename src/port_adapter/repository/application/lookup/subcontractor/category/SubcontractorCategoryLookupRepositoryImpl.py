"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

from elasticsearch_dsl import UpdateByQuery, Q
from elasticsearch_dsl.connections import connections
from sqlalchemy import create_engine

from src.application.lookup.subcontractor.category.SubcontractorCategoryLookupRepository import \
    SubcontractorCategoryLookupRepository
from src.domain_model.city.CityRepository import CityRepository
from src.domain_model.country.CountryRepository import CountryRepository
from src.domain_model.subcontractor.SubcontractorRepository import SubcontractorRepository
from src.domain_model.subcontractor.category.SubcontractorCategory import SubcontractorCategory
from src.domain_model.subcontractor.category.SubcontractorCategoryRepository import SubcontractorCategoryRepository
from src.port_adapter.repository.es_model.subcontractor.Subcontractor import (
    Subcontractor as EsSubcontractor,
)
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class SubcontractorCategoryLookupRepositoryImpl(SubcontractorCategoryLookupRepository):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi
        self._cityRepo: CityRepository = AppDi.instance.get(CityRepository)
        self._countryRepo: CountryRepository = AppDi.instance.get(CountryRepository)
        self._subcontractorCategoryRepo: SubcontractorCategoryRepository = AppDi.instance.get(
            SubcontractorCategoryRepository
        )
        self._subcontractorRepo: SubcontractorRepository = AppDi.instance.get(SubcontractorRepository)

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
                f"[{SubcontractorCategoryLookupRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def save(self, obj: SubcontractorCategory):
        if obj is not None:
            UpdateByQuery(index=EsSubcontractor.alias()).using(self._es) \
             .filter('nested', path="subcontractor_category",
                     query=Q("term",
                             **{"subcontractor_category.id": obj.id()})) \
             .script(source="ctx._source.subcontractor_category.name = params.name", params={"name": obj.name()}) \
            .execute()
