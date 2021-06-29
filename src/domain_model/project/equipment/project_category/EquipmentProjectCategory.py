"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.common.HasToMap import HasToMap
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.resource.logging.logger import logger
from uuid import uuid4


class EquipmentProjectCategory(HasToMap):
    def __init__(self, id: str = None, name: str = None, projectId: str = None, skipValidation: bool = False):
        self._id = str(uuid4()) if id is None else id
        self._name = name
        self._projectId = projectId

        if not skipValidation:
            if name is None or name == "":
                from src.domain_model.resource.exception.InvalidArgumentException import (
                    InvalidArgumentException,
                )

                raise InvalidArgumentException(
                    f"Invalid equipment project category name: {name}, for equipment project category id: {id}"
                )

    @classmethod
    def createFrom(
        cls,
        id: str = None,
        name: str = None,
        projectId: str = None,
        publishEvent: bool = False,
        skipValidation: bool = False,
        **_kwargs,
    ):
        from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryCreated import (
            EquipmentProjectCategoryCreated,
        )

        obj = EquipmentProjectCategory(id=id, name=name, projectId=projectId, skipValidation=skipValidation)

        if publishEvent:
            logger.debug(
                f"[{EquipmentProjectCategory.createFrom.__qualname__}] - Create equipment project category with id: {id}"
            )
            DomainPublishedEvents.addEventForPublishing(
                EquipmentProjectCategoryCreated(obj)
            )
        return obj

    @classmethod
    def createFromObject(
        cls,
        obj: "EquipmentProjectCategory",
        publishEvent: bool = False,
        generateNewId: bool = False,
        skipValidation: bool = False,
    ):
        logger.debug(f"[{EquipmentProjectCategory.createFromObject.__qualname__}]")
        id = None if generateNewId else obj.id()
        return cls.createFrom(
            id=id,
            name=obj.name(),
            projectId=obj._projectId(),
            skipValidation=skipValidation,
            publishEvent=publishEvent,
        )

    def id(self) -> str:
        return self._id

    def name(self) -> str:
        return self._name

    def projectId(self) -> str:
        return self._projectId

    def update(self, data: dict):
        from copy import copy

        updated = False
        old = copy(self)
        # if 'name' in data and data['name'] != self._name:
        #     updated = True
        #     self._name = data['name']
        if updated:
            pass
        # self.publishUpdate(old)

    def publishDelete(self):
        from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryDeleted import (
            EquipmentProjectCategoryDeleted,
        )

        DomainPublishedEvents.addEventForPublishing(
            EquipmentProjectCategoryDeleted(self)
        )

    def publishUpdate(self, old):
        from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryUpdated import (
            EquipmentProjectCategoryUpdated,
        )

        DomainPublishedEvents.addEventForPublishing(
            EquipmentProjectCategoryUpdated(old, self)
        )

    def toMap(self) -> dict:
        return {"equipment_project_category_id": self.id(), "name": self.name(), "project_id": self.projectId()}

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __eq__(self, other):
        if not isinstance(other, EquipmentProjectCategory):
            raise NotImplementedError(
                f"other: {other} can not be compared with EquipmentProjectCategory class"
            )
        return self.id() == other.id() and self.name() == other.name() and self.projectId() == other.projectId()
