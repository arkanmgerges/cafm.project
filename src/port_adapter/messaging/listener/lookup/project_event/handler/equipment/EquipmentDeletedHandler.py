"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.port_adapter.messaging.listener.common.handler.lookup.equipment.DeleteEquipmentHandler import (
    DeleteEquipmentHandler as Handler,
)

class EquipmentDeletedHandler(Handler):
    def canHandle(self, name: str) -> bool:
        from src.domain_model.event.EventConstant import CommonEventConstant
        return name == CommonEventConstant.EQUIPMENT_DELETED.value
