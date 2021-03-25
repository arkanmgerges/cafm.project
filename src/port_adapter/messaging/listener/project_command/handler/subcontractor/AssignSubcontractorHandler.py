"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.subcontractor.AssignSubcontractorHandler import \
    AssignSubcontractorHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__AssignSubcontractorHandler, "CommonCommandConstant.ASSIGN_SUBCONTRACTOR_TO_ORGANIZATION.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__AssignSubcontractorHandler, project__domainmodel_event__SubcontractorAssigned, "create")
"""


class AssignSubcontractorHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
