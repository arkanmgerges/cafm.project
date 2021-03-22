"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, Optional, Union
from uuid import uuid4

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException


class BuildingLevel:
    def __init__(self, id: str = None, name: str = '', rooms: List[BuildingLevelRoom] = None,
                 buildingIds: List[str] = None, skipValidation: bool = False):
        self._buildingIds = [] if buildingIds is None else buildingIds
        self._name = name
        self._rooms: [BuildingLevelRoom] = [] if rooms is None else rooms
        self._id = str(uuid4()) if id is None else id

    @classmethod
    def createFrom(cls, id: str = None, name: str = '', rooms: List[BuildingLevelRoom] = None,
                   buildingIds: List[str] = None, publishEvent: bool = False, skipValidation: bool = False):
        obj = BuildingLevel(id=id, name=name, rooms=rooms, buildingIds=buildingIds, skipValidation=skipValidation)
        if publishEvent:
            from src.domain_model.project.building.level.BuildingLevelCreated import BuildingLevelCreated
            DomainPublishedEvents.addEventForPublishing(BuildingLevelCreated(obj))
        return obj

    @classmethod
    def createFromObject(cls, obj: 'BuildingLevel' = None, publishEvent: bool = False, generateNewId: bool = False, skipValidation: bool = False):
        if obj is None or not isinstance(obj, BuildingLevel):
            raise InvalidArgumentException(f'Invalid building level passed as an argument: {obj}')
        id = None if generateNewId else obj.id()
        return cls.createFrom(id=id, name=obj.name(), buildingIds=obj.buildingIds(), publishEvent=publishEvent, skipValidation=skipValidation)

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
        from src.domain_model.project.building.level.BuildingLevelToBuildingUnlinked import \
            BuildingLevelToBuildingUnlinked
        DomainPublishedEvents.addEventForPublishing(BuildingLevelToBuildingUnlinked(obj=self, buildingId=buildingId))

    def addRoom(self, room: BuildingLevelRoom):
        for x in self._rooms:
            if x.id() == room.id():
                from src.domain_model.resource.exception.BuildingLevelAlreadyHasRoomException import \
                    BuildingLevelAlreadyHasRoomException
                raise BuildingLevelAlreadyHasRoomException(
                    f'Level already has room, building level: {self} room: {room}')
        self._rooms.append(room)
        room.updateIndex(len(self._rooms) - 1)
        from src.domain_model.project.building.level.BuildingLevelRoomToBuildingLevelAdded import \
            BuildingLevelRoomToBuildingLevelAdded
        DomainPublishedEvents.addEventForPublishing(
            BuildingLevelRoomToBuildingLevelAdded(buildingLevelRoom=room, buildingLevel=self))

    def removeRoom(self, room: BuildingLevelRoom):
        for x in self._rooms:
            if x.id() == room.id():
                self._rooms.remove(x)
                from src.domain_model.project.building.level.BuildingLevelRoomFromBuildingLevelRemoved import \
                    BuildingLevelRoomFromBuildingLevelRemoved
                DomainPublishedEvents.addEventForPublishing(
                    BuildingLevelRoomFromBuildingLevelRemoved(buildingLevelRoom=room, buildingLevel=self))

    def publishDelete(self):
        from src.domain_model.project.building.level.BuildingLevelDeleted import BuildingLevelDeleted
        DomainPublishedEvents.addEventForPublishing(BuildingLevelDeleted(self))

    def updateRoomIndex(self, roomId: str, index: int):
        self._rooms.sort(key=lambda x: x.index())
        roomsCount = len(self._rooms)
        currentIndex = self._roomArrayIndex(roomId=roomId)
        if 0 <= index < roomsCount and currentIndex != index and currentIndex is not None:
            currentIndex = self._roomArrayIndex(roomId=roomId)
            room = self._rooms[currentIndex]
            del self._rooms[currentIndex]
            left = self._rooms[0:index]
            right = self._rooms[index:]
            result = left + [room] + right
            for x in range(min(currentIndex, index), roomsCount):
                result[x].updateIndex(x)
            self._rooms = result
            from src.domain_model.project.building.level.BuildingLevelRoomIndexUpdated import \
                BuildingLevelRoomIndexUpdated
            DomainPublishedEvents.addEventForPublishing(BuildingLevelRoomIndexUpdated(room))
        else:
            raise InvalidArgumentException(message=f'Room index is invalid room id: {roomId}, provided index: {index}')

    def _roomArrayIndex(self, roomId: str) -> Optional[Union[int, None]]:
        idx = 0
        for room in self._rooms:
            if room.id() == roomId:
                return idx
            idx += 1
        return None

    def update(self, data: dict):
        from copy import copy
        updated = False
        old = copy(self)
        if 'name' in data and data['name'] != self._name:
            updated = True
            self._name = data['name']
        if updated:
            self.publishUpdate(old)

    def publishUpdate(self, old):
        from src.domain_model.project.building.level.BuildingLevelUpdated import BuildingLevelUpdated
        DomainPublishedEvents.addEventForPublishing(BuildingLevelUpdated(old, self))

    def buildingIds(self) -> List[str]:
        return self._buildingIds

    def hasBuildingId(self, buildingId: str) -> bool:
        return buildingId in self._buildingIds

    def hasRoom(self, roomId: str) -> bool:
        for x in self._rooms:
            if x.id() == roomId:
                return True
        return False

    def id(self) -> str:
        return self._id

    def name(self) -> str:
        return self._name

    def rooms(self) -> List[BuildingLevelRoom]:
        return self._rooms

    def toMap(self, excludeInnerData: bool = False) -> dict:
        result = {"id": self.id(), "name": self.name()}
        if not excludeInnerData:
            result = {**result, "building_ids": self.buildingIds(), "rooms": [x.toMap() for x in self.rooms()]}
        return result

    def __repr__(self):
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __str__(self) -> str:
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __eq__(self, other):
        if not isinstance(other, BuildingLevel):
            raise NotImplementedError(f'other: {other} can not be compared with User class')
        return self.id() == other.id() and self.buildingIds() == other.buildingIds() and self.name() == other.name()
