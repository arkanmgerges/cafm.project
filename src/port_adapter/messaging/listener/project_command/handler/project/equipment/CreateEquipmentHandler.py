"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.equipment.CreateEquipmentHandler import \
    CreateEquipmentHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__CreateEquipmentHandler, "CommonCommandConstant.CREATE_EQUIPMENT.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__CreateEquipmentHandler, project__domainmodel_event__EquipmentCreated, "create", "message")
"""


class CreateEquipmentHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
