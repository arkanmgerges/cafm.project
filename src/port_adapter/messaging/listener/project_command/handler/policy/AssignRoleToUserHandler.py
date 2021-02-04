"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.policy.AssignRoleToUserHandler import \
    AssignRoleToUserHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__AssignRoleToUserHandler, "CommonCommandConstant.ASSIGN_ROLE_TO_USER.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__AssignRoleToUserHandler, project__domainmodel_event__RoleToUserAssigned, "create")
"""


class AssignRoleToUserHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
