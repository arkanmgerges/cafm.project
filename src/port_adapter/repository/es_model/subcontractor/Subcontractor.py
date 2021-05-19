"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

from elasticsearch_dsl import Keyword, Nested, Document

from src.port_adapter.repository.es_model.City import City
from src.port_adapter.repository.es_model.Country import Country
from src.port_adapter.repository.es_model.State import State
from src.port_adapter.repository.es_model.model.AttributeData import AttributeData
from src.port_adapter.repository.es_model.subcontractor.SubcontractorCategory import SubcontractorCategory
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
    def attributeDataBySnakeCaseAttributeName(cls, instance: 'Subcontractor' = None, snakeCaseAttributeName: str = None) -> AttributeData:
        mapping = {
            "id": AttributeData(modelName='id', repoName='id', repoValue=getattr(instance, 'id', None)),
            "company_name": AttributeData(modelName='companyName', repoName='company_name', repoValue=getattr(instance, 'company_name', None)),
            "website_url": AttributeData(modelName='websiteUrl', repoName='website_url', repoValue=getattr(instance, 'website_url', None)),
            "contact_person": AttributeData(modelName='contactPerson', repoName='contact_person', repoValue=getattr(instance, 'contact_person', None)),
            "email": AttributeData(modelName='emil', repoName='email', repoValue=getattr(instance, 'email', None)),
            "phone_number": AttributeData(modelName='phoneNumber', repoName='phone_number', repoValue=getattr(instance, 'phone_number', None)),
            "address_one": AttributeData(modelName='addressOne', repoName='address_one', repoValue=getattr(instance, 'address_one', None)),
            "address_two": AttributeData(modelName='addressTwo', repoName='address_two', repoValue=getattr(instance, 'address_two', None)),
            "subcontractor_category_id": AttributeData(modelName='subcontractorCategoryId', repoName='subcontractor_category.id', repoValue=Util.deepAttribute(instance, 'subcontractor_category.id', None), dataType='int'),
            "subcontractor_category_name": AttributeData(modelName='subcontractorCategoryName', repoName='subcontractor_category.id', repoValue=Util.deepAttribute(instance, 'subcontractor_category.name', None)),
            "description": AttributeData(modelName='description', repoName='description', repoValue=getattr(instance, 'description', None)),
            "postal_code": AttributeData(modelName='postalCode', repoName='postal_code', repoValue=getattr(instance, 'postal_code', None)),
            "country_id": AttributeData(modelName='countryId', repoName='country.id', repoValue=Util.deepAttribute(instance, 'country.id', None), dataType='int'),
            "country_name": AttributeData(modelName='countryName', repoName='country.name', repoValue=Util.deepAttribute(instance, 'country.name', None)),
            "city_id": AttributeData(modelName='cityId', repoName='city.id', repoValue=Util.deepAttribute(instance, 'city.id', None), dataType='int'),
            "city_name": AttributeData(modelName='cityName', repoName='city.name', repoValue=Util.deepAttribute(instance, 'city.name', None)),
            "state_id": AttributeData(modelName='stateId', repoName='state.id', repoValue=Util.deepAttribute(instance, 'state.id', None)),
            "state_name": AttributeData(modelName='stateName', repoName='state_name', repoValue=Util.deepAttribute(instance, 'state.name', None)),
        }

        return mapping[snakeCaseAttributeName] if snakeCaseAttributeName in mapping else None


