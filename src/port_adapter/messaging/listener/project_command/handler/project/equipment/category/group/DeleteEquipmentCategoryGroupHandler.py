"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.equipment.category.group.DeleteEquipmentCategoryGroupHandler import \
    DeleteEquipmentCategoryGroupHandler as Handler


class DeleteEquipmentCategoryGroupHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]
