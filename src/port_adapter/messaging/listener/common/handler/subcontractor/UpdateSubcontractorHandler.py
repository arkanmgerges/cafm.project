"""
@author: Mohammad S. moso<moso@develoop.run>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.SubcontractorApplicationService import (
    SubcontractorApplicationService,
)
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__UpdateSubcontractorHandler, "Update Organization", "project command consumer", "Update Subcontractor")
c4model:Rel(project__messaging_project_command_handler__UpdateSubcontractorHandler, project__domainmodel_event__SubcontractorUpdated, "Subcontractor Updated", "message")
"""


class UpdateSubcontractorHandler(Handler):
    def __init__(self):
        self._commandConstant = CommonCommandConstant.UPDATE_SUBCONTRACTOR

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict, extraData: dict = None) -> dict:
        name = messageData["name"]
        data = messageData["data"]
        metadata = messageData["metadata"]
        logger.debug(
            f"[{UpdateSubcontractorHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}"
        )
        appService: SubcontractorApplicationService = AppDi.instance.get(
            SubcontractorApplicationService
        )
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        appService.updateSubcontractor(
            id=dataDict["subcontractor_id"],
            companyName=dataDict["company_name"]
            if "company_name" in dataDict
            else None,
            websiteUrl=dataDict["website_url"] if "website_url" in dataDict else None,
            contactPerson=dataDict["contact_person"]
            if "contact_person" in dataDict
            else None,
            email=dataDict["email"] if "email" in dataDict else None,
            phoneNumber=dataDict["phone_number"]
            if "phone_number" in dataDict
            else None,
            subcontractorCategoryId=dataDict["subcontractor_category_id"]
            if "subcontractor_category_id" in dataDict
            else None,
            addressOne=dataDict["address_one"] if "address_one" in dataDict else None,
            addressTwo=dataDict["address_two"] if "address_two" in dataDict else None,
            token=metadataDict["token"],
        )
        return {
            "name": self._commandConstant.value,
            "created_on": DateTimeHelper.utcNow(),
            "data": dataDict,
            "metadata": metadataDict,
        }
