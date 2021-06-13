"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.port_adapter.messaging.listener.common.handler.project.building.level.room.DeleteBuildingLevelRoomsByBuildingLevelIdHandler import (
    DeleteBuildingLevelRoomsByBuildingLevelIdHandler as Handler,
)


class BuildingLevelDeletedHandler(Handler):
    def canHandle(self, name: str) -> bool:
        from src.domain_model.event.EventConstant import CommonEventConstant
        return name == CommonEventConstant.BUILDING_LEVEL_DELETED.value

    def handleMessage(self, messageData: dict, extraData: dict = None) -> dict:
        super().handleMessage(messageData=messageData, extraData=extraData)
        return None