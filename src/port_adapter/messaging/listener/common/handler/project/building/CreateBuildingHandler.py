"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.BuildingApplicationService import BuildingApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class CreateBuildingHandler(Handler):
    def __init__(self):
        self._commandConstant = CommonCommandConstant.CREATE_BUILDING

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict, extraData: dict = None) -> dict:
        name = messageData["name"]
        data = messageData["data"]
        metadata = messageData["metadata"]

        logger.debug(
            f"[{CreateBuildingHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}"
        )

        appService: BuildingApplicationService = AppDi.instance.get(
            BuildingApplicationService
        )
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        id = dataDict["building_id"] if "building_id" in dataDict else None
        obj = appService.createBuilding(
            id=id,
            projectId=dataDict["project_id"],
            name=dataDict["name"],
            token=metadataDict["token"],
        )
        data = dataDict
        data["building_id"] = obj.id()
        return {
            "name": self._commandConstant.value,
            "created_on": DateTimeHelper.utcNow(),
            "data": data,
            "metadata": metadataDict,
        }
