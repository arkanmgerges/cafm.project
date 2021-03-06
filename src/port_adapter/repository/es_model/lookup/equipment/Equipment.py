"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import os

from elasticsearch_dsl import Keyword, Nested, Document, Integer

from src.port_adapter.repository.es_model.lookup.equipment.Building import Building
from src.port_adapter.repository.es_model.lookup.equipment.BuildingLevel import (
    BuildingLevel,
)
from src.port_adapter.repository.es_model.lookup.equipment.BuildingLevelRoom import (
    BuildingLevelRoom,
)
from src.port_adapter.repository.es_model.lookup.equipment.EquipmentCategoryGroup import (
    EquipmentCategoryGroup,
)
from src.port_adapter.repository.es_model.lookup.equipment.EquipmentModel import (
    EquipmentModel,
)
from src.port_adapter.repository.es_model.lookup.equipment.EquipmentProjectCategory import (
    EquipmentProjectCategory,
)
from src.port_adapter.repository.es_model.lookup.equipment.MaintenanceProcedure import (
    MaintenanceProcedure,
)
from src.port_adapter.repository.es_model.lookup.equipment.Manufacturer import (
    Manufacturer,
)
from src.port_adapter.repository.es_model.model.EsModelAttributeData import (
    EsModelAttributeData,
)
from src.resource.common.Util import Util

indexPrefix = f'{os.getenv("CAFM_PROJECT_SERVICE_NAME", "cafm.project")}'


class Equipment(Document):
    id = Keyword()
    name = Keyword()
    quantity = Integer()
    project_id = Keyword()
    equipment_project_category = Nested(EquipmentProjectCategory)
    equipment_category_group = Nested(EquipmentCategoryGroup)
    building = Nested(Building)
    building_level = Nested(BuildingLevel)
    building_level_room = Nested(BuildingLevelRoom)
    manufacturer = Nested(Manufacturer)
    equipment_model = Nested(EquipmentModel)
    maintenance_procedures = Nested(MaintenanceProcedure)

    class Index:
        name = f"{indexPrefix}.equipment_1"

    @classmethod
    def createIndex(cls):
        connection = cls._get_connection()
        connection.indices.create(index=f"{indexPrefix}.equipment_1")
        connection.indices.put_alias(
            index=f"{indexPrefix}.equipment_1", name=cls.alias()
        )
        cls.init()

    @classmethod
    def alias(cls):
        return f"{indexPrefix}.equipment"

    @classmethod
    def attributeDataBySnakeCaseAttributeName(
        cls, instance: "Equipment" = None, snakeCaseAttributeName: str = None
    ) -> EsModelAttributeData:
        # Remove any dots for nested objects, e.g. country.id should become country
        periodIndex = snakeCaseAttributeName.rfind(".")
        if periodIndex != -1:
            snakeCaseAttributeName = snakeCaseAttributeName[:periodIndex]
        mapping = {
            "id": EsModelAttributeData(
                attributeModelName="id",
                attributeRepoName="id",
                attributeRepoValue=getattr(instance, "id", None),
            ),
            "name": EsModelAttributeData(
                attributeModelName="name",
                attributeRepoName="name",
                attributeRepoValue=getattr(instance, "name", None),
            ),
            "quantity": EsModelAttributeData(
                attributeModelName="quantity",
                attributeRepoName="quantity",
                attributeRepoValue=getattr(instance, "quantity", None),
                dataType=int,
            ),
            "project_id": EsModelAttributeData(
                attributeModelName="projectId",
                attributeRepoName="project_id",
                attributeRepoValue=getattr(instance, "project_id", None),
            ),
            "equipment_project_category": EsModelAttributeData(
                attributeModelName="equipmentProjectCategory",
                attributeRepoName="equipment_project_category",
                attributeRepoValue=Util.deepAttribute(
                    instance, "equipment_project_category", None
                ),
                dataType=EquipmentProjectCategory,
                isClass=True,
            ),
            "equipment_category_group": EsModelAttributeData(
                attributeModelName="equipmentCategoryGroup",
                attributeRepoName="equipment_category_group",
                attributeRepoValue=Util.deepAttribute(
                    instance, "equipment_category_group", None
                ),
                dataType=EquipmentCategoryGroup,
                isClass=True,
            ),
            "building": EsModelAttributeData(
                attributeModelName="building",
                attributeRepoName="building",
                attributeRepoValue=Util.deepAttribute(instance, "building", None),
                dataType=Building,
                isClass=True,
            ),
            "building_level": EsModelAttributeData(
                attributeModelName="buildingLevel",
                attributeRepoName="building_level",
                attributeRepoValue=Util.deepAttribute(instance, "building_level", None),
                dataType=BuildingLevel,
                isClass=True,
            ),
            "building_level_room": EsModelAttributeData(
                attributeModelName="buildingLevelRoom",
                attributeRepoName="building_level_room",
                attributeRepoValue=Util.deepAttribute(
                    instance, "building_level_room", None
                ),
                dataType=BuildingLevelRoom,
                isClass=True,
            ),
            "manufacturer": EsModelAttributeData(
                attributeModelName="manufacturer",
                attributeRepoName="manufacturer",
                attributeRepoValue=Util.deepAttribute(instance, "manufacturer", None),
                dataType=Manufacturer,
                isClass=True,
            ),
            "equipment_model": EsModelAttributeData(
                attributeModelName="equipmentModel",
                attributeRepoName="equipment_model",
                attributeRepoValue=Util.deepAttribute(
                    instance, "equipment_model", None
                ),
                dataType=Equipment,
                isClass=True,
            ),
            "maintenance_procedures": EsModelAttributeData(
                attributeModelName="maintenanceProcedures",
                attributeRepoName="maintenance_procedures",
                attributeRepoValue=Util.deepAttribute(
                    instance, "maintenance_procedures", None
                ),
                dataType=MaintenanceProcedure,
                isClass=True,
                isArray=True,
            ),
        }

        return (
            mapping[snakeCaseAttributeName]
            if snakeCaseAttributeName in mapping
            else None
        )
