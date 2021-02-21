"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.equipment.Equipment import Equipment

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__EquipmentCreated, "CommonEventConstant.EQUIPMENT_CREATED.value", "message", "event")
"""


class EquipmentCreated(DomainEvent):
    def __init__(self, obj: Equipment):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.EQUIPMENT_CREATED.value)
        self._data = obj.toMap()
