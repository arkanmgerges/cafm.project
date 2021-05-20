"""
@author: Mohammad M. mmdii<mmdii@develoop.run>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.policy.RevokeRoleToProjectAssignmentHandler import (
    RevokeRoleToProjectAssignmentHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__RevokeRoleToProjectAssignmentHandler, "CommonCommandConstant.REVOKE_ROLE_TO_PROJECT_ASSIGNMENT.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__RevokeRoleToProjectAssignmentHandler, project__domainmodel_event__RoleToProjectAssignmentRevoked, "create")
"""


class RevokeRoleToProjectAssignmentHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
