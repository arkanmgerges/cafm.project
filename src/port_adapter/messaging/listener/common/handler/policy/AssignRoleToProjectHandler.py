"""
@author: Mohammad M. mmdii<mmdii@develoop.run>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.PolicyApplicationService import PolicyApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class AssignRoleToProjectHandler(Handler):
    def __init__(self):
        self._commandConstant = CommonCommandConstant.ASSIGN_ROLE_TO_PROJECT

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleMessage(self, messageData: dict, extraData: dict = None) -> dict:
        name = messageData["name"]
        data = messageData["data"]
        metadata = messageData["metadata"]

        logger.debug(
            f"[{AssignRoleToProjectHandler.handleMessage.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}"
        )
        appService: PolicyApplicationService = AppDi.instance.get(
            PolicyApplicationService
        )
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        appService.assignRoleToProject(
            roleId=dataDict["role_id"],
            projectId=dataDict["project_id"],
            token=metadataDict["token"],
        )

        appService.assignTagToRole(
            roleId=dataDict["role_id"],
            tagName="projectAccess",
            token=metadataDict["token"],
        )

        return {
            "name": self._commandConstant.value,
            "created_on": DateTimeHelper.utcNow(),
            "data": {
                "project_id": dataDict["project_id"],
                "role_id": dataDict["role_id"],
            },
            "metadata": metadataDict,
        }
