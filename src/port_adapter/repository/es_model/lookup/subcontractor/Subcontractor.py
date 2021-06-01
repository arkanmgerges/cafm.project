"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

from elasticsearch_dsl import Keyword, Nested, Document

from src.port_adapter.repository.es_model.lookup.subcontractor.City import City
from src.port_adapter.repository.es_model.lookup.subcontractor.Country import Country
from src.port_adapter.repository.es_model.lookup.subcontractor.State import State
from src.port_adapter.repository.es_model.model.EsModelAttributeData import EsModelAttributeData
from src.port_adapter.repository.es_model.lookup.subcontractor.SubcontractorCategory import SubcontractorCategory
from src.resource.common.Util import Util

indexPrefix = f'{os.getenv("CAFM_PROJECT_SERVICE_NAME", "cafm.project")}'

class Subcontractor(Document):
    id = Keyword()
    company_name = Keyword()
    website_url = Keyword()
    contact_person = Keyword()
    email = Keyword()
    phone_number = Keyword()
    address_one = Keyword()
    address_two = Keyword()
    subcontractor_category = Nested(SubcontractorCategory)
    description = Keyword()
    postal_code = Keyword()
    country = Nested(Country)
    city = Nested(City)
    state = Nested(State)

    class Index:
        name = f"{indexPrefix}.subcontractor_1"

    @classmethod
    def createIndex(cls):
        connection = cls._get_connection()
        connection.indices.create(index=f"{indexPrefix}.subcontractor_1")
        connection.indices.put_alias(index=f"{indexPrefix}.subcontractor_1", name=cls.alias())
        cls.init()

    @classmethod
    def alias(cls):
        return f"{indexPrefix}.subcontractor"

    @classmethod
    def attributeDataBySnakeCaseAttributeName(cls, instance: 'Subcontractor' = None, snakeCaseAttributeName: str = None) -> EsModelAttributeData:
        # Remove any dots for nested objects, e.g. country.id should become country
        periodIndex = snakeCaseAttributeName.find('.')
        if periodIndex != -1:
            snakeCaseAttributeName = snakeCaseAttributeName[:periodIndex]
        mapping = {
            "id": EsModelAttributeData(attributeModelName='id', attributeRepoName='id', attributeRepoValue=getattr(instance, 'id', None)),
            "company_name": EsModelAttributeData(attributeModelName='companyName', attributeRepoName='company_name', attributeRepoValue=getattr(instance, 'company_name', None)),
            "website_url": EsModelAttributeData(attributeModelName='websiteUrl', attributeRepoName='website_url', attributeRepoValue=getattr(instance, 'website_url', None)),
            "contact_person": EsModelAttributeData(attributeModelName='contactPerson', attributeRepoName='contact_person', attributeRepoValue=getattr(instance, 'contact_person', None)),
            "email": EsModelAttributeData(attributeModelName='email', attributeRepoName='email', attributeRepoValue=getattr(instance, 'email', None)),
            "phone_number": EsModelAttributeData(attributeModelName='phoneNumber', attributeRepoName='phone_number', attributeRepoValue=getattr(instance, 'phone_number', None)),
            "address_one": EsModelAttributeData(attributeModelName='addressOne', attributeRepoName='address_one', attributeRepoValue=getattr(instance, 'address_one', None)),
            "address_two": EsModelAttributeData(attributeModelName='addressTwo', attributeRepoName='address_two', attributeRepoValue=getattr(instance, 'address_two', None)),
            "subcontractor_category": EsModelAttributeData(attributeModelName='subcontractorCategory', attributeRepoName='subcontractor_category', attributeRepoValue=Util.deepAttribute(instance, 'subcontractor_category', None), dataType=SubcontractorCategory, isClass=True),
            "description": EsModelAttributeData(attributeModelName='description', attributeRepoName='description', attributeRepoValue=getattr(instance, 'description', None)),
            "postal_code": EsModelAttributeData(attributeModelName='postalCode', attributeRepoName='postal_code', attributeRepoValue=getattr(instance, 'postal_code', None)),
            "country": EsModelAttributeData(attributeModelName='country', attributeRepoName='country', attributeRepoValue=Util.deepAttribute(instance, 'country', None), dataType=Country, isClass=True),
            "city": EsModelAttributeData(attributeModelName='city', attributeRepoName='city', attributeRepoValue=Util.deepAttribute(instance, 'city', None), dataType=City, isClass=True),
            "state": EsModelAttributeData(attributeModelName='state', attributeRepoName='state', attributeRepoValue=Util.deepAttribute(instance, 'state', None), dataType=State, isClass=True),
        }

        return mapping[snakeCaseAttributeName] if snakeCaseAttributeName in mapping else None


