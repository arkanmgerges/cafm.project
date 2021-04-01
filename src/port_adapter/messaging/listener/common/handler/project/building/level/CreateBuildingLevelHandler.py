"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.BuildingLevelApplicationService import BuildingLevelApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class CreateBuildingLevelHandler(Handler):

    def __init__(self):
        self._commandConstant = CommonCommandConstant.CREATE_BUILDING_LEVEL

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{CreateBuildingLevelHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')

        appService: BuildingLevelApplicationService = AppDi.instance.get(BuildingLevelApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        id = dataDict['building_level_id'] if 'building_level_id' in dataDict else None
        obj = appService.createBuildingLevel(id=id,
                                       buildingId=dataDict['building_id'],
                                       projectId=dataDict['project_id'],
                                       name=dataDict['name'],
                                       token=metadataDict['token'])
        data = dataDict
        data['building_level_id'] = obj.id()
        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': data,
                'metadata': metadataDict}
