"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from src.port_adapter.messaging.listener.common.handler.lookup.equipment.CreateBuildingLevelHandler import \
    CreateBuildingLevelHandler as Handler


class BuildingLevelCreatedHandler(Handler):
    def canHandle(self, name: str) -> bool:
        from src.domain_model.event.EventConstant import CommonEventConstant
        return name == CommonEventConstant.BUILDING_LEVEL_CREATED.value