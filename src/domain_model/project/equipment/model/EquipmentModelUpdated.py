"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

import src.domain_equipmentModel.ou.Ou as Ou

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.equipment.model.EquipmentModel import EquipmentModel

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__EquipmentModelUpdated, "CommonEventConstant.EQUIPMENT_MODEL_UPDATED.value", "message", "event")
"""


class EquipmentModelUpdated(DomainEvent):
    def __init__(self, oldObj: Ou, newObj: EquipmentModel):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.EQUIPMENT_MODEL_UPDATED.value)
        self._data = {'old': oldObj.toMap(), 'new': newObj.toMap()}
