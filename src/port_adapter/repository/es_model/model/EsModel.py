"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


class EsModel:
    from src.port_adapter.repository.es_model.model.EsModelAttributeData import EsModelAttributeData

    @classmethod
    def createIndex(cls):
        pass

    @classmethod
    def alias(cls):
        pass

    @classmethod
    def attributeDataBySnakeCaseAttributeName(
        cls, instance: "EsModel" = None, snakeCaseAttributeName: str = None
    ) -> EsModelAttributeData:
        pass
