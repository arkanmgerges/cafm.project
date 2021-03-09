"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.user.UpdateUserHandler import UpdateUserHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__UpdateUserHandler, "CommonCommandConstant.UPDATE_USER.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__UpdateUserHandler, project__domainmodel_event__UserUpdated, "create")
"""


class UpdateUserHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]