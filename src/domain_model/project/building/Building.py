"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List
from uuid import uuid4

from src.domain_model.common.HasToMap import HasToMap
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.resource.exception.InvalidArgumentException import (
    InvalidArgumentException,
)


class Building(HasToMap):
    def __init__(
        self,
        id: str = None,
        projectId: str = None,
        name: str = "",
        buildingLevels: List[BuildingLevel] = None,
        skipValidation: bool = False,
    ):
        if not skipValidation:
            if projectId is None:
                raise InvalidArgumentException(f"project id: {projectId}")
        self._id = str(uuid4()) if id is None else id
        self._projectId = projectId
        self._name = name
        self._levels = [] if buildingLevels is None else buildingLevels

    @classmethod
    def createFrom(
        cls,
        id: str = None,
        projectId: str = None,
        name: str = "",
        buildingLevels: List[BuildingLevel] = None,
        publishEvent: bool = False,
        skipValidation: bool = False,
    ):
        obj = Building(
            id=id,
            projectId=projectId,
            name=name,
            buildingLevels=buildingLevels,
            skipValidation=skipValidation,
        )
        if publishEvent:
            from src.domain_model.project.building.BuildingCreated import (
                BuildingCreated,
            )

            DomainPublishedEvents.addEventForPublishing(BuildingCreated(obj))
        return obj

    @classmethod
    def createFromObject(
        cls,
        obj: "Building" = None,
        publishEvent: bool = False,
        generateNewId: bool = False,
        skipValidation: bool = False,
    ):
        if obj is None or not isinstance(obj, Building):
            raise InvalidArgumentException(
                f"Invalid building passed as an argument: {obj}"
            )
        id = None if generateNewId else obj.id()
        return cls.createFrom(
            id=id,
            projectId=obj.projectId(),
            name=obj.name(),
            buildingLevels=obj.levels(),
            publishEvent=publishEvent,
            skipValidation=skipValidation,
        )

    def addLevel(self, level: BuildingLevel):
        exist = False
        for lvl in self.levels():
            if lvl.id() == level.id():
                exist = True
        if exist:
            from src.domain_model.resource.exception.BuildingLevelAlreadyExistException import (
                BuildingLevelAlreadyExistException,
            )

            raise BuildingLevelAlreadyExistException(
                f"Building id {self.id()}, level: {level}"
            )
        self._levels.append(level)
        from src.domain_model.project.building.BuildingLevelToBuildingAdded import (
            BuildingLevelToBuildingAdded,
        )

        DomainPublishedEvents.addEventForPublishing(
            BuildingLevelToBuildingAdded(building=self, buildingLevel=level)
        )

    def removeLevel(self, level: BuildingLevel):
        removed = False
        for lvl in self.levels():
            if lvl.id() == level.id():
                removed = True
                self._levels.remove(lvl)
        if not removed:
            from src.domain_model.resource.exception.BuildingLevelDoesNotExistException import (
                BuildingLevelDoesNotExistException,
            )

            raise BuildingLevelDoesNotExistException(
                f"Could not remove the level for building id: {self.id()}, level: {level},"
            )
        from src.domain_model.project.building.BuildingLevelToBuildingRemoved import (
            BuildingLevelToBuildingRemoved,
        )

        DomainPublishedEvents.addEventForPublishing(
            BuildingLevelToBuildingRemoved(building=self, buildingLevel=level)
        )

    def update(self, data: dict):
        from copy import copy

        updated = False
        old = copy(self)
        if "name" in data and data["name"] != self._name:
            updated = True
            self._name = data["name"]
        if updated:
            self.publishUpdate(old)

    def publishDelete(self):
        from src.domain_model.project.building.BuildingDeleted import BuildingDeleted

        DomainPublishedEvents.addEventForPublishing(BuildingDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.project.building.BuildingUpdated import BuildingUpdated

        DomainPublishedEvents.addEventForPublishing(BuildingUpdated(old, self))

    def levels(self) -> List[BuildingLevel]:
        return self._levels

    def projectId(self):
        return self._projectId

    def name(self):
        return self._name

    def id(self):
        return self._id

    def toMap(self, excludeInnerData: bool = False) -> dict:
        result = {
            "building_id": self.id(),
            "project_id": self.projectId(),
            "name": self.name(),
        }
        if not excludeInnerData:
            result = {**result, "building_levels": [x.toMap() for x in self.levels()]}
        return result

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __eq__(self, other):
        if not isinstance(other, Building):
            raise NotImplementedError(
                f"other: {other} can not be compared with User class"
            )
        return (
            self.id() == other.id()
            and self.projectId() == other.projectId()
            and self.name() == other.name()
            and self.levels() == other.levels()
        )
