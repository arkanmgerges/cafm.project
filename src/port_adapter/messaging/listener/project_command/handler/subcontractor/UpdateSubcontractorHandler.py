"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.subcontractor.UpdateSubcontractorHandler import (
    UpdateSubcontractorHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__UpdateSubcontractorHandler, "CommonCommandConstant.UPDATE_SUBCONTRACTOR.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__UpdateSubcontractorHandler, project__domainmodel_event__SubcontractorUpdated, "create")
"""


class UpdateSubcontractorHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
