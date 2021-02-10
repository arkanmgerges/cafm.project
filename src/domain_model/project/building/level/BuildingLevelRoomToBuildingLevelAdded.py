"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__BuildingLevelRoomToBuildingLevelAdded, "CommonEventConstant.BUILDING_LEVEL_ROOM_TO_BUILDING_LEVEL_ADDED.value", "message", "event")
"""


class BuildingLevelRoomToBuildingLevelAdded(DomainEvent):
    def __init__(self, buildingLevelRoom: BuildingLevelRoom, buildingLevel: BuildingLevel):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.BUILDING_LEVEL_ROOM_TO_BUILDING_LEVEL_ADDED.value)
        self._data = {"building_level": buildingLevel.toMap(), "building_level_room": buildingLevelRoom.toMap()}
        del self._data['building_level_room']['index']
