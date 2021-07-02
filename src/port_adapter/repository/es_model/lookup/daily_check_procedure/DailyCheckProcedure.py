"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import os

from elasticsearch_dsl import Keyword, Nested, Document
from src.port_adapter.repository.es_model.lookup.daily_check_procedure.EquipmentCategoryGroup import EquipmentCategoryGroup
from src.port_adapter.repository.es_model.lookup.daily_check_procedure.DailyCheckProcedureOperation import DailyCheckProcedureOperation
from src.port_adapter.repository.es_model.model.EsModelAttributeData import EsModelAttributeData
from src.resource.common.Util import Util

indexPrefix = f'{os.getenv("CAFM_PROJECT_SERVICE_NAME", "cafm.project")}'

class DailyCheckProcedure(Document):
    id = Keyword()
    name = Keyword()
    description = Keyword()
    equipment_id = Keyword()
    project_id = Keyword()
    equipment_category_group = Nested(EquipmentCategoryGroup)
    daily_check_procedure_operations = Nested(DailyCheckProcedureOperation)

    class Index:
        name = f"{indexPrefix}.daily_check_procedure_1"

    @classmethod
    def createIndex(cls):
        connection = cls._get_connection()
        connection.indices.create(index=f"{indexPrefix}.daily_check_procedure_1")
        connection.indices.put_alias(index=f"{indexPrefix}.daily_check_procedure_1", name=cls.alias())
        cls.init()

    @classmethod
    def alias(cls):
        return f"{indexPrefix}.daily_check_procedure"

    @classmethod
    def attributeDataBySnakeCaseAttributeName(cls, instance: 'DailyCheckProcedure' = None, snakeCaseAttributeName: str = None) -> EsModelAttributeData:
        # Remove any dots for nested objects, e.g. country.id should become country
        periodIndex = snakeCaseAttributeName.find('.')
        if periodIndex != -1:
            snakeCaseAttributeName = snakeCaseAttributeName[:periodIndex]
        mapping = {
            "id": EsModelAttributeData(attributeModelName='id', attributeRepoName='id', attributeRepoValue=getattr(instance, 'id', None)),
            "name": EsModelAttributeData(attributeModelName='name', attributeRepoName='name', attributeRepoValue=getattr(instance, 'name', None)),
            "description": EsModelAttributeData(attributeModelName='description', attributeRepoName='description', attributeRepoValue=getattr(instance, 'description', None)),
            "equipment_id": EsModelAttributeData(attributeModelName='equipmentId', attributeRepoName='equipment_id', attributeRepoValue=getattr(instance, 'equipment_id', None)),
            "project_id": EsModelAttributeData(attributeModelName='projectId', attributeRepoName='project_id', attributeRepoValue=getattr(instance, 'project_id', None)),
            "equipment_category_group": EsModelAttributeData(attributeModelName='equipmentCategoryGroup', attributeRepoName='equipment_category_group', attributeRepoValue=Util.deepAttribute(instance, 'equipment_category_group', None), dataType=EquipmentCategoryGroup, isClass=True),
            "daily_check_procedure_operations": EsModelAttributeData(attributeModelName='dailyCheckProcedureOperations', attributeRepoName='daily_check_procedure_operations', attributeRepoValue=Util.deepAttribute(instance, 'daily_check_procedure_operations', None), dataType=DailyCheckProcedureOperation, isClass=True),
        }

        return mapping[snakeCaseAttributeName] if snakeCaseAttributeName in mapping else None


