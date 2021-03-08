"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import EquipmentCategoryGroup
from src.domain_model.project.equipment.project_category.EquipmentProjectCategory import EquipmentProjectCategory

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__EquipmentProjectCategoryGroupUnLinked, "CommonEventConstant.EQUIPMENT_PROJECT_CATEGORY_GROUP_UNLINKED.value", "message", "event")
"""


class EquipmentProjectCategoryGroupUnLinked(DomainEvent):
    def __init__(self, category: EquipmentProjectCategory, group: EquipmentCategoryGroup):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.EQUIPMENT_PROJECT_CATEGORY_GROUP_UNLINKED.value)
        self._data = {'category_id': category.id(), 'group_id': group.id()}
