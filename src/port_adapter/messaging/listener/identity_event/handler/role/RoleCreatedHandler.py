"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.port_adapter.messaging.listener.common.handler.role.RoleCreatedHandler import (
    RoleCreatedHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__RoleCreatedHandler, "CommonEventConstant.ROLE_CREATED.value", "identity event consumer", "")
c4model:Rel(project__messaging_identity_event_handler__RoleCreatedHandler, identity__domainmodel_event__RoleCreated, "consume")
c4model:Rel(project__messaging_identity_event_handler__RoleCreatedHandler, project__messaging_project_command_handler__CreateRoleHandler, "CommonCommandConstant.CREATE_ROLE.value", "message")
"""


class RoleCreatedHandler(Handler):
    pass
