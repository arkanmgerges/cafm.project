"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import time

import src.port_adapter.AppDi as AppDi
from src.application.UserApplicationService import UserApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.project_command.handler.Handler import Handler
from src.resource.logging.logger import logger


class UpdateUserHandler(Handler):

    def __init__(self):
        self._commandConstant = CommonCommandConstant.UPDATE_USER

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{UpdateUserHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        appService: UserApplicationService = AppDi.instance.get(UserApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        appService.updateUser(id=dataDict['id'], email=dataDict['email'], firstName=dataDict['first_name'],
                              lastName=dataDict['last_name'], addressOne=dataDict['address_one'],
                              addressTwo=dataDict['address_two'], postalCode=dataDict['postal_code'],
                              avatarImage=dataDict['avatar_image'],
                              token=metadataDict['token'])
        return {'name': self._commandConstant.value, 'created_on': round(time.time() * 1000),
                'data': {'id': dataDict['id'], 'email': dataDict['email'],
                         'first_name': dataDict['first_name'], 'last_name': dataDict['last_name'],
                         'address_one': dataDict['address_one'], 'address_two': dataDict['address_two'],
                         'postal_code': dataDict['postal_code'], 'avatar_image': dataDict['avatar_image']},
                'metadata': metadataDict}

    def targetsOnSuccess(self):
        return [Handler.targetOnSuccess]

    def targetsOnException(self):
        return [Handler.targetOnException]