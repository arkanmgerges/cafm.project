"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.policy.AssignRoleToOrganizationHandler import \
    AssignRoleToOrganizationHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__AssignRoleToOrganizationHandler, "CommonCommandConstant.ASSIGN_ROLE_TO_ORGANIZATION.value", "project command consumer", "")
"""


class AssignRoleToOrganizationHandler(Handler):

    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
