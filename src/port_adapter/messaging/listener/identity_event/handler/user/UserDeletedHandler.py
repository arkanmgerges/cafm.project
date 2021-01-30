"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.messaging.listener.common.handler.user.UserDeletedHandler import UserDeletedHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__UserDeletedHandler, "CommonEventConstant.USER_DELETED.value", "identity event consumer", "")
c4model:Rel(project__messaging_identity_event_handler__UserDeletedHandler, identity__domainmodel_event__UserDeleted, "consume")
c4model:Rel(project__messaging_identity_event_handler__UserDeletedHandler, project__messaging_project_command_handler__DeleteUserHandler, "CommonCommandConstant.DELETE_USER.value", "message")
"""


class UserDeletedHandler(Handler):
    pass
