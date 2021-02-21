"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.equipment.category.UpdateEquipmentCategoryHandler import \
    UpdateEquipmentCategoryHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__UpdateEquipmentCategoryHandler, "CommonCommandConstant.UPDATE_EQUIPMENT_CATEGORY.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__UpdateEquipmentCategoryHandler, project__domainmodel_event__EquipmentCategoryUpdated, "create", "message")
"""


class UpdateEquipmentCategoryHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
