"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.RoleApplicationService import RoleApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.project_command.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__CreateRoleHandler, "Create Role", "project command consumer", "Create Role")
c4model:Rel(project__messaging_project_command_handler__CreateRoleHandler, project__domainmodel_event__RoleCreated, "Role Created", "message")
"""
class CreateRoleHandler(Handler):

    def __init__(self):
        self._commandConstant = CommonCommandConstant.CREATE_ROLE

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{CreateRoleHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        appService: RoleApplicationService = AppDi.instance.get(RoleApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        appService.createRole(id=dataDict['id'], name=dataDict['name'], title=dataDict['title'],
                              token=metadataDict['token'])
        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': {'id': dataDict['id'], 'name': dataDict['name'], 'title': dataDict['title']},
                'metadata': metadataDict}

    def targetsOnSuccess(self):
        return [Handler.targetOnSuccess]

    def targetsOnException(self):
        return [Handler.targetOnException]
