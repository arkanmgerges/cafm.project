"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__BuildingLevelToBuildingAdded, "CommonEventConstant.BUILDING_LEVEL_TO_BUILDING_ADDED.value", "message", "event")
"""


class BuildingLevelToBuildingAdded(DomainEvent):
    def __init__(self, obj: BuildingLevel):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.BUILDING_LEVEL_TO_BUILDING_ADDED.value)
        self._data = obj.toMap()
