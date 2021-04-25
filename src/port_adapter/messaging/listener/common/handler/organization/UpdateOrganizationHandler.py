"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

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
from src.resource.logging.logger import logger

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__UpdateOrganizationHandler, "Update Organization", "project command consumer", "Update Organization")
c4model:Rel(project__messaging_project_command_handler__UpdateOrganizationHandler, project__domainmodel_event__OrganizationUpdated, "Organization Updated", "message")
"""


class UpdateOrganizationHandler(Handler):
    def __init__(self):
        self._commandConstant = CommonCommandConstant.UPDATE_ORGANIZATION

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict, extraData: dict = None) -> dict:
        name = messageData["name"]
        data = messageData["data"]
        metadata = messageData["metadata"]

        logger.debug(
            f"[{UpdateOrganizationHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}"
        )
        appService: OrganizationApplicationService = AppDi.instance.get(
            OrganizationApplicationService
        )
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        appService.updateOrganization(
            id=dataDict["organization_id"],
            name=dataDict["name"] if "name" in dataDict else None,
            websiteUrl=dataDict["website_url"] if "website_url" in dataDict else None,
            organizationType=dataDict["organization_type"]
            if "organization_type" in dataDict
            else None,
            addressOne=dataDict["address_one"] if "address_one" in dataDict else None,
            addressTwo=dataDict["address_two"] if "address_two" in dataDict else None,
            postalCode=dataDict["postal_code"] if "postal_code" in dataDict else None,
            countryId=dataDict["country_id"] if "country_id" in dataDict else None,
            cityId=dataDict["city_id"] if "city_id" in dataDict else None,
            countryStateName=dataDict["country_state_name"]
            if "country_state_name" in dataDict
            else None,
            managerFirstName=dataDict["manager_first_name"]
            if "manager_first_name" in dataDict
            else None,
            managerLastName=dataDict["manager_last_name"]
            if "manager_last_name" in dataDict
            else None,
            managerEmail=dataDict["manager_email"]
            if "manager_email" in dataDict
            else None,
            managerPhoneNumber=dataDict["manager_phone_number"]
            if "manager_phone_number" in dataDict
            else None,
            managerAvatar=dataDict["manager_avatar"]
            if "manager_avatar" in dataDict
            else None,
            token=metadataDict["token"],
        )
        return {
            "name": self._commandConstant.value,
            "created_on": DateTimeHelper.utcNow(),
            "data": dataDict,
            "metadata": metadataDict,
        }
