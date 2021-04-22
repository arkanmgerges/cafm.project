"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4
from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.equipment.Equipment import Equipment

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__EquipmentUpdated, "CommonEventConstant.EQUIPMENT_UPDATED.value", "message", "event")
"""


class EquipmentUpdated(DomainEvent):
    def __init__(self, oldObj: Equipment, newObj: Equipment):
        super().__init__(
            id=str(uuid4()), name=CommonEventConstant.EQUIPMENT_UPDATED.value
        )
        self._data = {"old": oldObj.toMap(), "new": newObj.toMap()}
