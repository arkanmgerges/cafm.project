"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.equipment.project_category.EquipmentProjectCategory import (
    EquipmentProjectCategory,
)

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__EquipmentProjectCategoryDeleted, "CommonEventConstant.EQUIPMENT_PROJECT_CATEGORY_DELETED.value", "message", "event")
"""


class EquipmentProjectCategoryDeleted(DomainEvent):
    def __init__(self, obj: EquipmentProjectCategory):
        super().__init__(
            id=str(uuid4()),
            name=CommonEventConstant.EQUIPMENT_PROJECT_CATEGORY_DELETED.value,
        )
        self._data = obj.toMap()
