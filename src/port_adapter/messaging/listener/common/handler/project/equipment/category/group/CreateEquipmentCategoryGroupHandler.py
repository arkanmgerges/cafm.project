"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.EquipmentCategoryGroupApplicationService import EquipmentCategoryGroupApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class CreateEquipmentCategoryGroupHandler(Handler):

    def __init__(self):
        self._commandConstant = CommonCommandConstant.CREATE_EQUIPMENT_CATEGORY_GROUP

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{CreateEquipmentCategoryGroupHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        appService: EquipmentCategoryGroupApplicationService = AppDi.instance.get(EquipmentCategoryGroupApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        id = dataDict['equipment_category_group_id'] if 'equipment_category_group_id' in dataDict else None
        obj = appService.createEquipmentCategoryGroup(id=id,
                                                      name=dataDict['name'],
                                                      equipmentCategoryId=dataDict['equipment_category_id'],
                                                      token=metadataDict['token'])
        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': {'id': obj.id(), 'name': obj.name(), 'equipment_category_id': obj.equipmentCategoryId()},
                'metadata': metadataDict}