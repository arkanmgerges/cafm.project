"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.organization.UpdateOrganizationHandler import \
    UpdateOrganizationHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__UpdateOrganizationHandler, "CommonCommandConstant.UPDATE_ORGANIZATION.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__UpdateOrganizationHandler, project__domainmodel_event__OrganizationUpdated, "create")
"""


class UpdateOrganizationHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
