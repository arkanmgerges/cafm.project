"""
@author: Mohammad M. mmdii<mmdii@develoop.run>
"""
from src.port_adapter.messaging.listener.common.handler.policy.RoleToProjectAssignmentRevokedHandler import (
    RoleToProjectAssignmentRevokedHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__RoleToProjectAssignmentRevokedHandler, "CommonEventConstant.ROLE_TO_PROJECT_ASSIGNMENT_REVOKED.value", "identity event consumer", "")
c4model:Rel(project__messaging_identity_event_handler__RoleToProjectAssignmentRevokedHandler, identity__domainmodel_event__RoleToProjectAssignmentRevoked, "consume")
c4model:Rel(project__messaging_identity_event_handler__RoleToProjectAssignmentRevokedHandler, project__messaging_project_command_handler__RevokeRoleToProjectAssignmentHandler, "CommonCommandConstant.REVOKE_ROLE_TO_PROJECT_ASSIGNMENT.value", "message")
"""


class RoleToProjectAssignmentRevokedHandler(Handler):
    pass
