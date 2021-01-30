"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.messaging.listener.common.handler.policy.RoleToUserAssignmentRevokedHandler import \
    RoleToUserAssignmentRevokedHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__RoleToUserAssignmentRevokedHandler, "CommonEventConstant.ROLE_TO_USER_ASSIGNMENT_REVOKED.value", "identity event consumer", "")
c4model:Rel(project__messaging_identity_event_handler__RoleToUserAssignmentRevokedHandler, identity__domainmodel_event__RoleToUserAssignmentRevoked, "consume")
c4model:Rel(project__messaging_identity_event_handler__RoleToUserAssignmentRevokedHandler, project__messaging_project_command_handler__RevokeRoleToUserAssignmentHandler, "CommonCommandConstant.REVOKE_ROLE_TO_USER_ASSIGNMENT.value", "message")
"""


class RoleToUserAssignmentRevokedHandler(Handler):
    pass
