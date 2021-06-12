"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.port_adapter.messaging.listener.common.handler.lookup.equipment.maintenance_procedure.maintenance_procedure_operation.UpdateMaintenanceProcedureOperationHandler import (
    UpdateMaintenanceProcedureOperationHandler as Handler,
)


class MaintenanceProcedureOperationUpdatedHandler(Handler):
    def canHandle(self, name: str) -> bool:
        from src.domain_model.event.EventConstant import CommonEventConstant
        return name == CommonEventConstant.MAINTENANCE_PROCEDURE_OPERATION_UPDATED.value

    def handleCommand(self, messageData: dict, extraData: dict = None) -> dict:
        import json
        messageData['data'] = json.dumps(json.loads(messageData['data'])['new'])
        return super().handleCommand(messageData)