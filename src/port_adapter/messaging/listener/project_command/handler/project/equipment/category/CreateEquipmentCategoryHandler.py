"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.equipment.category.CreateEquipmentCategoryHandler import \
    CreateEquipmentCategoryHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__CreateEquipmentCategoryHandler, "CommonCommandConstant.CREATE_EQUIPMENT_CATEGORY.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__CreateEquipmentCategoryHandler, project__domainmodel_event__EquipmentCategoryCreated, "create", "message")
"""


class CreateEquipmentCategoryHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
