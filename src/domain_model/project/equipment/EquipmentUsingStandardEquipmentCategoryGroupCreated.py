from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.equipment.Equipment import Equipment

class EquipmentUsingStandardEquipmentCategoryGroupCreated(DomainEvent):
    def __init__(self, obj: Equipment, standardEquipmentCategoryGroupId: str):
        super().__init__(
            id=str(uuid4()), name=CommonEventConstant.EQUIPMENT_USING_STANDARD_EQUIPMENT_CATEGORY_GROUP_CREATED.value
        )
        self._data = {"equipment": obj.toMap(), "standard_equipment_category_group_id": standardEquipmentCategoryGroupId}
