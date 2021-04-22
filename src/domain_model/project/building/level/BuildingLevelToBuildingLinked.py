"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.Project import Project
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__BuildingLevelToBuildingLinked, "CommonEventConstant.BUILDING_LEVEL_TO_BUILDING_LINKED.value", "message", "event")
"""


class BuildingLevelToBuildingLinked(DomainEvent):
    def __init__(self, obj: BuildingLevel, buildingId: str):
        super().__init__(
            id=str(uuid4()),
            name=CommonEventConstant.BUILDING_LEVEL_TO_BUILDING_LINKED.value,
        )
        self._data = {
            "building_level": obj.toMap(excludeInnerData=True),
            "building_id": buildingId,
        }
