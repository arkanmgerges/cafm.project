"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.common.HasToMap import HasToMap
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.resource.logging.logger import logger

from uuid import uuid4


class StandardEquipment(HasToMap):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        standardEquipmentCategoryId: str = None,
        standardEquipmentCategoryGroupId: str = None,
        manufacturerId: str = None,
        equipmentModelId: str = None,
        skipValidation: bool = False,
    ):
        if not skipValidation:
            if name is None or name == "":
                from src.domain_model.resource.exception.InvalidArgumentException import (
                    InvalidArgumentException,
                )

                raise InvalidArgumentException(
                    f"Invalid standard equipment name: {name}, for standard equipment id: {id}"
                )
            if standardEquipmentCategoryId is None or standardEquipmentCategoryId == "":
                from src.domain_model.resource.exception.InvalidArgumentException import (
                    InvalidArgumentException,
                )

                raise InvalidArgumentException(
                    f"Invalid standard equipment standard_equipment_category_id: {standardEquipmentCategoryId}, for standard equipment id: {id}"
                )
            if (
                standardEquipmentCategoryGroupId is None
                or standardEquipmentCategoryGroupId == ""
            ):
                from src.domain_model.resource.exception.InvalidArgumentException import (
                    InvalidArgumentException,
                )

                raise InvalidArgumentException(
                    f"Invalid standard equipment standard_equipment_category_group_id: {standardEquipmentCategoryGroupId}, for standard equipment id: {id}"
                )
            if manufacturerId is None or manufacturerId == "":
                from src.domain_model.resource.exception.InvalidArgumentException import (
                    InvalidArgumentException,
                )

                raise InvalidArgumentException(
                    f"Invalid standard equipment manufacturer_id: {manufacturerId}, for standard equipment id: {id}"
                )
            if equipmentModelId is None or equipmentModelId == "":
                from src.domain_model.resource.exception.InvalidArgumentException import (
                    InvalidArgumentException,
                )

                raise InvalidArgumentException(
                    f"Invalid standard equipment equipment_model_id: {equipmentModelId}, for standard equipment id: {id}"
                )

        self._id = str(uuid4()) if id is None else id
        self._name = name
        self._standardEquipmentCategoryId = standardEquipmentCategoryId
        self._standardEquipmentCategoryGroupId = standardEquipmentCategoryGroupId
        self._manufacturerId = manufacturerId
        self._equipmentModelId = equipmentModelId

    @classmethod
    def createFrom(
        cls,
        id: str = None,
        name: str = None,
        standardEquipmentCategoryId: str = None,
        standardEquipmentCategoryGroupId: str = None,
        manufacturerId: str = None,
        equipmentModelId: str = None,
        publishEvent: bool = False,
        skipValidation: bool = False,
    ):
        from src.domain_model.project.standard_equipment.StandardEquipmentCreated import (
            StandardEquipmentCreated,
        )

        obj = StandardEquipment(
            id=id,
            name=name,
            standardEquipmentCategoryId=standardEquipmentCategoryId,
            standardEquipmentCategoryGroupId=standardEquipmentCategoryGroupId,
            manufacturerId=manufacturerId,
            equipmentModelId=equipmentModelId,
            skipValidation=skipValidation,
        )

        if publishEvent:
            logger.debug(
                f"[{StandardEquipment.createFrom.__qualname__}] - Create standard equipment with id: {id}"
            )
            DomainPublishedEvents.addEventForPublishing(StandardEquipmentCreated(obj))
        return obj

    @classmethod
    def createFromObject(
        cls,
        obj: "StandardEquipment",
        publishEvent: bool = False,
        generateNewId: bool = False,
        skipValidation: bool = False,
    ):
        logger.debug(f"[{StandardEquipment.createFromObject.__qualname__}]")
        id = None if generateNewId else obj.id()
        return cls.createFrom(
            id=id,
            name=obj.name(),
            standardEquipmentCategoryId=obj.standardEquipmentCategoryId(),
            standardEquipmentCategoryGroupId=obj.standardEquipmentCategoryGroupId(),
            manufacturerId=obj.manufacturerId(),
            equipmentModelId=obj.equipmentModelId(),
            skipValidation=skipValidation,
            publishEvent=publishEvent,
        )

    def id(self) -> str:
        return self._id

    def name(self) -> str:
        return self._name

    def standardEquipmentCategoryId(self) -> str:
        return self._standardEquipmentCategoryId

    def standardEquipmentCategoryGroupId(self) -> str:
        return self._standardEquipmentCategoryGroupId

    def manufacturerId(self) -> str:
        return self._manufacturerId

    def equipmentModelId(self) -> str:
        return self._equipmentModelId

    def publishDelete(self):
        from src.domain_model.project.standard_equipment.StandardEquipmentDeleted import (
            StandardEquipmentDeleted,
        )

        DomainPublishedEvents.addEventForPublishing(StandardEquipmentDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.project.standard_equipment.StandardEquipmentUpdated import (
            StandardEquipmentUpdated,
        )

        DomainPublishedEvents.addEventForPublishing(StandardEquipmentUpdated(old, self))

    def toMap(self) -> dict:
        return {
            "standard_equipment_id": self.id(),
            "name": self.name(),
            "standard_equipment_category_id": self.standardEquipmentCategoryId(),
            "standard_equipment_category_group_id": self.standardEquipmentCategoryGroupId(),
            "manufacturer_id": self.manufacturerId(),
            "equipment_model_id": self.equipmentModelId(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __eq__(self, other):
        if not isinstance(other, StandardEquipment):
            raise NotImplementedError(
                f"other: {other} can not be compared with StandardEquipment class"
            )
        return (
            self.id() == other.id()
            and self.name() == other.name()
            and self.standardEquipmentCategoryId()
            == other.standardEquipmentCategoryId()
            and self.standardEquipmentCategoryGroupId()
            == other.standardEquipmentCategoryGroupId()
            and self.manufacturerId() == other.manufacturerId()
            and self.equipmentModelId() == other.equipmentModelId()
        )
