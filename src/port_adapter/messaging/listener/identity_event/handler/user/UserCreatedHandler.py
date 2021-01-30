"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.messaging.listener.common.handler.user.UserCreatedHandler import UserCreatedHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__UserCreatedHandler, "CommonEventConstant.USER_CREATED.value", "identity event consumer", "")
c4model:Rel(project__messaging_identity_event_handler__UserCreatedHandler, identity__domainmodel_event__UserCreated, "consume")
c4model:Rel(project__messaging_identity_event_handler__UserCreatedHandler, project__messaging_project_command_handler__CreateUserHandler, "CommonCommandConstant.CREATE_USER.value", "message")
"""


class UserCreatedHandler(Handler):
    pass
