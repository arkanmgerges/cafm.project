"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4
from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameter import (
    DailyCheckProcedureOperationParameter,
)


class DailyCheckProcedureOperationParameterDeleted(DomainEvent):
    def __init__(self, obj: DailyCheckProcedureOperationParameter):
        super().__init__(
            id=str(uuid4()),
            name=CommonEventConstant.DAILY_CHECK_PROCEDURE_OPERATION_PARAMETER_DELETED.value,
        )
        self._data = obj.toMap()
