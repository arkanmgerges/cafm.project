"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from elasticsearch_dsl import InnerDoc, Keyword


class SubcontractorCategory(InnerDoc):
    id = Keyword()
    name = Keyword()
