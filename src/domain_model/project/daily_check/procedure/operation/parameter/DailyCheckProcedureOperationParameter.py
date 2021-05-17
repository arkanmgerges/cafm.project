"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.common.HasToMap import HasToMap
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.resource.logging.logger import logger

from uuid import uuid4


class DailyCheckProcedureOperationParameter(HasToMap):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        unitId: str = None,
        dailyCheckProcedureOperationId: str = None,
        minValue: float = None,
        maxValue: float = None,
        skipValidation: bool = False,
    ):
        self._id = str(uuid4()) if id is None else id
        self._name = name
        self._unitId = unitId
        self._dailyCheckProcedureOperationId = dailyCheckProcedureOperationId
        self._minValue = minValue
        self._maxValue = maxValue

        if not skipValidation:
            if name is None or name == "":
                from src.domain_model.resource.exception.InvalidArgumentException import (
                    InvalidArgumentException,
                )

                raise InvalidArgumentException(
                    f"Invalid daily check procedure operation parameter name: {name}, for daily check procedure operation parameter id: {id}"
                )
            if unitId is None or unitId == "":
                from src.domain_model.resource.exception.InvalidArgumentException import (
                    InvalidArgumentException,
                )

                raise InvalidArgumentException(
                    f"Invalid daily check procedure operation parameter unit_id: {unitId}, for daily check procedure operation parameter id: {id}"
                )
            if minValue is None or maxValue is None:
                from src.domain_model.resource.exception.InvalidArgumentException import (
                    InvalidArgumentException,
                )

                raise InvalidArgumentException(
                    f"Minimum and maximum values must be set. min. value: {minValue}, max. value: {maxValue}"
                )
            if minValue is not None and maxValue is not None:
                if maxValue < minValue:
                    from src.domain_model.resource.exception.InvalidArgumentException import (
                        InvalidArgumentException,
                    )

                    raise InvalidArgumentException(
                        f"maximum value must be equal or greater than minimum value, min. value: {minValue}, max. value: {maxValue}"
                    )
            if (
                dailyCheckProcedureOperationId is None
                or dailyCheckProcedureOperationId == ""
            ):
                from src.domain_model.resource.exception.InvalidArgumentException import (
                    InvalidArgumentException,
                )

                raise InvalidArgumentException(
                    f"Invalid daily check procedure operation parameter daily_check_procedure_operation_id: {dailyCheckProcedureOperationId}, for daily check procedure operation parameter id: {id}"
                )

    @classmethod
    def createFrom(
        cls,
        id: str = None,
        name: str = None,
        unitId: str = None,
        dailyCheckProcedureOperationId: str = None,
        minValue: float = None,
        maxValue: float = None,
        publishEvent: bool = False,
        skipValidation: bool = False,
        **_kwargs,
    ):
        from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameterCreated import (
            DailyCheckProcedureOperationParameterCreated,
        )

        obj = DailyCheckProcedureOperationParameter(
            id=id,
            name=name,
            unitId=unitId,
            dailyCheckProcedureOperationId=dailyCheckProcedureOperationId,
            minValue=minValue,
            maxValue=maxValue,
            skipValidation=skipValidation,
        )

        if publishEvent:
            logger.debug(
                f"[{DailyCheckProcedureOperationParameter.createFrom.__qualname__}] - Create daily check procedure operation parameter with id: {id}"
            )
            DomainPublishedEvents.addEventForPublishing(
                DailyCheckProcedureOperationParameterCreated(obj)
            )
        return obj

    @classmethod
    def createFromObject(
        cls,
        obj: "DailyCheckProcedureOperationParameter",
        publishEvent: bool = False,
        generateNewId: bool = False,
        skipValidation: bool = False,
    ):
        logger.debug(
            f"[{DailyCheckProcedureOperationParameter.createFromObject.__qualname__}]"
        )
        id = None if generateNewId else obj.id()
        return cls.createFrom(
            id=id,
            name=obj.name(),
            unitId=obj.unitId(),
            dailyCheckProcedureOperationId=obj.dailyCheckProcedureOperationId(),
            minValue=obj.minValue(),
            maxValue=obj.maxValue(),
            skipValidation=skipValidation,
            publishEvent=publishEvent,
        )

    def id(self) -> str:
        return self._id

    def name(self) -> str:
        return self._name

    def unitId(self) -> str:
        return self._unitId

    def dailyCheckProcedureOperationId(self) -> str:
        return self._dailyCheckProcedureOperationId

    def minValue(self) -> float:
        return self._minValue

    def maxValue(self) -> float:
        return self._maxValue

    def publishDelete(self):
        from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameterDeleted import (
            DailyCheckProcedureOperationParameterDeleted,
        )

        DomainPublishedEvents.addEventForPublishing(
            DailyCheckProcedureOperationParameterDeleted(self)
        )

    def publishUpdate(self, old):
        from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameterUpdated import (
            DailyCheckProcedureOperationParameterUpdated,
        )

        DomainPublishedEvents.addEventForPublishing(
            DailyCheckProcedureOperationParameterUpdated(old, self)
        )

    def toMap(self) -> dict:
        return {
            "daily_check_procedure_operation_parameter_id": self.id(),
            "name": self.name(),
            "unit_id": self.unitId(),
            "daily_check_procedure_operation_id": self.dailyCheckProcedureOperationId(),
            "min_value": self.minValue(),
            "max_value": self.maxValue(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __eq__(self, other):
        if not isinstance(other, DailyCheckProcedureOperationParameter):
            raise NotImplementedError(
                f"other: {other} can not be compared with DailyCheckProcedureOperationParameter class"
            )
        return (
            self.id() == other.id()
            and self.name() == other.name()
            and self.unitId() == other.unitId()
            and self.dailyCheckProcedureOperationId()
            == other.dailyCheckProcedureOperationId()
            and self.minValue() == other.minValue()
            and self.maxValue() == other.maxValue()
        )
