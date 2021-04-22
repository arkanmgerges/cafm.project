"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.building.Building import Building

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__BuildingCreated, "CommonEventConstant.BUILDING_CREATED.value", "message", "event")
"""


class BuildingCreated(DomainEvent):
    def __init__(self, obj: Building):
        super().__init__(
            id=str(uuid4()), name=CommonEventConstant.BUILDING_CREATED.value
        )
        self._data = obj.toMap()
        if "building_levels" in self._data:
            del self._data["building_levels"]
