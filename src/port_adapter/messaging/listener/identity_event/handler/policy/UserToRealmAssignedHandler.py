"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.messaging.listener.common.handler.policy.UserToRealmAssignedHandler import \
    UserToRealmAssignedHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__UserToRealmAssignedHandler, "CommonEventConstant.USER_TO_REALM_ASSIGNED.value", "identity event consumer", "")
c4model:Rel(project__messaging_identity_event_handler__UserToRealmAssignedHandler, identity__domainmodel_event__UserToRealmAssigned, "consume")
c4model:Rel(project__messaging_identity_event_handler__UserToRealmAssignedHandler, project__messaging_project_command_handler__AssignUserToOrganizationHandler, "CommonCommandConstant.ASSIGN_USER_TO_ORGANIZATION.value", "message")
"""


class UserToRealmAssignedHandler(Handler):
    pass
