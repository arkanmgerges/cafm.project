"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4
from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.maintenance.procedure.operation.label.MaintenanceProcedureOperationLabel import MaintenanceProcedureOperationLabel


class MaintenanceProcedureOperationLabelDeleted(DomainEvent):
    def __init__(self, obj: MaintenanceProcedureOperationLabel):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.MAINTENANCE_PROCEDURE_OPERATION_LABEL_DELETED.value)
        self._data = obj.toMap()
