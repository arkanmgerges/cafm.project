"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.lookup.equipment.MaintenanceProcedureOperationLabelApplicationService import \
    MaintenanceProcedureOperationLabelApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.Util import Util
from src.resource.logging.logger import logger


class CreateMaintenanceProcedureOperationLabelHandler(Handler):
    def __init__(self):
        self._commandConstant = CommonCommandConstant.CREATE_MAINTENANCE_PROCEDURE_OPERATION_LABEL

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleMessage(self, messageData: dict, extraData: dict = None) -> dict:
        name = messageData["name"]
        data = messageData["data"]
        metadata = messageData["metadata"]

        logger.debug(
            f"[{CreateMaintenanceProcedureOperationLabelHandler.handleMessage.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}"
        )
        appService: MaintenanceProcedureOperationLabelApplicationService = AppDi.instance.get(MaintenanceProcedureOperationLabelApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        dataDict["id"] = dataDict.pop("maintenance_procedure_operation_label_id")

        appService.createMaintenanceProcedureOperationLabel(
            **Util.snakeCaseToLowerCameCaseDict(dataDict),
            token=metadataDict["token"],
        )

        return None
