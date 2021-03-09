"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.building.DeleteBuildingHandler import \
    DeleteBuildingHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__DeleteBuildingHandler, "CommonCommandConstant.DELETE_BUILDING.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__DeleteBuildingHandler, project__domainmodel_event__BuildingDeleted, "create", "message")
"""


class DeleteBuildingHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]