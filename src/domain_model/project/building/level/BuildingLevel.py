"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List
from uuid import uuid4

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException


class BuildingLevel:
    def __init__(self, id: str = None, name: str = '', rooms: List[BuildingLevelRoom] = None,
                 buildingIds: List[str] = None):
        self._buildingIds = buildingIds
        self._name = name
        self._rooms = [] if rooms is None else rooms
        self._id = str(uuid4()) if id is None else id

    @classmethod
    def createFrom(cls, id: str = None, name: str = '', rooms: List[BuildingLevelRoom] = None,
                   buildingIds: List[str] = None, publishEvent: bool = False):
        obj = BuildingLevel(id=id, name=name, rooms=rooms, buildingIds=buildingIds)
        if publishEvent:
            from src.domain_model.project.building.level.BuildingLevelCreated import BuildingLevelCreated
            DomainPublishedEvents.addEventForPublishing(BuildingLevelCreated(obj))
        return obj

    @classmethod
    def createFromObject(cls, obj: 'BuildingLevel' = None, publishEvent: bool = False, generateNewId: bool = False):
        if obj is None or not isinstance(obj, BuildingLevel):
            raise InvalidArgumentException(f'Invalid building level passed as an argument: {obj}')
        id = None if generateNewId else obj.id()
        return cls.createFrom(id=id, name=obj.name(), buildingIds=obj.buildingIds(), publishEvent=publishEvent)

    def linkBuildingById(self, buildingId: str):
        if buildingId in self._buildingIds:
            from src.domain_model.resource.exception.BuildingLevelAlreadyLinkedToBuildingException import \
                BuildingLevelAlreadyLinkedToBuildingException
            raise BuildingLevelAlreadyLinkedToBuildingException(f'Building id: {buildingId}, level: {self}')
        self._buildingIds.append(buildingId)
        from src.domain_model.project.building.level.BuildingLevelToBuildingLinked import BuildingLevelToBuildingLinked
        DomainPublishedEvents.addEventForPublishing(BuildingLevelToBuildingLinked(obj=self, buildingId=buildingId))

    def unlinkBuildingById(self, buildingId: str):
        if buildingId in self._buildingIds:
            self._buildingIds.remove(buildingId)
        from src.domain_model.project.building.level.BuildingLevelToBuildingUnLinked import \
            BuildingLevelToBuildingUnLinked
        DomainPublishedEvents.addEventForPublishing(BuildingLevelToBuildingUnLinked(obj=self, buildingId=buildingId))

    def addRoom(self, room: BuildingLevelRoom):
        for x in self._rooms:
            if x.id() == room.id():
                from src.domain_model.resource.exception.BuildingLevelAlreadyHasRoomException import \
                    BuildingLevelAlreadyHasRoomException
                raise BuildingLevelAlreadyHasRoomException(
                    f'Level already has room, building level: {self} room: {room}')
        self._rooms.append(room)
        from src.domain_model.project.building.level.BuildingLevelRoomAdded import BuildingLevelRoomAdded
        DomainPublishedEvents.addEventForPublishing(BuildingLevelRoomAdded(obj=room, obj2=self))

    def removeRoom(self, room: BuildingLevelRoom):
        for x in self._rooms:
            if x.id() == room.id():
                self._rooms.remove(x)
                from src.domain_model.project.building.level.BuildingLevelRoomRemoved import BuildingLevelRoomRemoved
                DomainPublishedEvents.addEventForPublishing(BuildingLevelRoomRemoved(obj=room, obj2=self))

    def publishDelete(self):
        from src.domain_model.project.building.level.BuildingLevelDeleted import BuildingLevelDeleted
        DomainPublishedEvents.addEventForPublishing(BuildingLevelDeleted(self))

    def buildingIds(self) -> List[str]:
        return self._buildingIds

    def hasBuildingId(self, buildingId: str) -> bool:
        return buildingId in self._buildingIds

    def id(self) -> str:
        return self._id

    def name(self) -> str:
        return self._name

    def toMap(self) -> dict:
        return {"id": self.id(), "name": self.name(), "building_ids": self.buildingIds()}

    def __repr__(self):
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __str__(self) -> str:
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __eq__(self, other):
        if not isinstance(other, BuildingLevel):
            raise NotImplementedError(f'other: {other} can not be compared with User class')
        return self.id() == other.id() and self.buildingIds() == other.buildingIds() and self.name() == other.name()
