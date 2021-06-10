"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from src.port_adapter.messaging.listener.common.handler.lookup.equipment.UpdateManufacturerHandler import \
    UpdateManufacturerHandler as Handler


class ManufacturerUpdatedHandler(Handler):
    def canHandle(self, name: str) -> bool:
        from src.domain_model.event.EventConstant import CommonEventConstant
        return name == CommonEventConstant.MANUFACTURER_UPDATED.value