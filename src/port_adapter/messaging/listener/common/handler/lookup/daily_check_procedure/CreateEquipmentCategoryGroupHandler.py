"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import json
import src.port_adapter.AppDi as AppDi
from src.application.lookup.daily_check_procedure.EquipmentCategoryGroupApplicationService import EquipmentCategoryGroupApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.logging.logger import logger
from src.resource.common.Util import Util


class CreateEquipmentCategoryGroupHandler(Handler):

    def __init__(self):
        self._commandConstant = CommonCommandConstant.CREATE_EQUIPMENT_CATEGORY_GROUP

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict, extraData: dict = None) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{CreateEquipmentCategoryGroupHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        equipmentCategoryGroupAppService: EquipmentCategoryGroupApplicationService = AppDi.instance.get(EquipmentCategoryGroupApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        dataDict['id'] = dataDict.pop('equipment_category_group_id')
        equipmentCategoryGroupAppService.createEquipmentCategoryGroup(**Util.snakeCaseToLowerCameCaseDict(dataDict), token=metadataDict['token'])
        return None
