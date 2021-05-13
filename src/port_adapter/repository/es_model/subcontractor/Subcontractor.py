"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

from elasticsearch_dsl import Document, InnerDoc, Keyword, Nested, Index


indexPrefix = f'{os.getenv("CAFM_PROJECT_SERVICE_NAME", "cafm.project")}'

class SubcontractorCategory(InnerDoc):
    id = Keyword()
    name = Keyword()


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

    class Index:
        name = f'{indexPrefix}.subcontractor_1'

    @classmethod
    def createIndex(cls):
        connection = cls._get_connection()
        connection.indices.create(index=f'{indexPrefix}.subcontractor_1')
        connection.indices.put_alias(index=f'{indexPrefix}.subcontractor_1', name=f'{indexPrefix}.subcontractor')
        cls.init()
