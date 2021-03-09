"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.role.CreateRoleHandler import CreateRoleHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__CreateRoleHandler, "CommonCommandConstant.CREATE_ROLE.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__CreateRoleHandler, project__domainmodel_event__RoleCreated, "create")
"""


class CreateRoleHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]