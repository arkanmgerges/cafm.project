"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4
from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.standard_equipment.standard_category.StandardEquipmentCategory import (
    StandardEquipmentCategory,
)


class StandardEquipmentCategoryDeleted(DomainEvent):
    def __init__(self, obj: StandardEquipmentCategory):
        super().__init__(
            id=str(uuid4()),
            name=CommonEventConstant.STANDARD_EQUIPMENT_CATEGORY_DELETED.value,
        )
        self._data = obj.toMap()
