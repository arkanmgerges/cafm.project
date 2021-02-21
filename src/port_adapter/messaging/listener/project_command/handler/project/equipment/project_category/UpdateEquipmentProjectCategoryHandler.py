"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.equipment.project_category.UpdateEquipmentProjectCategoryHandler import \
    UpdateEquipmentProjectCategoryHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__UpdateEquipmentProjectCategoryHandler, "CommonCommandConstant.UPDATE_EQUIPMENT_PROJECT_CATEGORY.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__UpdateEquipmentProjectCategoryHandler, project__domainmodel_event__EquipmentProjectCategoryUpdated, "create", "message")
"""


class UpdateEquipmentProjectCategoryHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
