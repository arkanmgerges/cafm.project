"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.messaging.listener.common.handler.project.ProjectDeletedHandler import \
    ProjectDeletedHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__ProjectDeletedHandler, "CommonEventConstant.PROJECT_DELETED.value", "identity event consumer", "Project deleted")
c4model:Rel(project__messaging_identity_event_handler__ProjectDeletedHandler, identity__domainmodel_event__ProjectDeleted, "consume")
c4model:Rel(project__messaging_identity_event_handler__ProjectDeletedHandler, project__messaging_project_command_handler__DeleteProjectHandler, "CommonCommandConstant.DELETE_PROJECT.value", "message")
"""


class ProjectDeletedHandler(Handler):
    pass
