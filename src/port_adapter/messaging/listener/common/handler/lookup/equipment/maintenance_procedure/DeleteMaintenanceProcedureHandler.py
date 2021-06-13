"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.lookup.equipment.MaintenanceProcedureApplicationService import \
    MaintenanceProcedureApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.Util import Util
from src.resource.logging.logger import logger


class DeleteMaintenanceProcedureHandler(Handler):
    def __init__(self):
        self._commandConstant = CommonCommandConstant.DELETE_MAINTENANCE_PROCEDURE

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleMessage(self, messageData: dict, extraData: dict = None) -> dict:
        name = messageData["name"]
        data = messageData["data"]
        metadata = messageData["metadata"]

        logger.debug(
            f"[{DeleteMaintenanceProcedureHandler.handleMessage.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}"
        )
        appService: MaintenanceProcedureApplicationService = AppDi.instance.get(MaintenanceProcedureApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        dataDict["id"] = dataDict.pop("maintenance_procedure_id")
        appService.deleteMaintenanceProcedure(
            **Util.snakeCaseToLowerCameCaseDict(dataDict),
            token=metadataDict["token"],
        )

        return None
