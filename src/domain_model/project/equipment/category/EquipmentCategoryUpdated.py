"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

import src.domain_equipmentCategory.ou.Ou as Ou

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.equipment.category.EquipmentCategory import EquipmentCategory

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__EquipmentCategoryUpdated, "CommonEventConstant.EQUIPMENT_CATEGORY_UPDATED.value", "message", "event")
"""


class EquipmentCategoryUpdated(DomainEvent):
    def __init__(self, oldObj: Ou, newObj: EquipmentCategory):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.EQUIPMENT_CATEGORY_UPDATED.value)
        self._data = {'old': oldObj.toMap(), 'new': newObj.toMap()}
