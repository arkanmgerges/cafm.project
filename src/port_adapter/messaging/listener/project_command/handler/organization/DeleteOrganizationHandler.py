"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.messaging.listener.common.handler.organization.DeleteOrganizationHandler import \
    DeleteOrganizationHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__DeleteOrganizationHandler, "CommonCommandConstant.DELETE_ORGANIZATION.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__DeleteOrganizationHandler, project__domainmodel_event__OrganizationDeleted, "create")
"""


class DeleteOrganizationHandler(Handler):
    pass
