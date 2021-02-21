"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.equipment.project_category.CreateEquipmentProjectCategoryHandler import \
    CreateEquipmentProjectCategoryHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__CreateEquipmentProjectCategoryHandler, "CommonCommandConstant.CREATE_EQUIPMENT_PROJECT_CATEGORY.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__CreateEquipmentProjectCategoryHandler, project__domainmodel_event__EquipmentProjectCategoryCreated, "create", "message")
"""


class CreateEquipmentProjectCategoryHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
