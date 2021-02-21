"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4
from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import EquipmentCategoryGroup

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__EquipmentCategoryGroupUpdated, "CommonEventConstant.EQUIPMENT_CATEGORY_GROUP_UPDATED.value", "message", "event")
"""


class EquipmentCategoryGroupUpdated(DomainEvent):
    def __init__(self, oldObj: EquipmentCategoryGroup, newObj: EquipmentCategoryGroup):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.EQUIPMENT_CATEGORY_GROUP_UPDATED.value)
        self._data = {'old': oldObj.toMap(), 'new': newObj.toMap()}
