"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.policy.RevokeUserToOrganizationAssignmentHandler import (
    RevokeUserToOrganizationAssignmentHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__RevokeUserToOrganizationAssignmentHandler, "CommonCommandConstant.REVOKE_USER_TO_ORGANIZATION_ASSIGNMENT.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__RevokeUserToOrganizationAssignmentHandler, project__domainmodel_event__UserToOrganizationAssignmentRevoked, "create")
"""


class RevokeUserToOrganizationAssignmentHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
