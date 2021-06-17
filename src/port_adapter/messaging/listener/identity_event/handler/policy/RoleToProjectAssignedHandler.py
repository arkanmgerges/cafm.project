"""
@author: Mohammad M. mmdii<mmdii@develoop.run>
"""
from src.port_adapter.messaging.listener.common.handler.policy.RoleToProjectAssignedHandler import (
    RoleToProjectAssignedHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__RoleToProjectAssignedHandler, "CommonEventConstant.ROLE_TO_PROJECT_ASSIGNED.value", "identity event consumer", "")
c4model:Rel(project__messaging_identity_event_handler__RoleToProjectAssignedHandler, identity__domainmodel_event__RoleToProjectAssigned, "consume")
c4model:Rel(project__messaging_identity_event_handler__RoleToProjectAssignedHandler, project__messaging_project_command_handler__AssignRoleToProjectHandler, "CommonCommandConstant.ASSIGN_ROLE_TO_PROJECT.value", "message")
"""


class RoleToProjectAssignedHandler(Handler):
    pass
