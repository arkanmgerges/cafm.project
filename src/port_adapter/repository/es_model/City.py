"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from elasticsearch_dsl import InnerDoc, Keyword, Integer


class City(InnerDoc):
    id = Integer()
    name = Keyword()
