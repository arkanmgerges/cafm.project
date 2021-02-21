"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.equipment.category.group.CreateEquipmentCategoryGroupHandler import \
    CreateEquipmentCategoryGroupHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__CreateEquipmentCategoryGroupHandler, "CommonCommandConstant.CREATE_EQUIPMENT_CATEGORY_GROUP.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__CreateEquipmentCategoryGroupHandler, project__domainmodel_event__EquipmentCategoryGroupCreated, "create", "message")
"""


class CreateEquipmentCategoryGroupHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
