"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.organization.CreateOrganizationHandler import \
    CreateOrganizationHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__CreateOrganizationHandler, "CommonCommandConstant.CREATE_ORGANIZATION.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__CreateOrganizationHandler, project__domainmodel_event__OrganizationCreated, "create")
"""


class CreateOrganizationHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
