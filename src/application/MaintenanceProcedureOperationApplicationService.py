"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.domain_model.project.maintenance.procedure.operation.MaintenanceProcedureOperation import MaintenanceProcedureOperation
from src.domain_model.project.maintenance.procedure.operation.MaintenanceProcedureOperationRepository import MaintenanceProcedureOperationRepository
from src.domain_model.project.maintenance.procedure.operation.MaintenanceProcedureOperationService import MaintenanceProcedureOperationService
from src.domain_model.resource.exception.UpdateMaintenanceProcedureOperationFailedException import UpdateMaintenanceProcedureOperationFailedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureRepository import MaintenanceProcedureRepository

class MaintenanceProcedureOperationApplicationService:
    def __init__(self, repo: MaintenanceProcedureOperationRepository, maintenanceProcedureOperationService: MaintenanceProcedureOperationService,
            maintenanceProcedureRepo: MaintenanceProcedureRepository,):
        self._repo = repo
        self._maintenanceProcedureOperationService = maintenanceProcedureOperationService
        self._maintenanceProcedureRepo = maintenanceProcedureRepo

    @debugLogger
    def createMaintenanceProcedureOperation(self, id: str = None, name: str = None, description: str = None, type: str = None, maintenanceProcedureId: str = None, objectOnly: bool = False, token: str = ''):
        obj: MaintenanceProcedureOperation = self.constructObject(id=id, name=name, description=description, type=type, maintenanceProcedureId=maintenanceProcedureId)
        tokenData = TokenService.tokenDataFromToken(token=token)
        self._maintenanceProcedureRepo.maintenanceProcedureById(id=maintenanceProcedureId)
        return self._maintenanceProcedureOperationService.createMaintenanceProcedureOperation(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateMaintenanceProcedureOperation(self, id: str, name: str = None, description: str = None, type: str = None, maintenanceProcedureId: str = None, token: str = None):
        obj: MaintenanceProcedureOperation = self.constructObject(id=id, name=name, description=description, type=type, maintenanceProcedureId=maintenanceProcedureId)
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: MaintenanceProcedureOperation = self._repo.maintenanceProcedureOperationById(id=id)
            self._maintenanceProcedureOperationService.updateMaintenanceProcedureOperation(oldObject=oldObject, newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateMaintenanceProcedureOperationFailedException(message=str(e))

    @debugLogger
    def deleteMaintenanceProcedureOperation(self, id: str, token: str = None):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.maintenanceProcedureOperationById(id=id)
        self._maintenanceProcedureOperationService.deleteMaintenanceProcedureOperation(obj=obj, tokenData=tokenData)

    @debugLogger
    def maintenanceProcedureOperationById(self, id: str, token: str = None) -> MaintenanceProcedureOperation:
        maintenanceProcedureOperation = self._repo.maintenanceProcedureOperationById(id=id)
        TokenService.tokenDataFromToken(token=token)
        return maintenanceProcedureOperation

    @debugLogger
    def maintenanceProcedureOperations(self, resultFrom: int = 0, resultSize: int = 100, order: List[dict] = None,
                        token: str = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._maintenanceProcedureOperationService.maintenanceProcedureOperations(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)

    @debugLogger
    def maintenanceProcedureOperationsByMaintenanceProcedureId(self, maintenanceProcedureId: str = None, resultFrom: int = 0, resultSize: int = 100, order: List[dict] = None,
                        token: str = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._maintenanceProcedureOperationService.maintenanceProcedureOperationsByMaintenanceProcedureId(tokenData=tokenData, maintenanceProcedureId=maintenanceProcedureId, resultFrom=resultFrom, resultSize=resultSize, order=order)

    @debugLogger
    def constructObject(self, id: str, name: str = None, description: str = None, type: str = None, maintenanceProcedureId: str = None) -> MaintenanceProcedureOperation:
        return MaintenanceProcedureOperation.createFrom(id=id, name=name, description=description, type=type, maintenanceProcedureId=maintenanceProcedureId)
