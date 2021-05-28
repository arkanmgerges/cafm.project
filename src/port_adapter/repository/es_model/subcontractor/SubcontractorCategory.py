"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from elasticsearch_dsl import InnerDoc, Keyword

from src.port_adapter.repository.es_model.model.EsModelAttributeData import EsModelAttributeData


class SubcontractorCategory(InnerDoc):
    id = Keyword()
    name = Keyword()

    @classmethod
    def attributeDataBySnakeCaseAttributeName(
        cls, instance: "SubcontractorCategory" = None, snakeCaseAttributeName: str = None
    ) -> EsModelAttributeData:
        # Remove any dots for nested objects, e.g. country.id should become country
        periodIndex = snakeCaseAttributeName.rfind(".")
        if periodIndex != -1:
            snakeCaseAttributeName = snakeCaseAttributeName[:periodIndex]
        mapping = {
            "id": EsModelAttributeData(
                attributeModelName="id", attributeRepoName="id", attributeRepoValue=getattr(instance, "id", None)
            ),
            "name": EsModelAttributeData(
                attributeModelName="name", attributeRepoName="name", attributeRepoValue=getattr(instance, "name", None)
            ),
        }

        return mapping[snakeCaseAttributeName] if snakeCaseAttributeName in mapping else None