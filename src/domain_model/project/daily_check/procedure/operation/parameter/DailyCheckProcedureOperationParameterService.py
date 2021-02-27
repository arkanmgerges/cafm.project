"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List
from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameter import DailyCheckProcedureOperationParameter
from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameterRepository import DailyCheckProcedureOperationParameterRepository
from src.domain_model.resource.exception.DailyCheckProcedureOperationParameterAlreadyExistException import DailyCheckProcedureOperationParameterAlreadyExistException
from src.domain_model.resource.exception.DailyCheckProcedureOperationParameterDoesNotExistException import DailyCheckProcedureOperationParameterDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class DailyCheckProcedureOperationParameterService:
    def __init__(self, repository: DailyCheckProcedureOperationParameterRepository):
        self._repo = repository

    @debugLogger
    def createDailyCheckProcedureOperationParameter(self, obj: DailyCheckProcedureOperationParameter, objectOnly: bool = False, tokenData: TokenData = None):
        try:
            if obj.id() == '':
                raise DailyCheckProcedureOperationParameterDoesNotExistException()
            self._repo.dailyCheckProcedureOperationParameterById(id=obj.id())
            raise DailyCheckProcedureOperationParameterAlreadyExistException(obj.id())
        except DailyCheckProcedureOperationParameterDoesNotExistException:
            if objectOnly:
                return DailyCheckProcedureOperationParameter.createFromObject(obj=obj, generateNewId=True) if obj.id() == '' else obj
            else:
                obj = DailyCheckProcedureOperationParameter.createFromObject(obj=obj, publishEvent=True)
                return obj

    @debugLogger
    def deleteDailyCheckProcedureOperationParameter(self, obj: DailyCheckProcedureOperationParameter, tokenData: TokenData = None):
        obj.publishDelete()

    @debugLogger
    def updateDailyCheckProcedureOperationParameter(self, oldObject: DailyCheckProcedureOperationParameter, newObject: DailyCheckProcedureOperationParameter, tokenData: TokenData = None):
        newObject.publishUpdate(oldObject)

    @debugLogger
    def dailyCheckProcedureOperationParameters(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
                      order: List[dict] = None):
        return self._repo.dailyCheckProcedureOperationParameters(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
