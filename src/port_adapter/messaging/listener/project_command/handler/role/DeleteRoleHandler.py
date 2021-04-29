"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.role.DeleteRoleHandler import (
    DeleteRoleHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__DeleteRoleHandler, "CommonCommandConstant.DELETE_ROLE.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__DeleteRoleHandler, project__domainmodel_event__RoleDeleted, "create")
"""


class DeleteRoleHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
