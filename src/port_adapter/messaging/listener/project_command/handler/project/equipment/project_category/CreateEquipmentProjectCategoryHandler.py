"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.equipment.project_category.CreateEquipmentProjectCategoryHandler import \
    CreateEquipmentProjectCategoryHandler as Handler


class CreateEquipmentProjectCategoryHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]