"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.manufacturer.DeleteManufacturerHandler import \
    DeleteManufacturerHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__DeleteManufacturerHandler, "CommonCommandConstant.DELETE_MANUFACTURER.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__DeleteManufacturerHandler, project__domainmodel_event__ManufacturerDeleted, "create", "message")
"""


class DeleteManufacturerHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
