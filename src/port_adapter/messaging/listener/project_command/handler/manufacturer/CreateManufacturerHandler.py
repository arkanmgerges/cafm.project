"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.manufacturer.CreateManufacturerHandler import \
    CreateManufacturerHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__CreateManufacturerHandler, "CommonCommandConstant.CREATE_MANUFACTURER.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__CreateManufacturerHandler, project__domainmodel_event__ManufacturerCreated, "create", "message")
"""


class CreateManufacturerHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
