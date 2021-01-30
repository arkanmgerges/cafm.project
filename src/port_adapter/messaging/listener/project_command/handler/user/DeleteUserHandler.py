"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.messaging.listener.common.handler.user.DeleteUserHandler import DeleteUserHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__DeleteUserHandler, "CommonCommandConstant.DELETE_USER.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__DeleteUserHandler, project__domainmodel_event__UserDeleted, "create")
"""


class DeleteUserHandler(Handler):
    pass
