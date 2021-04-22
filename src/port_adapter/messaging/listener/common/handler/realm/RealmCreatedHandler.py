"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class RealmCreatedHandler(Handler):
    def __init__(self):
        self._eventConstant = CommonEventConstant.REALM_CREATED
        self._commandConstant = CommonCommandConstant.CREATE_ORGANIZATION

    def canHandle(self, name: str) -> bool:
        return name == self._eventConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData["name"]
        data = messageData["data"]
        metadata = messageData["metadata"]

        logger.debug(
            f"[{RealmCreatedHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}"
        )
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        return {
            "name": self._commandConstant.value,
            "created_on": DateTimeHelper.utcNow(),
            "data": {
                "organization_id": dataDict["realm_id"],
                "name": dataDict["name"],
                "organization_type": dataDict["realm_type"],
            },
            "metadata": metadataDict,
        }
