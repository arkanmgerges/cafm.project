"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.OrganizationApplicationService import OrganizationApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.project_command.handler.Handler import Handler
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

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{UpdateOrganizationHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        appService: OrganizationApplicationService = AppDi.instance.get(OrganizationApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        appService.updateOrganization(id=dataDict['id'],
                                      name=dataDict['name'],
                                      websiteUrl=dataDict['website_url'],
                                      organizationType=dataDict['organization_type'],
                                      addressOne=dataDict['address_one'],
                                      addressTwo=dataDict['address_two'],
                                      postalCode=dataDict['postal_code'],
                                      countryId=dataDict['country_id'],
                                      cityId=dataDict['city_id'],
                                      countryStateName=dataDict['country_state_name'],
                                      managerFirstName=dataDict['manager_first_name'],
                                      managerLastName=dataDict['manager_last_name'],
                                      managerEmail=dataDict['manager_email'],
                                      managerPhoneNumber=dataDict['manager_phone_number'],
                                      managerAvatar=dataDict['manager_avatar'],
                                      token=metadataDict['token'])
        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': {'id': dataDict['id'],
                         'name': dataDict['name'],
                         'website_url': dataDict['website_url'],
                         'organization_type': dataDict['organization_type'],
                         'address_one': dataDict['address_one'],
                         'address_two': dataDict['address_two'],
                         'postal_code': dataDict['postal_code'],
                         'country_id': dataDict['country_id'],
                         'city_id': dataDict['city_id'],
                         'country_state_name': dataDict['country_state_name'],
                         'manager_first_name': dataDict['manager_first_name'],
                         'manager_last_name': dataDict['manager_last_name'],
                         'manager_email': dataDict['manager_email'],
                         'manager_phone_number': dataDict['manager_phone_number'],
                         'manager_avatar': dataDict['manager_avatar'],
                         },
                'metadata': metadataDict}

    def targetsOnSuccess(self):
        return [Handler.targetOnSuccess]

    def targetsOnException(self):
        return [Handler.targetOnException]
