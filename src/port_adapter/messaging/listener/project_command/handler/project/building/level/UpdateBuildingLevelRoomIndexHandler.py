"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.building.level.UpdateBuildingLevelRoomIndexHandler import (
    UpdateBuildingLevelRoomIndexHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__UpdateBuildingLevelRoomIndexHandler, "CommonCommandConstant.UPDATE_BUILDING_LEVEL_ROOM_INDEX.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__UpdateBuildingLevelRoomIndexHandler, project__domainmodel_event__BuildingLevelRoomIndexUpdated, "create", "message")
"""


class UpdateBuildingLevelRoomIndexHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
