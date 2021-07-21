"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.port_adapter.messaging.listener.common.handler.lookup.equipment.maintenance_procedure.\
    maintenance_procedure_operation.maintenance_procedure_operation_label.CreateMaintenanceProcedureOperationLabelHandler import (
    CreateMaintenanceProcedureOperationLabelHandler as Handler,
)


class MaintenanceProcedureOperationLabelCreatedHandler(Handler):
    def canHandle(self, name: str) -> bool:
        from src.domain_model.event.EventConstant import CommonEventConstant
        return name == CommonEventConstant.MAINTENANCE_PROCEDURE_OPERATION_LABEL_CREATED.value
