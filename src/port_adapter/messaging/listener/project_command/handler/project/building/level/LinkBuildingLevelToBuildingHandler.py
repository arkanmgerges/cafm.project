"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.building.level.LinkBuildingLevelToBuildingHandler import \
    LinkBuildingLevelToBuildingHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__LinkBuildingLevelToBuildingHandler, "CommonCommandConstant.LINK_BUILDING_LEVEL_TO_BUILDING.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__LinkBuildingLevelToBuildingHandler, project__domainmodel_event__BuildingLevelToBuildingLinked, "create", "message")
"""


class LinkBuildingLevelToBuildingHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]