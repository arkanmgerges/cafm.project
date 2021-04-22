"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.standard_equipment.standard_category.UpdateStandardEquipmentCategoryHandler import (
    UpdateStandardEquipmentCategoryHandler as Handler,
)


class UpdateStandardEquipmentCategoryHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
