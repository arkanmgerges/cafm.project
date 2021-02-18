"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import EquipmentCategoryGroup

"""
c4model|cb|project:ComponentQueue(project__domainemodel_event__EquipmentCategoryGroupCreated, "CommonEventConstant.EQUIPMENT_CATEGORY_GROUP_CREATED.value", "message", "event")
"""


class EquipmentCategoryGroupCreated(DomainEvent):
    def __init__(self, obj: EquipmentCategoryGroup):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.EQUIPMENT_CATEGORY_GROUP_CREATED.value)
        self._data = obj.toMap()
