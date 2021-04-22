"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.UserApplicationService import UserApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class UpdateUserHandler(Handler):
    def __init__(self):
        self._commandConstant = CommonCommandConstant.UPDATE_USER

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData["name"]
        data = messageData["data"]
        metadata = messageData["metadata"]

        logger.debug(
            f"[{UpdateUserHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}"
        )
        appService: UserApplicationService = AppDi.instance.get(UserApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        appService.updateUser(
            id=dataDict["user_id"],
            email=dataDict["email"] if "email" in dataDict else None,
            firstName=dataDict["first_name"] if "first_name" in dataDict else None,
            lastName=dataDict["last_name"] if "last_name" in dataDict else None,
            addressOne=dataDict["address_one"] if "address_one" in dataDict else None,
            addressTwo=dataDict["address_two"] if "address_two" in dataDict else None,
            postalCode=dataDict["postal_code"] if "postal_code" in dataDict else None,
            phoneNumber=dataDict["phone_number"]
            if "phone_number" in dataDict
            else None,
            avatarImage=dataDict["avatar_image"]
            if "avatar_image" in dataDict
            else None,
            countryId=dataDict["country_id"] if "country_id" in dataDict else None,
            cityId=dataDict["city_id"] if "city_id" in dataDict else None,
            countryStateName=dataDict["country_state_name"]
            if "country_state_name" in dataDict
            else None,
            startDate=dataDict["start_date"] if "start_date" in dataDict else None,
            token=metadataDict["token"],
        )
        return {
            "name": self._commandConstant.value,
            "created_on": DateTimeHelper.utcNow(),
            "data": dataDict,
            "metadata": metadataDict,
        }
