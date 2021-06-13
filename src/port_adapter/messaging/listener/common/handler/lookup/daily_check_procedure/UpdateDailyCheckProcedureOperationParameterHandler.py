"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import json
import src.port_adapter.AppDi as AppDi
from src.application.lookup.daily_check_procedure.DailyCheckProcedureOperationParameterApplicationService import DailyCheckProcedureOperationParameterApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.logging.logger import logger
from src.resource.common.Util import Util

class UpdateDailyCheckProcedureOperationParameterHandler(Handler):

    def __init__(self):
        self._commandConstant = CommonCommandConstant.UPDATE_DAILY_CHECK_PROCEDURE_OPERATION_PARAMETER

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleMessage(self, messageData: dict, extraData: dict = None) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{UpdateDailyCheckProcedureOperationParameterHandler.handleMessage.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')

        dailyCheckProcedureOperationParameterAppService: DailyCheckProcedureOperationParameterApplicationService = AppDi.instance.get(DailyCheckProcedureOperationParameterApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        dataDict['id'] = dataDict.pop('daily_check_procedure_operation_parameter_id')
        dailyCheckProcedureOperationParameterAppService.updateDailyCheckProcedureOperationParameter(**Util.snakeCaseToLowerCameCaseDict(dataDict), token=metadataDict['token'])
        return None
