"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os
from typing import List, Optional

from elasticsearch_dsl.connections import connections
from sqlalchemy import create_engine

from src.application.lookup.subcontractor.SubcontractorLookup import SubcontractorLookup
from src.application.lookup.subcontractor.SubcontractorLookupRepository import SubcontractorLookupRepository
from src.domain_model.city.City import City
from src.domain_model.city.CityRepository import CityRepository
from src.domain_model.country.Country import Country
from src.domain_model.country.CountryRepository import CountryRepository
from src.domain_model.country.state.State import State
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.subcontractor.SubcontractorRepository import SubcontractorRepository
from src.domain_model.subcontractor.category.SubcontractorCategory import SubcontractorCategory
from src.domain_model.subcontractor.category.SubcontractorCategoryRepository import SubcontractorCategoryRepository
from src.port_adapter.repository.application.lookup.BaseLookupRepository import BaseLookupRepository
from src.port_adapter.repository.es_model.City import City as EsCity
from src.port_adapter.repository.es_model.Country import Country as EsCountry
from src.port_adapter.repository.es_model.State import State as EsState
from src.port_adapter.repository.es_model.subcontractor.Subcontractor import Subcontractor as EsSubcontractor
from src.port_adapter.repository.es_model.subcontractor.SubcontractorCategory import (
    SubcontractorCategory as EsSubcontractorCategory,
)
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class SubcontractorLookupRepositoryImpl(BaseLookupRepository, SubcontractorLookupRepository):
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
                f"[{SubcontractorLookupRepositoryImpl.__init__.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

    @debugLogger
    def save(self, obj: Subcontractor):
        city: Optional[City, None] = None
        country: Optional[Country, None] = None
        state: Optional[State, None] = None
        try:
            city = self._cityRepo.cityById(id=obj.cityId()) if obj.cityId() is not None else None
            country = self._countryRepo.countryById(id=obj.countryId()) if obj.countryId() is not None else None
            state = (
                self._countryRepo.stateByCountryIdAndStateId(countryId=obj.countryId(), stateId=obj.stateId())
                if obj.countryId() is not None and obj.stateId() is not None
                else None
            )
        except:
            pass

        subcontractorCategory: SubcontractorCategory = (
            self._subcontractorCategoryRepo.subcontractorCategoryById(id=obj.subcontractorCategoryId())
            if obj.subcontractorCategoryId() is not None
            else None
        )
        esDoc = EsSubcontractor.get(id=obj.id(), ignore=404)
        if esDoc is None:
            # Create
            EsSubcontractor(
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
                )
                if subcontractorCategory is not None
                else None,
                description=obj.description(),
                postal_code=obj.postalCode(),
                country=EsCountry(_id=country.id(), id=country.id(), name=country.name())
                if country is not None
                else None,
                city=EsCity(_id=city.id(), id=city.id(), name=city.name()) if city is not None else None,
                state=EsState(_id=state.id(), id=city.id(), name=city.name()) if state is not None else None,
            ).save()
        else:
            # Update
            EsSubcontractor(
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
                )
                if obj.subcontractorCategoryId() is not None
                else esDoc.subcontractor_category,
                description=obj.description() if obj.description() is not None else esDoc.description,
                postal_code=obj.postalCode() if obj.postalCode() is not None else esDoc.postal_code,
                country=EsCountry(_id=country.id(), id=country.id(), name=country.name())
                if country is not None
                else esDoc.country,
                city=EsCity(_id=city.id(), id=city.id(), name=city.name()) if city is not None else esDoc.city,
                state=EsState(_id=state.id(), id=city.id(), name=city.name()) if state is not None else esDoc.state,
            ).save()

    @debugLogger
    def delete(self, obj: Subcontractor):
        EsSubcontractor.delete(id=obj.id(), ignore=404)

    @debugLogger
    def lookup(self, resultFrom: int, resultSize: int, orders: List[dict], filters: List[dict]):
        return super().lookup(
            resultFrom=resultFrom,
            resultSize=resultSize,
            orders=orders,
            filters=filters,
            esModel=EsSubcontractor,
            lookupModel=SubcontractorLookup,
        )
