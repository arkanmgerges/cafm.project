"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__BuildingLevelToBuildingRemoved, "CommonEventConstant.BUILDING_LEVEL_TO_BUILDING_REMOVED.value", "message", "event")
"""


class BuildingLevelToBuildingRemoved(DomainEvent):
    def __init__(self, building: Building, buildingLevel: BuildingLevel):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.BUILDING_LEVEL_TO_BUILDING_REMOVED.value)
        self._data = {"building": building.toMap(), "building_level": buildingLevel.toMap()}
