"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.equipment.category.EquipmentCategory import EquipmentCategory

"""
c4model|cb|project:ComponentQueue(project__domainemodel_event__EquipmentCategoryCreated, "CommonEventConstant.EQUIPMENT_CATEGORY_CREATED.value", "message", "event")
"""


class EquipmentCategoryCreated(DomainEvent):
    def __init__(self, obj: EquipmentCategory):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.EQUIPMENT_CATEGORY_CREATED.value)
        self._data = obj.toMap()