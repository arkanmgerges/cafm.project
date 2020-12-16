"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import time

import src.port_adapter.AppDi as AppDi
from src.application.ProjectApplicationService import ProjectApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.EventConstant import CommonEventConstant
from src.port_adapter.messaging.listener.project_command.handler.Handler import Handler
from src.resource.logging.logger import logger


class ProjectCreatedHandler(Handler):

    def __init__(self):
        self._eventConstant = CommonEventConstant.PROJECT_CREATED

    def canHandle(self, name: str) -> bool:
        return name == self._eventConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{ProjectCreatedHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        appService: ProjectApplicationService = AppDi.instance.get(ProjectApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        obj = appService.createProject(id=dataDict['id'], name=dataDict['name'], token=metadataDict['token'],
                                       objectOnly=True)
        return {'name': CommonCommandConstant.CREATE_PROJECT.value, 'created_on': round(time.time() * 1000),
                'data': {'id': obj.id(), 'name': obj.name()},
                'metadata': metadataDict}
