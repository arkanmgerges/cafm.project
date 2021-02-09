"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.building.level.CreateBuildingLevelHandler import \
    CreateBuildingLevelHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__CreateBuildingLevelHandler, "CommonCommandConstant.CREATE_BUILDING_LEVEL.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__CreateBuildingLevelHandler, project__domainmodel_event__BuildingLevelToBuildingAdded, "create", "message")
"""


class CreateBuildingLevelHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
