"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import json

import src.port_adapter.AppDi as AppDi
from src.application.DailyCheckProcedureApplicationService import DailyCheckProcedureApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class DeleteDailyCheckProcedureHandler(Handler):

    def __init__(self):
        self._commandConstant = CommonCommandConstant.DELETE_DAILY_CHECK_PROCEDURE

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{DeleteDailyCheckProcedureHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        appService: DailyCheckProcedureApplicationService = AppDi.instance.get(DailyCheckProcedureApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        appService.deleteDailyCheckProcedure(id=dataDict['daily_check_procedure_id'], token=metadataDict['token'])
        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': {'daily_check_procedure_id': dataDict['daily_check_procedure_id']},
                'metadata': metadataDict}