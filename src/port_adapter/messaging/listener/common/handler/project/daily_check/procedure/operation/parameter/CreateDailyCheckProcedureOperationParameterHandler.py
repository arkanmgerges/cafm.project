"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import json
import src.port_adapter.AppDi as AppDi
from src.application.DailyCheckProcedureOperationParameterApplicationService import DailyCheckProcedureOperationParameterApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class CreateDailyCheckProcedureOperationParameterHandler(Handler):

    def __init__(self):
        self._commandConstant = CommonCommandConstant.CREATE_DAILY_CHECK_PROCEDURE_OPERATION_PARAMETER

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{CreateDailyCheckProcedureOperationParameterHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        appService: DailyCheckProcedureOperationParameterApplicationService = AppDi.instance.get(DailyCheckProcedureOperationParameterApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        id = dataDict['daily_check_procedure_operation_parameter_id'] if 'daily_check_procedure_operation_parameter_id' in dataDict else None
        obj = appService.createDailyCheckProcedureOperationParameter(id=id, name=dataDict["name"], unitId=dataDict["unit_id"], dailyCheckProcedureOperationId=dataDict["daily_check_procedure_operation_id"], minValue=dataDict["min_value"], maxValue=dataDict["max_value"], token=metadataDict['token'])
        data = dataDict
        data['daily_check_procedure_operation_parameter_id'] = obj.id()
        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': data,
                'metadata': metadataDict}
