"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.building.UpdateBuildingHandler import \
    UpdateBuildingHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__UpdateBuildingHandler, "CommonCommandConstant.UPDATE_BUILDING.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__UpdateBuildingHandler, project__domainmodel_event__BuildingUpdated, "create", "message")
"""


class UpdateBuildingHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]