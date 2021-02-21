"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.equipment.DeleteEquipmentHandler import \
    DeleteEquipmentHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__DeleteEquipmentHandler, "CommonCommandConstant.DELETE_EQUIPMENT.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__DeleteEquipmentHandler, project__domainmodel_event__EquipmentDeleted, "create", "message")
"""


class DeleteEquipmentHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
