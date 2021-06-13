"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.common.handler.project.maintenance.procedure.operation.MaintenanceProcedureOperationUpdatedHandler import (
    MaintenanceProcedureOperationUpdatedHandler as Handler,
)
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class ProjectDeletedHandler(Handler):
    def canHandle(self, name: str) -> bool:
        from src.domain_model.event.EventConstant import CommonEventConstant
        return name == CommonEventConstant.PROJECT_DELETED.value

    def handleMessage(self, messageData: dict, extraData: dict = None) -> dict:
        name = messageData["name"]
        data = messageData["data"]
        metadata = messageData["metadata"]

        logger.debug(
            f"[{ProjectDeletedHandler.handleMessage.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}"
        )
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
        return {
            "name": CommonCommandConstant.DELETE_BUILDING_BY_PROJECT_ID.value,
            "created_on": DateTimeHelper.utcNow(),
            "data": dataDict["new"],
            "metadata": metadataDict,
        }
