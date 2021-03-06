"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.resource.logging.logger import logger
from src.domain_model.common.HasToMap import HasToMap

from uuid import uuid4


class StandardEquipmentProjectCategory(HasToMap):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        organizationId: str = None,
        skipValidation: bool = False,
    ):
        if not skipValidation:
            if name is None or name == "":
                from src.domain_model.resource.exception.InvalidArgumentException import (
                    InvalidArgumentException,
                )

                raise InvalidArgumentException(
                    f"Invalid standard equipment project category name: {name}, for standard equipment project category id: {id}"
                )
            # if organizationId is None or organizationId == "":
            #     from src.domain_model.resource.exception.InvalidArgumentException import (
            #         InvalidArgumentException,
            #     )

            #     raise InvalidArgumentException(
            #         f"Invalid standard equipment project category organization_id: {organizationId}, for standard equipment project category id: {id}"
            #     )

        self._id = str(uuid4()) if id is None else id
        self._name = name
        self._organizationId = organizationId

    @classmethod
    def createFrom(
        cls,
        id: str = None,
        name: str = None,
        organizationId: str = None,
        publishEvent: bool = False,
        skipValidation: bool = False,
        **_kwargs,
    ):
        from src.domain_model.project.standard_equipment.standard_project.standard_category.StandardEquipmentProjectCategoryCreated import (
            StandardEquipmentProjectCategoryCreated,
        )

        obj = StandardEquipmentProjectCategory(
            id=id,
            name=name,
            organizationId=organizationId,
            skipValidation=skipValidation,
        )
        logger.debug(
            f"[{StandardEquipmentProjectCategory.createFrom.__qualname__}] - data: {obj.toMap()} event: {publishEvent}"
        )
        if publishEvent:
            logger.debug(
                f"[{StandardEquipmentProjectCategory.createFrom.__qualname__}] - Create standard equipment project category with id: {id}"
            )
            DomainPublishedEvents.addEventForPublishing(
                StandardEquipmentProjectCategoryCreated(obj)
            )
        return obj

    @classmethod
    def createFromObject(
        cls,
        obj: "StandardEquipmentProjectCategory",
        publishEvent: bool = False,
        generateNewId: bool = False,
        skipValidation: bool = False,
    ):
        logger.debug(
            f"[{StandardEquipmentProjectCategory.createFromObject.__qualname__}]"
        )
        id = None if generateNewId else obj.id()
        return cls.createFrom(
            id=id,
            name=obj.name(),
            organizationId=obj.organizationId(),
            skipValidation=skipValidation,
            publishEvent=publishEvent,
        )

    def id(self) -> str:
        return self._id

    def name(self) -> str:
        return self._name

    def organizationId(self) -> str:
        return self._organizationId

    def publishDelete(self):
        from src.domain_model.project.standard_equipment.standard_project.standard_category.StandardEquipmentProjectCategoryDeleted import (
            StandardEquipmentProjectCategoryDeleted,
        )

        DomainPublishedEvents.addEventForPublishing(
            StandardEquipmentProjectCategoryDeleted(self)
        )

    def publishUpdate(self, old):
        from src.domain_model.project.standard_equipment.standard_project.standard_category.StandardEquipmentProjectCategoryUpdated import (
            StandardEquipmentProjectCategoryUpdated,
        )

        DomainPublishedEvents.addEventForPublishing(
            StandardEquipmentProjectCategoryUpdated(old, self)
        )

    def toMap(self) -> dict:
        return {
            "standard_equipment_project_category_id": self.id(),
            "name": self.name(),
            "organization_id": self.organizationId(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __eq__(self, other):
        if not isinstance(other, StandardEquipmentProjectCategory):
            raise NotImplementedError(
                f"other: {other} can not be compared with StandardEquipmentProjectCategory class"
            )
        return (
            self.id() == other.id()
            and self.name() == other.name()
            and self.organizationId() == other.organizationId()
        )
