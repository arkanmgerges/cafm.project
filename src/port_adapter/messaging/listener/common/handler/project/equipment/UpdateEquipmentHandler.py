"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.EquipmentApplicationService import EquipmentApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class UpdateEquipmentHandler(Handler):

    def __init__(self):
        self._commandConstant = CommonCommandConstant.UPDATE_EQUIPMENT

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{UpdateEquipmentHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')

        appService: EquipmentApplicationService = AppDi.instance.get(EquipmentApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        id = dataDict['manufacturer_id'] if 'manufacturer_id' in dataDict else None
        appService.updateEquipment(id=id,
                                   name=dataDict['name'],
                                   projectId=dataDict['project_id'],
                                   equipmentProjectCategoryId=dataDict['equipment_project_category_id'],
                                   equipmentCategoryId=dataDict['equipment_category_id'],
                                   equipmentCategoryGroupId=dataDict['equipment_category_group_id'],
                                   buildingId=dataDict['building_id'],
                                   buildingLevelId=dataDict['building_level_id'],
                                   buildingLevelRoomId=dataDict['building_level_room_id'],
                                   manufacturerId=dataDict['manufacturer_id'],
                                   equipmentModelId=dataDict['equipment_model_id'],
                                   quantity=dataDict['quantity'],
                                   token=metadataDict['token'])
        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': {'id': id, 'name': dataDict['name']},
                'metadata': metadataDict}
