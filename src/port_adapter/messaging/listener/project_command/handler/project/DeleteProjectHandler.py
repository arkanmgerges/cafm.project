"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.messaging.listener.common.handler.project.DeleteProjectHandler import \
    DeleteProjectHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__DeleteProjectHandler, "CommonCommandConstant.DELETE_PROJECT.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__DeleteProjectHandler, project__domainmodel_event__ProjectDeleted, "create")
"""


class DeleteProjectHandler(Handler):
    pass
