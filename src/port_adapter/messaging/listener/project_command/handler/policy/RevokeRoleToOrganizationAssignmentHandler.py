"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.policy.RevokeRoleToOrganizationAssignmentHandler import (
    RevokeRoleToOrganizationAssignmentHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__RevokeRoleToOrganizationAssignmentHandler, "CommonCommandConstant.REVOKE_ROLE_TO_ORGANIZATION_ASSIGNMENT.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__RevokeRoleToOrganizationAssignmentHandler, project__domainmodel_event__RoleToOrganizationAssignmentRevoked, "create")
"""


class RevokeRoleToOrganizationAssignmentHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
