"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException


class BuildingLevelRoom:
    def __init__(self, id: str = None, name: str = '', index: int = 0, description: str = '',
                 buildingLevelId: str = None, skipValidation: bool = False):
        if not skipValidation:
            if buildingLevelId is None:
                raise InvalidArgumentException(f'building level id: {buildingLevelId}')
        self._buildingLevelId = buildingLevelId
        self._name = name
        self._index = index
        self._description = description
        self._id = str(uuid4()) if id is None else id

    @classmethod
    def createFrom(cls, id: str = None, name: str = '', index: int = 0, description: str = '',
                   buildingLevelId: str = None,
                   publishEvent: bool = False, skipValidation: bool = False):
        obj = BuildingLevelRoom(id=id, name=name, index=index, description=description, buildingLevelId=buildingLevelId, skipValidation=skipValidation)
        if publishEvent:
            from src.domain_model.project.building.level.room.BuildingLevelRoomCreated import BuildingLevelRoomCreated
            DomainPublishedEvents.addEventForPublishing(BuildingLevelRoomCreated(obj))
        return obj

    @classmethod
    def createFromObject(cls, obj: 'BuildingLevelRoom' = None, publishEvent: bool = False, generateNewId: bool = False, skipValidation: bool = False):
        if obj is None or not isinstance(obj, BuildingLevelRoom):
            raise InvalidArgumentException(f'Invalid building level passed as an argument: {obj}')
        id = None if generateNewId else obj.id()
        return cls.createFrom(id=id, name=obj.name(), index=obj.index(), description=obj.description(),
                              buildingLevelId=obj.buildingLevelId(), publishEvent=publishEvent, skipValidation=skipValidation)

    def publishDelete(self):
        from src.domain_model.project.building.level.room.BuildingLevelRoomDeleted import BuildingLevelRoomDeleted
        DomainPublishedEvents.addEventForPublishing(BuildingLevelRoomDeleted(self))

    def update(self, data: dict):
        from copy import copy
        updated = False
        old = copy(self)
        if 'name' in data and data['name'] != self._name:
            updated = True
            self._name = data['name']
        if 'description' in data and data['description'] != self._description:
            updated = True
            self._description = data['description']
        if updated:
            self.publishUpdate(old)

    def publishUpdate(self, old):
        from src.domain_model.project.building.level.room.BuildingLevelRoomUpdated import BuildingLevelRoomUpdated
        DomainPublishedEvents.addEventForPublishing(BuildingLevelRoomUpdated(old, self))

    def buildingLevelId(self) -> str:
        return self._buildingLevelId

    def id(self) -> str:
        return self._id

    def name(self) -> str:
        return self._name

    def index(self) -> int:
        return self._index

    def description(self) -> str:
        return self._description

    def updateIndex(self, index: int = 0):
        if index != self.index():
            self._index = index

    def updateDescription(self, description: str = ''):
        if self.description() != description:
            self._description = description
            from src.domain_model.project.building.level.room.BuildingLevelRoomDescriptionUpdated import \
                BuildingLevelRoomDescriptionUpdated
            DomainPublishedEvents.addEventForPublishing(BuildingLevelRoomDescriptionUpdated(self))

    def toMap(self) -> dict:
        return {"building_level_room_id": self.id(), "name": self.name(), "index": self.index(),
                "description": self.description(), "building_level_id": self.buildingLevelId()}

    def __repr__(self):
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __str__(self) -> str:
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __eq__(self, other):
        if not isinstance(other, BuildingLevelRoom):
            raise NotImplementedError(f'other: {other} can not be compared with User class')
        return self.id() == other.id() and self.buildingLevelId() == other.buildingLevelId() and \
               self.name() == other.name() and self.index() == other.index() and \
               self.description() == other.description()
