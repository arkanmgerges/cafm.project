"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.organization.LinkOrganizationToBuildingHandler import (
    LinkOrganizationToBuildingHandler as Handler,
)

class LinkOrganizationToBuildingHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
