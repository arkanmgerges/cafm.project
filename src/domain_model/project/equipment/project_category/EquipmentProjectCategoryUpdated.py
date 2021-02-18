"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

import src.domain_equipmentProjectCategory.ou.Ou as Ou

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.equipment.project_category.EquipmentProjectCategory import EquipmentProjectCategory

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__EquipmentProjectCategoryUpdated, "CommonEventConstant.EQUIPMENT_PROJECT_CATEGORY_UPDATED.value", "message", "event")
"""


class EquipmentProjectCategoryUpdated(DomainEvent):
    def __init__(self, oldObj: Ou, newObj: EquipmentProjectCategory):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.EQUIPMENT_PROJECT_CATEGORY_UPDATED.value)
        self._data = {'old': oldObj.toMap(), 'new': newObj.toMap()}
