"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.building.level.UnlinkBuildingLevelFromBuildingHandler import \
    UnlinkBuildingLevelFromBuildingHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__UnlinkBuildingLevelFromBuildingHandler, "CommonCommandConstant.UNLINK_BUILDING_LEVEL_FROM_BUILDING.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__UnlinkBuildingLevelFromBuildingHandler, project__domainmodel_event__BuildingLevelToBuildingUnlinked, "create", "message")
"""


class UnlinkBuildingLevelFromBuildingHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
