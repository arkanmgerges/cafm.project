"""
@author: Mohammad M. mmdii<mmdii@develoop.run>
"""
from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.policy.AssignRoleToProjectHandler import (
    AssignRoleToProjectHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__AssignRoleToProjectHandler, "CommonCommandConstant.ASSIGN_ROLE_TO_PROJECT.value", "project command consumer", "")
"""


class AssignRoleToProjectHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
