"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

from elasticsearch_dsl.connections import connections
from sqlalchemy import create_engine

from src.application.lookup.subcontractor.SubcontractorLookupRepository import SubcontractorLookupRepository
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.port_adapter.repository.es_model.subcontractor.Subcontractor import (
    Subcontractor as EsSubcontractor,
    SubcontractorCategory as EsSubcontractorCategory,
)
from src.domain_model.subcontractor.SubcontractorRepository import SubcontractorRepository
from src.domain_model.subcontractor.category.SubcontractorCategoryRepository import SubcontractorCategoryRepository
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class SubcontractorLookupRepositoryImpl(SubcontractorLookupRepository):
    def __init__(self):
        import src.port_adapter.AppDi as AppDi

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
                f"[{SubcontractorLookupRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def save(self, obj: Subcontractor):
        subcontractorCategory = self._subcontractorCategoryRepo.subcontractorCategoryById(id=obj.subcontractorCategoryId())
        esDoc = EsSubcontractor.get(id=obj.id(), ignore=404)
        resultObj = None
        if subcontractorCategory is not None:
            if esDoc is None:
                # Create
                resultObj = EsSubcontractor(
                    _id=obj.id(),
                    id=obj.id(),
                    company_name=obj.companyName(),
                    website_url=obj.websiteUrl(),
                    contact_person=obj.contactPerson(),
                    email=obj.email(),
                    phone_number=obj.phoneNumber(),
                    address_one=obj.addressOne(),
                    address_two=obj.addressTwo(),
                    subcontractor_category=EsSubcontractorCategory(
                        _id=subcontractorCategory.id(), id=subcontractorCategory.id(), name=subcontractorCategory.name()
                    ),
                )
            else:
                # Update
                resultObj = EsSubcontractor(
                    _id=obj.id(),
                    id=obj.id(),
                    company_name=obj.companyName() if obj.companyName() is not None else esDoc.company_name,
                    website_url=obj.websiteUrl() if obj.websiteUrl() is not None else esDoc.website_url,
                    contact_person=obj.contactPerson() if obj.contactPerson() is not None else esDoc.contact_person,
                    email=obj.email() if obj.email() is not None else esDoc.email,
                    phone_number=obj.phoneNumber() if obj.phoneNumber() is not None else esDoc.phone_number,
                    address_one=obj.addressOne() if obj.addressOne() is not None else esDoc.address_one,
                    address_two=obj.addressTwo() if obj.addressTwo() is not None else esDoc.address_two,
                    subcontractor_category=EsSubcontractorCategory(
                        _id=subcontractorCategory.id(), id=subcontractorCategory.id(), name=subcontractorCategory.name()
                    ),
                )

            resultObj.save()
