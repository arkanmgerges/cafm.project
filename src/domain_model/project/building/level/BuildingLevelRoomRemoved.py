"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__BuildingLevelRoomRemoved, "CommonEventConstant.BUILDING_LEVEL_ROOM_REMOVED.value", "message", "event")
"""


class BuildingLevelRoomRemoved(DomainEvent):
    def __init__(self, obj: BuildingLevelRoom, obj2: BuildingLevel):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.BUILDING_LEVEL_ROOM_REMOVED.value)
        self._data = {"building_level": obj2.toMap(), "building_level_room": obj.toMap()}
