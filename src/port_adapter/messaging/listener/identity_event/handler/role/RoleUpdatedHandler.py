"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from src.port_adapter.messaging.listener.common.handler.role.RoleUpdatedHandler import (
    RoleUpdatedHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__RoleUpdatedHandler, "CommonEventConstant.ROLE_UPDATED.value", "identity event consumer", "")
c4model:Rel(project__messaging_identity_event_handler__RoleUpdatedHandler, identity__domainmodel_event__RoleUpdated, "consume")
c4model:Rel(project__messaging_identity_event_handler__RoleUpdatedHandler, project__messaging_project_command_handler__UpdateRoleHandler, "CommonCommandConstant.UPDATE_ROLE.value", "message")
"""


class RoleUpdatedHandler(Handler):
    pass
