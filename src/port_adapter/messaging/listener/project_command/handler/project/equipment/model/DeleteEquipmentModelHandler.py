"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.equipment.model.DeleteEquipmentModelHandler import \
    DeleteEquipmentModelHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__DeleteEquipmentModelHandler, "CommonCommandConstant.DELETE_EQUIPMENT_MODEL.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__DeleteEquipmentModelHandler, project__domainmodel_event__EquipmentModelDeleted, "create", "message")
"""


class DeleteEquipmentModelHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
