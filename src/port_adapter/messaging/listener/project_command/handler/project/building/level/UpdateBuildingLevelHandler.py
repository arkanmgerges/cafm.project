"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.building.level.UpdateBuildingLevelHandler import \
    UpdateBuildingLevelHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__UpdateBuildingLevelHandler, "CommonCommandConstant.UPDATE_BUILDING_LEVEL.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__UpdateBuildingLevelHandler, project__domainmodel_event__BuildingLevelUpdated, "create", "message")
"""


class UpdateBuildingLevelHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]