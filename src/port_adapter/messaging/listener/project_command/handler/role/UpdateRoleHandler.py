"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.role.UpdateRoleHandler import (
    UpdateRoleHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__UpdateRoleHandler, "CommonCommandConstant.UPDATE_ROLE.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__UpdateRoleHandler, project__domainmodel_event__RoleUpdated, "update")
"""


class UpdateRoleHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
