"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from typing import List, Callable

from src.port_adapter.messaging.listener.common.handler.project.daily_check.procedure.DeleteDailyCheckProcedureHandler import \
    DeleteDailyCheckProcedureHandler as Handler


class DeleteDailyCheckProcedureHandler(Handler):
    @staticmethod
    def targetsOnException() -> List[Callable]:
        return [Handler.targetOnException]

    @staticmethod
    def targetsOnSuccess() -> List[Callable]:
        return [Handler.targetOnSuccess]