"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



from elasticsearch_dsl import InnerDoc, Keyword


class EquipmentProjectCategory(InnerDoc):
    id = Keyword()
    name = Keyword()
