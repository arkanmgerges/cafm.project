"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4
from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroup import (
    StandardEquipmentCategoryGroup,
)


class StandardEquipmentCategoryGroupUpdated(DomainEvent):
    def __init__(
        self,
        oldObj: StandardEquipmentCategoryGroup,
        newObj: StandardEquipmentCategoryGroup,
    ):
        super().__init__(
            id=str(uuid4()),
            name=CommonEventConstant.STANDARD_EQUIPMENT_CATEGORY_GROUP_UPDATED.value,
        )
        self._data = {"old": oldObj.toMap(), "new": newObj.toMap()}
