"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.OrganizationApplicationService import OrganizationApplicationService
from src.domain_model.organization.Organization import Organization
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.project_command.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__CreateOrganizationHandler, "Create Organization", "project command consumer", "Create Organization")
c4model:Rel(project__messaging_project_command_handler__CreateOrganizationHandler, project__domainmodel_event__OrganizationCreated, "Organization Created", "message")
"""
class CreateOrganizationHandler(Handler):

    def __init__(self):
        self._commandConstant = CommonCommandConstant.CREATE_ORGANIZATION

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{CreateOrganizationHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        appService: OrganizationApplicationService = AppDi.instance.get(OrganizationApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        obj: Organization = appService.createOrganization(id=dataDict['id'], name=dataDict['name'],
                                                          organizationType=dataDict['organization_type'],
                                                          token=metadataDict['token'])
        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': {'id': obj.id(), 'name': obj.name(), 'organization_type': obj.organizationType()},
                'metadata': metadataDict}

    def targetsOnSuccess(self):
        return [Handler.targetOnSuccess]

    def targetsOnException(self):
        return [Handler.targetOnException]
