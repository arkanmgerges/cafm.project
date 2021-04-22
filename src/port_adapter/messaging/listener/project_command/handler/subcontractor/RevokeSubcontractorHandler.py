"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.subcontractor.RevokeSubcontractorHandler import (
    RevokeSubcontractorHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__RevokeSubcontractorHandler, "CommonCommandConstant.REVOKE_ASSIGNMENT_SUBCONTRACTOR_TO_ORGANIZATION", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__RevokeSubcontractorHandler, project__domainmodel_event__SubcontractorRevoked, "create")
"""


class RevokeSubcontractorHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
