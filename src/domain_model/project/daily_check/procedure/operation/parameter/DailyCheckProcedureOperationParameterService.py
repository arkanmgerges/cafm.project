"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, Tuple
from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameter import (
    DailyCheckProcedureOperationParameter,
)
from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameterRepository import (
    DailyCheckProcedureOperationParameterRepository,
)
from src.domain_model.resource.exception.DailyCheckProcedureOperationParameterAlreadyExistException import (
    DailyCheckProcedureOperationParameterAlreadyExistException,
)
from src.domain_model.resource.exception.DailyCheckProcedureOperationParameterDoesNotExistException import (
    DailyCheckProcedureOperationParameterDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class DailyCheckProcedureOperationParameterService:
    def __init__(self, repository: DailyCheckProcedureOperationParameterRepository):
        self._repo = repository

    @debugLogger
    def createDailyCheckProcedureOperationParameter(
        self,
        obj: DailyCheckProcedureOperationParameter,
        objectOnly: bool = False,
        tokenData: TokenData = None,
    ):
        if objectOnly:
            return (
                DailyCheckProcedureOperationParameter.createFromObject(
                    obj=obj, generateNewId=True
                )
                if obj.id() == ""
                else obj
            )
        else:
            obj = DailyCheckProcedureOperationParameter.createFromObject(
                obj=obj, publishEvent=True
            )
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def deleteDailyCheckProcedureOperationParameter(
        self, obj: DailyCheckProcedureOperationParameter, tokenData: TokenData = None
    ):
        obj.publishDelete()
        self._repo.deleteDailyCheckProcedureOperationParameter(obj=obj)

    @debugLogger
    def updateDailyCheckProcedureOperationParameter(
        self,
        oldObject: DailyCheckProcedureOperationParameter,
        newObject: DailyCheckProcedureOperationParameter,
        tokenData: TokenData = None,
    ):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def bulkCreate(self, objList: List[DailyCheckProcedureOperationParameter]):
        self._repo.bulkSave(objList=objList)
        for obj in objList:
            DailyCheckProcedureOperationParameter.createFromObject(obj=obj, publishEvent=True)

    @debugLogger
    def bulkDelete(self, objList: List[DailyCheckProcedureOperationParameter]):
        self._repo.bulkDelete(objList=objList)
        for obj in objList:
            obj.publishDelete()

    @debugLogger
    def bulkUpdate(self, objList: List[Tuple]):
        newObjList = list(map(lambda x: x[0], objList))
        self._repo.bulkSave(objList=newObjList)
        for obj in objList:
            newObj = obj[0]
            oldObj = obj[1]
            newObj.publishUpdate(oldObj)

    @debugLogger
    def dailyCheckProcedureOperationParameters(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.dailyCheckProcedureOperationParameters(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationId(
        self,
        dailyCheckProcedureOperationId: str = None,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationId(
            tokenData=tokenData,
            dailyCheckProcedureOperationId=dailyCheckProcedureOperationId,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )
