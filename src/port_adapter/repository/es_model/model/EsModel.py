"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.repository.es_model.model.AttributeData import AttributeData


class EsModel:
    @classmethod
    def createIndex(cls):
        pass

    @classmethod
    def alias(cls):
        pass

    @classmethod
    def attributeDataBySnakeCaseAttributeName(cls, instance: 'EsModel' = None, snakeCaseAttributeName: str = None) -> AttributeData:
        pass