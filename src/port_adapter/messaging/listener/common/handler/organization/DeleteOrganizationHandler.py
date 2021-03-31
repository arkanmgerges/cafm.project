"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.UserApplicationService import UserApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__DeleteOrganizationHandler, "Delete Organization", "project command consumer", "Delete Organization")
c4model:Rel(project__messaging_project_command_handler__DeleteOrganizationHandler, project__domainmodel_event__OrganizationDeleted, "Organization Deleted", "message")
"""


class DeleteOrganizationHandler(Handler):

    def __init__(self):
        self._commandConstant = CommonCommandConstant.DELETE_ORGANIZATION

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{DeleteOrganizationHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        appService: UserApplicationService = AppDi.instance.get(UserApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        appService.deleteUser(id=dataDict['organization_id'], token=metadataDict['token'])
        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': dataDict,
                'metadata': metadataDict}
