"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

from elasticsearch_dsl import Document, Keyword, Nested

from src.port_adapter.repository.es_model.City import City
from src.port_adapter.repository.es_model.Country import Country
from src.port_adapter.repository.es_model.State import State
from src.port_adapter.repository.es_model.subcontractor.SubcontractorCategory import SubcontractorCategory

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