"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.manufacturer.UpdateManufacturerHandler import \
    UpdateManufacturerHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__UpdateManufacturerHandler, "CommonCommandConstant.UPDATE_MANUFACTURER.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__UpdateManufacturerHandler, project__domainmodel_event__ManufacturerUpdated, "create", "message")
"""


class UpdateManufacturerHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
