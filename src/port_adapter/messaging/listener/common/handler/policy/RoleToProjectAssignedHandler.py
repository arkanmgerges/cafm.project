"""
@author: Mohammad M. mmdii<mmdii@develoop.run>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.PolicyApplicationService import PolicyApplicationService

from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class RoleToProjectAssignedHandler(Handler):
    def __init__(self):
        self._eventConstant = CommonEventConstant.ROLE_TO_PROJECT_ASSIGNED
        self._commandConstant = CommonCommandConstant.ASSIGN_ROLE_TO_PROJECT

    def canHandle(self, name: str) -> bool:
        return name == self._eventConstant.value

    def handleMessage(self, messageData: dict, extraData: dict = None) -> dict:
        name = messageData["name"]
        data = messageData["data"]
        metadata = messageData["metadata"]

        logger.debug(
            f"[{RoleToProjectAssignedHandler.handleMessage.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}"
        )
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        appService: PolicyApplicationService = AppDi.instance.get(
            PolicyApplicationService
        )

        appService.assignRoleToProject(
            roleId=dataDict["role_id"],
            projectId=dataDict["project_id"],
            token=metadataDict["token"],
        )
        return None