"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



from elasticsearch_dsl import InnerDoc, Keyword, Float, Nested, Integer

from src.port_adapter.repository.es_model.lookup.equipment.Unit import Unit
from src.port_adapter.repository.es_model.model.EsModelAttributeData import EsModelAttributeData
from src.resource.common.Util import Util


class MaintenanceProcedureOperationLabel(InnerDoc):
    id = Keyword()
    label = Keyword()
    generate_alert = Integer()


    @classmethod
    def attributeDataBySnakeCaseAttributeName(
        cls, instance: "MaintenanceProcedureOperationLabel" = None, snakeCaseAttributeName: str = None
    ) -> EsModelAttributeData:
        # Remove any dots for nested objects, e.g. country.id should become country
        periodIndex = snakeCaseAttributeName.rfind(".")
        if periodIndex != -1:
            snakeCaseAttributeName = snakeCaseAttributeName[:periodIndex]
        mapping = {
            "id": EsModelAttributeData(
                attributeModelName="id", attributeRepoName="id", attributeRepoValue=getattr(instance, "id", None)
            ),
            "label": EsModelAttributeData(
                attributeModelName="label", attributeRepoName="label", attributeRepoValue=getattr(instance, "label", None)
            ),
            "generate_alert": EsModelAttributeData(
                attributeModelName="generateAlert", attributeRepoName="generate_alert", attributeRepoValue=getattr(instance, "generate_alert", None), dataType=int
            ),
        }

        return mapping[snakeCaseAttributeName] if snakeCaseAttributeName in mapping else None