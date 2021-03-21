"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import json
import src.port_adapter.AppDi as AppDi
from src.application.DailyCheckProcedureOperationApplicationService import DailyCheckProcedureOperationApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class CreateDailyCheckProcedureOperationHandler(Handler):

    def __init__(self):
        self._commandConstant = CommonCommandConstant.CREATE_DAILY_CHECK_PROCEDURE_OPERATION

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{CreateDailyCheckProcedureOperationHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        appService: DailyCheckProcedureOperationApplicationService = AppDi.instance.get(DailyCheckProcedureOperationApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        id = dataDict['daily_check_procedure_operation_id'] if 'daily_check_procedure_operation_id' in dataDict else None
        obj = appService.createDailyCheckProcedureOperation(id=id, name=dataDict["name"], description=dataDict["description"], type=dataDict["type"], dailyCheckProcedureId=dataDict["daily_check_procedure_id"], token=metadataDict['token'])
        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': {'id': obj.id(), "name":obj.name(), "description":obj.description(), "type":obj.type(), "daily_check_procedure_id":obj.dailyCheckProcedureId()},
                'metadata': metadataDict}
