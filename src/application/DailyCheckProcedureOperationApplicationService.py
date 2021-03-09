"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperation import DailyCheckProcedureOperation
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationRepository import DailyCheckProcedureOperationRepository
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationService import DailyCheckProcedureOperationService
from src.domain_model.resource.exception.UpdateDailyCheckProcedureOperationFailedException import UpdateDailyCheckProcedureOperationFailedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.domain_model.project.daily_check.procedure.DailyCheckProcedureRepository import DailyCheckProcedureRepository

class DailyCheckProcedureOperationApplicationService:
    def __init__(self, repo: DailyCheckProcedureOperationRepository, dailyCheckProcedureOperationService: DailyCheckProcedureOperationService,
            dailyCheckProcedureRepo: DailyCheckProcedureRepository,):
        self._repo = repo
        self._dailyCheckProcedureOperationService = dailyCheckProcedureOperationService
        self._dailyCheckProcedureRepo = dailyCheckProcedureRepo

    @debugLogger
    def newId(self):
        return DailyCheckProcedureOperation.createFrom(skipValidation=True).id()


    @debugLogger
    def createDailyCheckProcedureOperation(self, id: str = None, name: str = None, description: str = None, type: str = None, dailyCheckProcedureId: str = None, objectOnly: bool = False, token: str = ''):
        obj: DailyCheckProcedureOperation = self.constructObject(id=id, name=name, description=description, type=type, dailyCheckProcedureId=dailyCheckProcedureId)
        tokenData = TokenService.tokenDataFromToken(token=token)
        self._dailyCheckProcedureRepo.dailyCheckProcedureById(id=dailyCheckProcedureId)
        return self._dailyCheckProcedureOperationService.createDailyCheckProcedureOperation(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateDailyCheckProcedureOperation(self, id: str, name: str = None, description: str = None, type: str = None, dailyCheckProcedureId: str = None, token: str = None):
        obj: DailyCheckProcedureOperation = self.constructObject(id=id, name=name, description=description, type=type, dailyCheckProcedureId=dailyCheckProcedureId)
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: DailyCheckProcedureOperation = self._repo.dailyCheckProcedureOperationById(id=id)
            self._dailyCheckProcedureOperationService.updateDailyCheckProcedureOperation(oldObject=oldObject, newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateDailyCheckProcedureOperationFailedException(message=str(e))

    @debugLogger
    def deleteDailyCheckProcedureOperation(self, id: str, token: str = None):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.dailyCheckProcedureOperationById(id=id)
        self._dailyCheckProcedureOperationService.deleteDailyCheckProcedureOperation(obj=obj, tokenData=tokenData)

    @debugLogger
    def dailyCheckProcedureOperationById(self, id: str, token: str = None) -> DailyCheckProcedureOperation:
        dailyCheckProcedureOperation = self._repo.dailyCheckProcedureOperationById(id=id)
        TokenService.tokenDataFromToken(token=token)
        return dailyCheckProcedureOperation

    @debugLogger
    def dailyCheckProcedureOperations(self, resultFrom: int = 0, resultSize: int = 100, order: List[dict] = None,
                        token: str = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._dailyCheckProcedureOperationService.dailyCheckProcedureOperations(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)

    @debugLogger
    def dailyCheckProcedureOperationsByDailyCheckProcedureId(self, dailyCheckProcedureId: str = None, resultFrom: int = 0, resultSize: int = 100, order: List[dict] = None,
                        token: str = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._dailyCheckProcedureOperationService.dailyCheckProcedureOperationsByDailyCheckProcedureId(tokenData=tokenData, dailyCheckProcedureId=dailyCheckProcedureId, resultFrom=resultFrom, resultSize=resultSize, order=order)

    @debugLogger
    def constructObject(self, id: str, name: str = None, description: str = None, type: str = None, dailyCheckProcedureId: str = None) -> DailyCheckProcedureOperation:
        return DailyCheckProcedureOperation.createFrom(id=id, name=name, description=description, type=type, dailyCheckProcedureId=dailyCheckProcedureId)
