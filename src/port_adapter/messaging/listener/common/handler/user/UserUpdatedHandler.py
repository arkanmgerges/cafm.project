"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class UserUpdatedHandler(Handler):

    def __init__(self):
        self._eventConstant = CommonEventConstant.USER_UPDATED
        self._commandConstant = CommonCommandConstant.UPDATE_USER

    def canHandle(self, name: str) -> bool:
        return name == self._eventConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{UserUpdatedHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        dataDict = json.loads(data)
        dataDict = dataDict['new']  # Get the new object
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': {'id': dataDict['id'],
                         'email': dataDict['email'],
                         'first_name': dataDict['first_name'],
                         'last_name': dataDict['last_name'],
                         'address_one': dataDict['address_one'],
                         'address_two': dataDict['address_two'],
                         'postal_code': dataDict['postal_code'],
                         'phone_number': dataDict['phone_number'],
                         'avatar_image': dataDict['avatar_image'],
                         'country_id': dataDict['country_id'],
                         'city_id': dataDict['city_id'],
                         'state_name': dataDict['state_name'],
                         'start_date': dataDict['start_date']
                         },
                'metadata': metadataDict}
