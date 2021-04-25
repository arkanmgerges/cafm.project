"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import json

import src.port_adapter.AppDi as AppDi
from src.application.DailyCheckProcedureOperationApplicationService import (
    DailyCheckProcedureOperationApplicationService,
)
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class UpdateDailyCheckProcedureOperationHandler(Handler):
    def __init__(self):
        self._commandConstant = (
            CommonCommandConstant.UPDATE_DAILY_CHECK_PROCEDURE_OPERATION
        )

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict, extraData: dict = None) -> dict:
        name = messageData["name"]
        data = messageData["data"]
        metadata = messageData["metadata"]

        logger.debug(
            f"[{UpdateDailyCheckProcedureOperationHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}"
        )

        appService: DailyCheckProcedureOperationApplicationService = AppDi.instance.get(
            DailyCheckProcedureOperationApplicationService
        )
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        id = (
            dataDict["daily_check_procedure_operation_id"]
            if "daily_check_procedure_operation_id" in dataDict
            else None
        )
        appService.updateDailyCheckProcedureOperation(
            id=id,
            name=dataDict["name"] if "name" in dataDict else None,
            description=dataDict["description"] if "description" in dataDict else None,
            type=dataDict["type"] if "type" in dataDict else None,
            dailyCheckProcedureId=dataDict["daily_check_procedure_id"]
            if "daily_check_procedure_id" in dataDict
            else None,
            token=metadataDict["token"],
        )
        return {
            "name": self._commandConstant.value,
            "created_on": DateTimeHelper.utcNow(),
            "data": dataDict,
            "metadata": metadataDict,
        }
