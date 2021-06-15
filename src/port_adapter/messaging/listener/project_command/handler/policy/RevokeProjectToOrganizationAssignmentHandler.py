from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.policy.RevokeProjectToOrganizationAssignmentHandler import (
    RevokeProjectToOrganizationAssignmentHandler as Handler,
)


class RevokeProjectToOrganizationAssignmentHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]
