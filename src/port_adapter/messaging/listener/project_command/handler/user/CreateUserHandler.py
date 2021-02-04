"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.user.CreateUserHandler import CreateUserHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__CreateUserHandler, "CommonCommandConstant.CREATE_USER.value", "project command consumer", "Create User")
c4model:Rel(project__messaging_project_command_handler__CreateUserHandler, project__domainmodel_event__UserCreated, "create")
"""


class CreateUserHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
