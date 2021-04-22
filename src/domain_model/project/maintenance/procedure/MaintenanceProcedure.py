"""
The file is generated by a scaffold script then modified manually
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureType import (
    MaintenanceProcedureType,
)
from src.resource.logging.logger import logger

from uuid import uuid4


class MaintenanceProcedure:
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: str = None,
        subType: str = None,
        frequency: str = None,
        startDate: int = None,
        equipmentId: str = None,
        subcontractorId: str = None,
        skipValidation: bool = False,
    ):
        if not skipValidation:
            # if name is None or name == '':
            #     from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
            #     raise InvalidArgumentException(
            #         f'Invalid maintenance procedure name: {name}, for maintenance procedure id: {id}')
            if type is None or type == "" or not self._isType(type):
                from src.domain_model.resource.exception.InvalidArgumentException import (
                    InvalidArgumentException,
                )

                raise InvalidArgumentException(
                    f"Invalid maintenance procedure type: {type}, for maintenance procedure id: {id}"
                )
            if frequency is None or frequency == "" or not self._isFrequency(frequency):
                from src.domain_model.resource.exception.InvalidArgumentException import (
                    InvalidArgumentException,
                )

                raise InvalidArgumentException(
                    f"Invalid maintenance procedure frequency: {frequency}, for maintenance procedure id: {id}"
                )
            if equipmentId is None or equipmentId == "":
                from src.domain_model.resource.exception.InvalidArgumentException import (
                    InvalidArgumentException,
                )

                raise InvalidArgumentException(
                    f"Invalid maintenance procedure equipment_id: {equipmentId}, for maintenance procedure id: {id}"
                )
            # TODO: put some validation for sub type
            # if type == MaintenanceProcedureType.HARD.value and (subType is None or subType == ''
            #                                               or not self._isSubType(subType)):
            #     from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
            #     raise InvalidArgumentException(
            #         f'Invalid maintenance procedure sub type: {subType}, for maintenance procedure id: {id}')

        self._id = str(uuid4()) if id is None else id
        self._name = name
        self._type = type
        self._subType = subType
        self._frequency = frequency
        self._startDate = startDate
        self._equipmentId = equipmentId
        self._subcontractorId = subcontractorId

    @classmethod
    def createFrom(
        cls,
        id: str = None,
        name: str = None,
        type: str = None,
        subType: str = None,
        frequency: str = None,
        startDate: int = None,
        equipmentId: str = None,
        subcontractorId: str = None,
        publishEvent: bool = False,
        skipValidation: bool = False,
    ):
        from src.domain_model.project.maintenance.procedure.MaintenanceProcedureCreated import (
            MaintenanceProcedureCreated,
        )

        obj = MaintenanceProcedure(
            id=id,
            name=name,
            type=type,
            subType=subType,
            frequency=frequency,
            startDate=startDate,
            equipmentId=equipmentId,
            subcontractorId=subcontractorId,
            skipValidation=skipValidation,
        )
        if publishEvent:
            logger.debug(
                f"[{MaintenanceProcedure.createFrom.__qualname__}] - Create maintenance procedure with id: {id}"
            )
            DomainPublishedEvents.addEventForPublishing(
                MaintenanceProcedureCreated(obj)
            )
        return obj

    @classmethod
    def createFromObject(
        cls,
        obj: "MaintenanceProcedure",
        publishEvent: bool = False,
        generateNewId: bool = False,
        skipValidation: bool = False,
    ):
        logger.debug(f"[{MaintenanceProcedure.createFromObject.__qualname__}]")
        id = None if generateNewId else obj.id()

        return cls.createFrom(
            id=id,
            name=obj.name(),
            type=obj.type(),
            subType=obj.subType(),
            frequency=obj.frequency(),
            startDate=obj.startDate(),
            equipmentId=obj.equipmentId(),
            subcontractorId=obj.subcontractorId(),
            skipValidation=skipValidation,
            publishEvent=publishEvent,
        )

    def id(self) -> str:
        return self._id

    def name(self) -> str:
        return self._name

    def type(self) -> str:
        return self._type

    def subType(self) -> str:
        return self._subType

    def frequency(self) -> str:
        return self._frequency

    def startDate(self) -> int:
        return self._startDate

    def subcontractorId(self) -> str:
        return self._subcontractorId

    def equipmentId(self) -> str:
        return self._equipmentId

    def publishDelete(self):
        from src.domain_model.project.maintenance.procedure.MaintenanceProcedureDeleted import (
            MaintenanceProcedureDeleted,
        )

        DomainPublishedEvents.addEventForPublishing(MaintenanceProcedureDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.project.maintenance.procedure.MaintenanceProcedureUpdated import (
            MaintenanceProcedureUpdated,
        )

        DomainPublishedEvents.addEventForPublishing(
            MaintenanceProcedureUpdated(old, self)
        )

    def _isType(self, type) -> bool:
        return type in MaintenanceProcedureType._value2member_map_

    def _isSubType(self, subType) -> bool:
        from src.domain_model.project.maintenance.procedure.MaintenanceProcedureHardSubType import (
            MaintenanceProcedureHardSubType,
        )

        return subType in MaintenanceProcedureHardSubType._value2member_map_

    def _isFrequency(self, frequency: str) -> bool:
        from src.domain_model.project.maintenance.procedure.MaintenanceProcedureFrequency import (
            MaintenanceProcedureFrequency,
        )

        return frequency in MaintenanceProcedureFrequency._value2member_map_

    def toMap(self) -> dict:
        return {
            "maintenance_procedure_id": self.id(),
            "name": self.name(),
            "type": self.type(),
            "frequency": self.frequency(),
            "start_date": self.startDate(),
            "equipment_id": self.equipmentId(),
            "subcontractor_id": self.subcontractorId(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __eq__(self, other):
        if not isinstance(other, MaintenanceProcedure):
            raise NotImplementedError(
                f"other: {other} can not be compared with MaintenanceProcedure class"
            )
        return (
            self.id() == other.id()
            and self.name() == other.name()
            and self.type() == other.type()
            and self.frequency() == other.frequency()
            and self.startDate() == other.startDate()
            and self.subcontractorId() == other.subcontractorId()
            and self.equipmentId() == other.equipmentId()
        )
