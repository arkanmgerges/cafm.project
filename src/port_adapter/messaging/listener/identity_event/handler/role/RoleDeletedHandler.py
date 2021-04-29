"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from src.port_adapter.messaging.listener.common.handler.role.RoleDeletedHandler import (
    RoleDeletedHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__RoleDeletedHandler, "CommonEventConstant.ROLE_DELETED.value", "identity event consumer", "")
c4model:Rel(project__messaging_identity_event_handler__RoleDeletedHandler, identity__domainmodel_event__RoleDeleted, "consume")
c4model:Rel(project__messaging_identity_event_handler__RoleDeletedHandler, project__messaging_project_command_handler__DeleteRoleHandler, "CommonCommandConstant.DELETE_ROLE.value", "message")
"""


class RoleDeletedHandler(Handler):
    pass
