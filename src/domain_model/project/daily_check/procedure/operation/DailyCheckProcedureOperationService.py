"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperation import (
    DailyCheckProcedureOperation,
)
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationRepository import (
    DailyCheckProcedureOperationRepository,
)
from src.domain_model.resource.exception.DailyCheckProcedureOperationAlreadyExistException import (
    DailyCheckProcedureOperationAlreadyExistException,
)
from src.domain_model.resource.exception.DailyCheckProcedureOperationDoesNotExistException import (
    DailyCheckProcedureOperationDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class DailyCheckProcedureOperationService:
    def __init__(self, repository: DailyCheckProcedureOperationRepository):
        self._repo = repository

    @debugLogger
    def createDailyCheckProcedureOperation(
        self,
        obj: DailyCheckProcedureOperation,
        objectOnly: bool = False,
        tokenData: TokenData = None,
    ):
        if objectOnly:
            return (
                DailyCheckProcedureOperation.createFromObject(
                    obj=obj, generateNewId=True
                )
                if obj.id() == ""
                else obj
            )
        else:
            obj = DailyCheckProcedureOperation.createFromObject(
                obj=obj, publishEvent=True
            )
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def deleteDailyCheckProcedureOperation(
        self, obj: DailyCheckProcedureOperation, tokenData: TokenData = None
    ):
        obj.publishDelete()
        self._repo.deleteDailyCheckProcedureOperation(obj=obj)

    @debugLogger
    def updateDailyCheckProcedureOperation(
        self,
        oldObject: DailyCheckProcedureOperation,
        newObject: DailyCheckProcedureOperation,
        tokenData: TokenData = None,
    ):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def dailyCheckProcedureOperations(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.dailyCheckProcedureOperations(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def dailyCheckProcedureOperationsByDailyCheckProcedureId(
        self,
        dailyCheckProcedureId: str = None,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.dailyCheckProcedureOperationsByDailyCheckProcedureId(
            tokenData=tokenData,
            dailyCheckProcedureId=dailyCheckProcedureId,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )
