"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import json
import src.port_adapter.AppDi as AppDi
from src.application.EquipmentInputApplicationService import EquipmentInputApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class CreateEquipmentInputHandler(Handler):

    def __init__(self):
        self._commandConstant = CommonCommandConstant.CREATE_EQUIPMENT_INPUT

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{CreateEquipmentInputHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        appService: EquipmentInputApplicationService = AppDi.instance.get(EquipmentInputApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        id = dataDict['equipment_input_id'] if 'equipment_input_id' in dataDict else None
        obj = appService.createEquipmentInput(id=id, name=dataDict["name"], value=dataDict["value"], unitId=dataDict["unit_id"], equipmentId=dataDict["equipment_id"], token=metadataDict['token'])
        data = dataDict
        data['id'] = obj.id()
        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': data,
                'metadata': metadataDict}
