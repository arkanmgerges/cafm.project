"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.messaging.listener.common.handler.policy.UserToRealmAssignmentRevokedHandler import (
    UserToRealmAssignmentRevokedHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__UserToRealmAssignmentRevokedHandler, "CommonEventConstant.USER_TO_REALM_ASSIGNMENT_REVOKED.value", "identity event consumer", "")
c4model:Rel(project__messaging_identity_event_handler__UserToRealmAssignmentRevokedHandler, identity__domainmodel_event__UserToRealmAssignmentRevoked, "consume")
c4model:Rel(project__messaging_identity_event_handler__UserToRealmAssignmentRevokedHandler, project__messaging_project_command_handler__RevokeUserToOrganizationAssignmentHandler, "CommonCommandConstant.REVOKE_USER_TO_ORGANIZATION_ASSIGNMENT.value", "message")
"""


class UserToRealmAssignmentRevokedHandler(Handler):
    pass
