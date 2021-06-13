"""
@author: Mohammad S. moso<moso@develoop.run>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.ProjectApplicationService import ProjectApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.common.Util import Util
from src.resource.logging.logger import logger


class ChangeProjectStateHandler(Handler):
    def __init__(self):
        self._commandConstant = CommonCommandConstant.CHANGE_PROJECT_STATE

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleMessage(self, messageData: dict, extraData: dict = None) -> dict:
        name = messageData["name"]
        data = messageData["data"]
        metadata = messageData["metadata"]
        logger.debug(
            f"[{ChangeProjectStateHandler.handleMessage.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}"
        )
        appService: ProjectApplicationService = AppDi.instance.get(ProjectApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        appService.changeState(**Util.snakeCaseToLowerCameCaseDict(dataDict), token=metadataDict["token"])

        return {
            "name": self._commandConstant.value,
            "created_on": DateTimeHelper.utcNow(),
            "data": dataDict,
            "metadata": metadataDict,
        }
