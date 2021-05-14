"""
@author: Mohammad S. moso<moso@develoop.run>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.SubcontractorLookupApplicationService import (
    SubcontractorLookupApplicationService,
)
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.Util import Util
from src.resource.logging.logger import logger


class CreateSubcontractorHandler(Handler):
    def __init__(self):
        self._commandConstant = CommonCommandConstant.CREATE_SUBCONTRACTOR

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict, extraData: dict = None) -> dict:
        name = messageData["name"]
        data = messageData["data"]
        metadata = messageData["metadata"]

        logger.debug(
            f"[{CreateSubcontractorHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}"
        )
        appService: SubcontractorLookupApplicationService = AppDi.instance.get(SubcontractorLookupApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        dataDict["id"] = dataDict.pop("subcontractor_id")
        appService.createSubcontractor(
            **Util.snakeCaseToLowerCameCaseDict(dataDict),
            token=metadataDict["token"],
        )
