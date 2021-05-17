"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from elasticsearch_dsl import InnerDoc, Keyword


class State(InnerDoc):
    id = Keyword()
    name = Keyword()
