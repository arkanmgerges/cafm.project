"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.common.HasToMap import HasToMap
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.resource.exception.InvalidArgumentException import (
    InvalidArgumentException,
)
from src.resource.logging.logger import logger
from uuid import uuid4


class EquipmentCategoryGroup(HasToMap):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        equipmentCategoryId: str = None,
        skipValidation: bool = False,
    ):
        self._id = str(uuid4()) if id is None else id
        self._name = name
        self._equipmentCategoryId = equipmentCategoryId

        if not skipValidation:
            if name is None or name == "":
                raise InvalidArgumentException(
                    f"Invalid equipment category group name: {name}, for equipment category group id: {id}"
                )
            if equipmentCategoryId is None or equipmentCategoryId == "":
                raise InvalidArgumentException(
                    f"Invalid equipment category id: {equipmentCategoryId}, for equipment category group id: {id}"
                )

    @classmethod
    def createFrom(
        cls,
        id: str = None,
        name: str = "",
        equipmentCategoryId: str = None,
        publishEvent: bool = False,
        skipValidation: bool = False,
        **_kwargs,
    ):
        from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupCreated import (
            EquipmentCategoryGroupCreated,
        )

        obj = EquipmentCategoryGroup(
            id=id,
            name=name,
            equipmentCategoryId=equipmentCategoryId,
            skipValidation=skipValidation,
        )

        if publishEvent:
            logger.debug(
                f"[{EquipmentCategoryGroup.createFrom.__qualname__}] - Create equipment category group with id: {id}"
            )
            DomainPublishedEvents.addEventForPublishing(
                EquipmentCategoryGroupCreated(obj)
            )
        return obj

    @classmethod
    def createFromObject(
        cls,
        obj: "EquipmentCategoryGroup",
        publishEvent: bool = False,
        generateNewId: bool = False,
        skipValidation: bool = False,
    ):
        logger.debug(f"[{EquipmentCategoryGroup.createFromObject.__qualname__}]")
        id = None if generateNewId else obj.id()
        return cls.createFrom(
            id=id,
            name=obj.name(),
            equipmentCategoryId=obj.equipmentCategoryId(),
            skipValidation=skipValidation,
            publishEvent=publishEvent,
        )

    def id(self) -> str:
        return self._id

    def name(self) -> str:
        return self._name

    def equipmentCategoryId(self) -> str:
        return self._equipmentCategoryId

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
        from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupDeleted import (
            EquipmentCategoryGroupDeleted,
        )

        DomainPublishedEvents.addEventForPublishing(EquipmentCategoryGroupDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupUpdated import (
            EquipmentCategoryGroupUpdated,
        )

        DomainPublishedEvents.addEventForPublishing(
            EquipmentCategoryGroupUpdated(old, self)
        )

    def toMap(self) -> dict:
        return {
            "equipment_category_group_id": self.id(),
            "name": self.name(),
            "equipment_category_id": self.equipmentCategoryId(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __eq__(self, other):
        if not isinstance(other, EquipmentCategoryGroup):
            raise NotImplementedError(
                f"other: {other} can not be compared with EquipmentCategoryGroup class"
            )
        return (
            self.id() == other.id()
            and self.name() == other.name()
            and self.equipmentCategoryId() == other.equipmentCategoryId()
        )
