"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4
from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.daily_check.procedure.operation.label.DailyCheckProcedureOperationLabel import DailyCheckProcedureOperationLabel


class DailyCheckProcedureOperationLabelCreated(DomainEvent):
    def __init__(self, obj: DailyCheckProcedureOperationLabel):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.DAILY_CHECK_PROCEDURE_OPERATION_LABEL_CREATED.value)
        self._data = obj.toMap()
