"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException


class BuildingLevelRoom:
    def __init__(self, id: str = None, name: str = '', index: int = 0, description: str = '',
                 buildingLevelId: str = None):
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
                   publishEvent: bool = False):
        obj = BuildingLevelRoom(id=id, name=name, index=index, description=description, buildingLevelId=buildingLevelId)
        if publishEvent:
            from src.domain_model.project.building.level.room.BuildingLevelRoomCreated import BuildingLevelRoomCreated
            DomainPublishedEvents.addEventForPublishing(BuildingLevelRoomCreated(obj))
        return obj

    @classmethod
    def createFromObject(cls, obj: 'BuildingLevelRoom' = None, publishEvent: bool = False, generateNewId: bool = False):
        if obj is None or not isinstance(obj, BuildingLevelRoom):
            raise InvalidArgumentException(f'Invalid building level passed as an argument: {obj}')
        id = None if generateNewId else obj.id()
        return cls.createFrom(id=id, name=obj.name(), index=obj.index(), description=obj.description(),
                              buildingLevelId=obj.buildingLevelId(), publishEvent=publishEvent)

    def publishDelete(self):
        from src.domain_model.project.building.level.room.BuildingLevelRoomDeleted import BuildingLevelRoomDeleted
        DomainPublishedEvents.addEventForPublishing(BuildingLevelRoomDeleted(self))

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

    def changeIndex(self, newIndex: int = 0):
        if newIndex != self.index():
            self._index = newIndex
            from src.domain_model.project.building.level.room.BuildingLevelRoomIndexChanged import \
                BuildingLevelRoomIndexChanged
            DomainPublishedEvents.addEventForPublishing(BuildingLevelRoomIndexChanged(self))

    def changeDescription(self, description: str = ''):
        if self.description() != description:
            self._description = description
            from src.domain_model.project.building.level.room.BuildingLevelRoomDescriptionChanged import \
                BuildingLevelRoomDescriptionChanged
            DomainPublishedEvents.addEventForPublishing(BuildingLevelRoomDescriptionChanged(self))

    def toMap(self) -> dict:
        return {"id": self.id(), "name": self.name(), "index": self.index(),
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
