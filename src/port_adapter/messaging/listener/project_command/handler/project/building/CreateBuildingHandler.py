"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.building.CreateBuildingHandler import (
    CreateBuildingHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__CreateBuildingHandler, "CommonCommandConstant.CREATE_BUILDING.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__CreateBuildingHandler, project__domainmodel_event__BuildingCreated, "create", "message")
"""


class CreateBuildingHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
