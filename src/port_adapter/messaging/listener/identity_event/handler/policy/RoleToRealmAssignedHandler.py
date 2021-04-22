"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from src.port_adapter.messaging.listener.common.handler.policy.RoleToRealmAssignedHandler import \
    RoleToRealmAssignedHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__RoleToRealmAssignedHandler, "CommonEventConstant.ROLE_TO_REALM_ASSIGNED.value", "identity event consumer", "")
c4model:Rel(project__messaging_identity_event_handler__RoleToRealmAssignedHandler, identity__domainmodel_event__RoleToRealmAssigned, "consume")
c4model:Rel(project__messaging_identity_event_handler__RoleToRealmAssignedHandler, project__messaging_project_command_handler__AssignRoleToOrganizationHandler, "CommonCommandConstant.ASSIGN_ROLE_TO_ORGANIZATION.value", "message")
"""


class RoleToRealmAssignedHandler(Handler):
    pass
