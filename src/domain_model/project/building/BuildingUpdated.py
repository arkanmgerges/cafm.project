"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.building.Building import Building

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__BuildingUpdated, "CommonEventConstant.BUILDING_UPDATED.value", "message", "event")
"""


class BuildingUpdated(DomainEvent):
    def __init__(self, oldObj: Building, newObj: Building):
        super().__init__(
            id=str(uuid4()), name=CommonEventConstant.BUILDING_UPDATED.value
        )
        self._data = {"old": oldObj.toMap(), "new": newObj.toMap()}
