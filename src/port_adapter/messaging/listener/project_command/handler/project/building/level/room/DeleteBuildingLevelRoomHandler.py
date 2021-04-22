"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.building.level.room.DeleteBuildingLevelRoomHandler import (
    DeleteBuildingLevelRoomHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__DeleteBuildingLevelRoomHandler, "CommonCommandConstant.DELETE_BUILDING_LEVEL_ROOM.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__DeleteBuildingLevelRoomHandler, project__domainmodel_event__BuildingLevelRoomFromBuildingLevelRemoved, "create", "message")
"""


class DeleteBuildingLevelRoomHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
