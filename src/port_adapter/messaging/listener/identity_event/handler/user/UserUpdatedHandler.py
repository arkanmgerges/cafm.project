"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.messaging.listener.common.handler.user.UserUpdatedHandler import UserUpdatedHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__UserUpdatedHandler, "CommonEventConstant.USER_UPDATED.value", "identity event consumer", "User updated")
c4model:Rel(project__messaging_identity_event_handler__UserUpdatedHandler, identity__domainmodel_event__UserUpdated, "consume")
c4model:Rel(project__messaging_identity_event_handler__UserUpdatedHandler, project__messaging_project_command_handler__UpdateUserHandler, "CommonCommandConstant.UPDATE_USER.value", "message")
"""


class UserUpdatedHandler(Handler):
    pass
