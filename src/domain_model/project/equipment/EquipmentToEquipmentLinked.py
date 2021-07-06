from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.equipment.Equipment import Equipment


class EquipmentToEquipmentLinked(DomainEvent):
    def __init__(self, sourceObj: Equipment, destinationObj: Equipment):
        super().__init__(
            id=str(uuid4()), name=CommonEventConstant.EQUIPMENT_TO_EQUIPMENT_LINKED.value
        )
        self._data = {"source_equipment": sourceObj.toMap(), "destination_equipment": destinationObj.toMap()}
