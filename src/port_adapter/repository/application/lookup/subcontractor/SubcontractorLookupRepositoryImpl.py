"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

from elasticsearch_dsl.connections import connections
from sqlalchemy import create_engine

from src.application.lookup.subcontractor.SubcontractorLookupRepository import SubcontractorLookupRepository
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.port_adapter.repository.es_model.subcontractor.Subcontractor import Subcontractor as EsSubcontractor, \
    SubcontractorCategory as EsSubcontractorCategory
from src.domain_model.subcontractor.SubcontractorRepository import SubcontractorRepository
from src.domain_model.subcontractor.category.SubcontractorCategoryRepository import SubcontractorCategoryRepository
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class SubcontractorLookupRepositoryImpl(SubcontractorLookupRepository):

    def __init__(self):
        import src.port_adapter.AppDi as AppDi

        self._subcontractorCategoryRepo: SubcontractorCategoryRepository = AppDi.instance.get(SubcontractorCategoryRepository)
        self._subcontractorRepo: SubcontractorRepository = AppDi.instance.get(SubcontractorRepository)

        try:
            self._db = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}"
            )
            self._es = connections.create_connection(hosts=[f'{os.getenv("CAFM_PROJECT_ELASTICSEARCH_HOST", "elasticsearch")}:{os.getenv("CAFM_PROJECT_ELASTICSEARCH_PORT", 9200)}'])
        except Exception as e:
            logger.warn(
                f"[{SubcontractorLookupRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def saveBySource(self, source: Subcontractor):
        subcontractorCategory = self._subcontractorCategoryRepo.subcontractorCategoryById(id=source.subcontractorCategoryId())
        esDoc = self._es.get(id=source.id(), ignore=404)
        obj = None
        if subcontractorCategory is not None:
            if esDoc is None:
                # Create
                obj = EsSubcontractor(
                    _id=source.id(),
                    id=source.id(),
                    company_name=source.companyName(),
                    website_url=source.websiteUrl(),
                    contact_person=source.contactPerson(),
                    email=source.email(),
                    phone_number=source.phoneNumber(),
                    address_one=source.addressOne(),
                    address_two=source.addressTwo(),
                    subcontractor_category=EsSubcontractorCategory(name=subcontractorCategory.name()),
                            )
            else:
                # Update
                obj = EsSubcontractor(
                    _id=source.id(),
                    id=source.id(),
                    company_name=source.companyName() if source.companyName() is not None else esDoc.company_name,
                    website_url=source.websiteUrl() if source.companyName() is not None else esDoc.website_url,
                    contact_person=source.contactPerson() if source.companyName() is not None else esDoc.contact_person,
                    email=source.email() if source.companyName() is not None else esDoc.email,
                    phone_number=source.phoneNumber() if source.companyName() is not None else esDoc.phone_number,
                    address_one=source.addressOne() if source.companyName() is not None else esDoc.address_one,
                    address_two=source.addressTwo() if source.companyName() is not None else esDoc.address_two,
                    subcontractor_category=EsSubcontractorCategory(name=subcontractorCategory.name()) if source.companyName() is not None else esDoc.subcontractor_category.name,
                            )

            obj.save()