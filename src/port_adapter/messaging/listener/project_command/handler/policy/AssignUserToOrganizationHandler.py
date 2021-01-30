"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.messaging.listener.common.handler.policy.AssignUserToOrganizationHandler import \
    AssignUserToOrganizationHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__AssignUserToOrganizationHandler, "CommonCommandConstant.ASSIGN_USER_TO_ORGANIZATION.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__AssignUserToOrganizationHandler, project__domainmodel_event__UserToOrganizationAssigned, "create")
"""


class AssignUserToOrganizationHandler(Handler):
    pass
