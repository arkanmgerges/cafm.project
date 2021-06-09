"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.port_adapter.messaging.listener.common.handler.lookup.equipment.maintenance_procedure.UpdateMaintenanceProcedureHandler import (
    UpdateMaintenanceProcedureHandler as Handler,
)

class MaintenanceProcedureUpdatedHandler(Handler):
    def canHandle(self, name: str) -> bool:
        from src.domain_model.event.EventConstant import CommonEventConstant
        return name == CommonEventConstant.MAINTENANCE_PROCEDURE_DELETED.value
