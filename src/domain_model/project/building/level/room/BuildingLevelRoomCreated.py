"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__BuildingLevelRoomCreated, "CommonEventConstant.BUILDING_LEVEL_ROOM_CREATED.value", "message", "event")
"""


class BuildingLevelRoomCreated(DomainEvent):
    def __init__(self, obj: BuildingLevelRoom):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.BUILDING_LEVEL_ROOM_CREATED.value)
        self._data = obj.toMap()
