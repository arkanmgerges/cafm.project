"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.equipment.category.group.UpdateEquipmentCategoryGroupHandler import \
    UpdateEquipmentCategoryGroupHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__UpdateEquipmentCategoryGroupHandler, "CommonCommandConstant.UPDATE_EQUIPMENT_CATEGORY_GROUP.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__UpdateEquipmentCategoryGroupHandler, project__domainmodel_event__EquipmentCategoryGroupUpdated, "create", "message")
"""


class UpdateEquipmentCategoryGroupHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
