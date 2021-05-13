"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
from copy import copy

import src.port_adapter.AppDi as AppDi
from src.application.EquipmentModelApplicationService import (
    EquipmentModelApplicationService,
)
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.common.Util import Util
from src.resource.logging.logger import logger


class CreateEquipmentModelHandler(Handler):
    def __init__(self):
        self._commandConstant = CommonCommandConstant.CREATE_EQUIPMENT_MODEL

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict, extraData: dict = None) -> dict:
        name = messageData["name"]
        data = messageData["data"]
        metadata = messageData["metadata"]

        logger.debug(
            f"[{CreateEquipmentModelHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}"
        )
        appService: EquipmentModelApplicationService = AppDi.instance.get(EquipmentModelApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        data = copy(dataDict)
        dataDict["id"] = dataDict.pop("equipment_model_id")
        appService.createEquipmentModel(**Util.snakeCaseToLowerCameCaseDict(dataDict), token=metadataDict["token"])
        return {
            "name": self._commandConstant.value,
            "created_on": DateTimeHelper.utcNow(),
            "data": data,
            "metadata": metadataDict,
        }
