"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4
from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.standard_maintenance.procedure.operation.StandardMaintenanceProcedureOperation import (
    StandardMaintenanceProcedureOperation,
)


class StandardMaintenanceProcedureOperationUpdated(DomainEvent):
    def __init__(
        self,
        oldObj: StandardMaintenanceProcedureOperation,
        newObj: StandardMaintenanceProcedureOperation,
    ):
        super().__init__(
            id=str(uuid4()),
            name=CommonEventConstant.STANDARD_MAINTENANCE_PROCEDURE_OPERATION_UPDATED.value,
        )
        self._data = {"old": oldObj.toMap(), "new": newObj.toMap()}
