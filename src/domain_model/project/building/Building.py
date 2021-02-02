"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List
from uuid import uuid4

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException


class Building:
    def __init__(self, id: str = None, projectId: str = None, name: str = '', levels: List[BuildingLevel] = None):
        if projectId is None:
            raise InvalidArgumentException(f'project id: {projectId}')
        self._id = str(uuid4()) if id is None else id
        self._projectId = projectId
        self._name = name
        self._levels = [] if levels is None else levels

    @classmethod
    def createFrom(cls, id: str = None, projectId: str = None, name: str = '', levels: List[BuildingLevel] = None,
                   publishEvent: bool = False):
        obj = Building(id=id, projectId=projectId, name=name, levels=levels)
        if publishEvent:
            from src.domain_model.project.building.BuildingCreated import BuildingCreated
            DomainPublishedEvents.addEventForPublishing(BuildingCreated(obj))
        return obj

    @classmethod
    def createFromObject(cls, obj: 'Building' = None, publishEvent: bool = False, generateNewId: bool = False):
        if obj is None or not isinstance(obj, Building):
            raise InvalidArgumentException(f'Invalid building passed as an argument: {obj}')
        id = None if generateNewId else obj.id()
        return cls.createFrom(id=id, projectId=obj.projectId(), name=obj.name(), levels=obj.levels(),
                              publishEvent=publishEvent)

    def addLevel(self, level: BuildingLevel):
        exist = False
        for lvl in self.levels():
            if lvl.id() == level.id():
                exist = True
        if exist:
            from src.domain_model.resource.exception.BuildingLevelAlreadyExistException import \
                BuildingLevelAlreadyExistException
            raise BuildingLevelAlreadyExistException(f'Building id {self.id()}, level: {level}')
        self._levels.append(level)
        from src.domain_model.project.building.BuildingLevelToBuildingAdded import BuildingLevelToBuildingAdded
        DomainPublishedEvents.addEventForPublishing(BuildingLevelToBuildingAdded(level))

    def removeLevel(self, level: BuildingLevel):
        removed = False
        for lvl in self.levels():
            if lvl.id() == level.id():
                removed = True
                self._levels.remove(lvl)
        if not removed:
            from src.domain_model.resource.exception.BuildingLevelDoesNotExistException import \
                BuildingLevelDoesNotExistException
            raise BuildingLevelDoesNotExistException(
                f'Could not remove the level for building id: {self.id()}, level: {level},')
        from src.domain_model.project.building.BuildingLevelToBuildingRemoved import \
            BuildingLevelToBuildingRemoved
        DomainPublishedEvents.addEventForPublishing(BuildingLevelToBuildingRemoved(level))

    def publishDelete(self):
        from src.domain_model.project.building.BuildingDeleted import BuildingDeleted
        DomainPublishedEvents.addEventForPublishing(BuildingDeleted(self))

    def levels(self) -> List[BuildingLevel]:
        return self._levels

    def projectId(self):
        return self._projectId

    def name(self):
        return self._name

    def id(self):
        return self._id

    def toMap(self) -> dict:
        return {"id": self.id(), "project_id": self.projectId(), "name": self.name(),
                "building_levels": [x.toMap() for x in self.levels()]}

    def __repr__(self):
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __str__(self) -> str:
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __eq__(self, other):
        if not isinstance(other, Building):
            raise NotImplementedError(f'other: {other} can not be compared with User class')
        return self.id() == other.id() and self.projectId() == other.projectId() and \
               self.name() == other.name() and self.levels() == other.levels()
