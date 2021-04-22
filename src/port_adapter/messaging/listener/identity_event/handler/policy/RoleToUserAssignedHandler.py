"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.messaging.listener.common.handler.policy.RoleToUserAssignedHandler import (
    RoleToUserAssignedHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__RoleToUserAssignedHandler, "CommonEventConstant.ROLE_TO_USER_ASSIGNED.value", "identity event consumer", "")
c4model:Rel(project__messaging_identity_event_handler__RoleToUserAssignedHandler, identity__domainmodel_event__RoleToUserAssigned, "consume")
c4model:Rel(project__messaging_identity_event_handler__RoleToUserAssignedHandler, project__messaging_project_command_handler__AssignRoleToUserHandler, "CommonCommandConstant.ASSIGN_ROLE_TO_USER.value", "message")
"""


class RoleToUserAssignedHandler(Handler):
    pass
