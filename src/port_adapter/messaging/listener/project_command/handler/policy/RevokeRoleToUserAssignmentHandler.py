"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.policy.RevokeRoleToUserAssignmentHandler import (
    RevokeRoleToUserAssignmentHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__RevokeRoleToUserAssignmentHandler, "CommonCommandConstant.REVOKE_ROLE_TO_USER_ASSIGNMENT.value", "project command consumer", "Revoke Role to User Assignment")
c4model:Rel(project__messaging_project_command_handler__RevokeRoleToUserAssignmentHandler, project__domainmodel_event__RoleToUserAssignmentRevoked, "create")
"""


class RevokeRoleToUserAssignmentHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
