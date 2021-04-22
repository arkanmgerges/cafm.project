"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.messaging.listener.common.handler.policy.RoleToRealmAssignmentRevokedHandler import (
    RoleToRealmAssignmentRevokedHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__RoleToRealmAssignmentRevokedHandler, "CommonEventConstant.ROLE_TO_REALM_ASSIGNMENT_REVOKED.value", "identity event consumer", "")
c4model:Rel(project__messaging_identity_event_handler__RoleToRealmAssignmentRevokedHandler, identity__domainmodel_event__RoleToUserAssignmentRevoked, "consume")
c4model:Rel(project__messaging_identity_event_handler__RoleToRealmAssignmentRevokedHandler, project__messaging_project_command_handler__RevokeRoleToOrganizationAssignmentHandler, "CommonCommandConstant.REVOKE_ROLE_TO_ORGANIZATION_ASSIGNMENT.value", "message")
"""


class RoleToRealmAssignmentRevokedHandler(Handler):
    pass
