"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.equipment.UpdateEquipmentHandler import \
    UpdateEquipmentHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__UpdateEquipmentHandler, "CommonCommandConstant.UPDATE_EQUIPMENT.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__UpdateEquipmentHandler, project__domainmodel_event__EquipmentUpdated, "create", "message")
"""


class UpdateEquipmentHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
