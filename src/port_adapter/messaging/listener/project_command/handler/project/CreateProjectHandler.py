"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.CreateProjectHandler import \
    CreateProjectHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__CreateProjectHandler, "CommonCommandConstant.CREATE_PROJECT.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__CreateProjectHandler, project__domainmodel_event__ProjectCreated, "create", "message")
"""


class CreateProjectHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
