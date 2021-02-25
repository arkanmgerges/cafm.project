"""
The file is generated by a scaffold script
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

        id = dataDict['equipment_id'] if 'equipment_id' in dataDict else None
        appService.updateEquipment(id=id, name=dataDict["name"], project_id=dataDict["project_id"], equipment_project_category_id=dataDict["equipment_project_category_id"], equipment_category_id=dataDict["equipment_category_id"], equipment_category_group_id=dataDict["equipment_category_group_id"], building_id=dataDict["building_id"], building_level_id=dataDict["building_level_id"], building_level_room_id=dataDict["building_level_room_id"], manufacturer_id=dataDict["manufacturer_id"], equipment_model_id=dataDict["equipment_model_id"], quantity=dataDict["quantity"], token=metadataDict['token'])
        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': {'equipment_id': id, "name":dataDict["name"], "project_id":dataDict["project_id"], "equipment_project_category_id":dataDict["equipment_project_category_id"], "equipment_category_id":dataDict["equipment_category_id"], "equipment_category_group_id":dataDict["equipment_category_group_id"], "building_id":dataDict["building_id"], "building_level_id":dataDict["building_level_id"], "building_level_room_id":dataDict["building_level_room_id"], "manufacturer_id":dataDict["manufacturer_id"], "equipment_model_id":dataDict["equipment_model_id"], "quantity":dataDict["quantity"]},
                'metadata': metadataDict}