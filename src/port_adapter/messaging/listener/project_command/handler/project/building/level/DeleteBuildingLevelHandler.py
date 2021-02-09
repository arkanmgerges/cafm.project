"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.building.level.DeleteBuildingLevelHandler import \
    DeleteBuildingLevelHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__DeleteBuildingLevelHandler, "CommonCommandConstant.DELETE_BUILDING_LEVEL.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__DeleteBuildingLevelHandler, project__domainmodel_event__BuildingLevelToBuildingRemoved, "create", "message")
"""


class DeleteBuildingLevelHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
