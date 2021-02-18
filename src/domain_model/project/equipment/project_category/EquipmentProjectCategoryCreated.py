"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.equipment.project_category.EquipmentProjectCategory import EquipmentProjectCategory

"""
c4model|cb|project:ComponentQueue(project__domainemodel_event__EquipmentProjectCategoryCreated, "CommonEventConstant.EQUIPMENT_PROJECT_CATEGORY_CREATED.value", "message", "event")
"""


class EquipmentProjectCategoryCreated(DomainEvent):
    def __init__(self, obj: EquipmentProjectCategory):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.EQUIPMENT_PROJECT_CATEGORY_CREATED.value)
        self._data = obj.toMap()
