"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.subcontractor.DeleteSubcontractorHandler import \
    DeleteSubcontractorHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__DeleteSubcontractorHandler, "CommonCommandConstant.DELETE_SUBCONTRACTOR.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__DeleteSubcontractorHandler, project__domainmodel_event__SubcontractorDeleted, "create")
"""


class DeleteSubcontractorHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
