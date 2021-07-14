import json
from copy import copy

import src.port_adapter.AppDi as AppDi
from src.application.OrganizationApplicationService import (
    OrganizationApplicationService,
)
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.common.Util import Util
from src.resource.logging.logger import logger


class LinkOrganizationToBuildingHandler(Handler):
    def __init__(self):
        self._commandConstant = CommonCommandConstant.LINK_ORGANIZATION_BUILDING

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleMessage(self, messageData: dict, extraData: dict = None) -> dict:
        name = messageData["name"]
        data = messageData["data"]
        metadata = messageData["metadata"]

        logger.debug(
            f"[{LinkOrganizationToBuildingHandler.handleMessage.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}"
        )
        appService: OrganizationApplicationService = AppDi.instance.get(OrganizationApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        data = copy(dataDict)
        dataDict["id"] = dataDict.pop("organization_id")
        appService.linkOrganizationToBuilding(
            **Util.snakeCaseToLowerCameCaseDict(dataDict),
            token=metadataDict["token"],
        )
        return {
            "name": self._commandConstant.value,
            "created_on": DateTimeHelper.utcNow(),
            "data": data,
            "metadata": metadataDict,
        }
