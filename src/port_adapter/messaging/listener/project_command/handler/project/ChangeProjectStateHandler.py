"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.ChangeProjectStateHandler import (
    ChangeProjectStateHandler as Handler,
)


class ChangeProjectStateHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
