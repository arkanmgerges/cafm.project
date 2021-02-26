"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.domain_model.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameter import MaintenanceProcedureOperationParameter
from src.domain_model.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameterRepository import MaintenanceProcedureOperationParameterRepository
from src.domain_model.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameterService import MaintenanceProcedureOperationParameterService
from src.domain_model.resource.exception.UpdateMaintenanceProcedureOperationParameterFailedException import UpdateMaintenanceProcedureOperationParameterFailedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.domain_model.project.maintenance.procedure.operation.MaintenanceProcedureOperationRepository import MaintenanceProcedureOperationRepository

class MaintenanceProcedureOperationParameterApplicationService:
    def __init__(self, repo: MaintenanceProcedureOperationParameterRepository, maintenanceProcedureOperationParameterService: MaintenanceProcedureOperationParameterService,
            maintenanceProcedureOperationRepo: MaintenanceProcedureOperationRepository,):
        self._repo = repo
        self._maintenanceProcedureOperationParameterService = maintenanceProcedureOperationParameterService
        self._maintenanceProcedureOperationRepo = maintenanceProcedureOperationRepo

    @debugLogger
    def createMaintenanceProcedureOperationParameter(self, id: str = None, name: str = None, unitId: str = None, maintenanceProcedureOperationId: str = None, minValue: float = None, maxValue: float = None, objectOnly: bool = False, token: str = ''):
        obj: MaintenanceProcedureOperationParameter = self.constructObject(id=id, name=name, unitId=unitId, maintenanceProcedureOperationId=maintenanceProcedureOperationId, minValue=minValue, maxValue=maxValue)
        tokenData = TokenService.tokenDataFromToken(token=token)
        self._maintenanceProcedureOperationRepo.maintenanceProcedureOperationById(id=maintenanceProcedureOperationId)
        return self._maintenanceProcedureOperationParameterService.createMaintenanceProcedureOperationParameter(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateMaintenanceProcedureOperationParameter(self, id: str, name: str = None, unitId: str = None, maintenanceProcedureOperationId: str = None, minValue: float = None, maxValue: float = None, token: str = None):
        obj: MaintenanceProcedureOperationParameter = self.constructObject(id=id, name=name, unitId=unitId, maintenanceProcedureOperationId=maintenanceProcedureOperationId, minValue=minValue, maxValue=maxValue)
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: MaintenanceProcedureOperationParameter = self._repo.maintenanceProcedureOperationParameterById(id=id)
            self._maintenanceProcedureOperationParameterService.updateMaintenanceProcedureOperationParameter(oldObject=oldObject, newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateMaintenanceProcedureOperationParameterFailedException(message=str(e))

    @debugLogger
    def deleteMaintenanceProcedureOperationParameter(self, id: str, token: str = None):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.maintenanceProcedureOperationParameterById(id=id)
        self._maintenanceProcedureOperationParameterService.deleteMaintenanceProcedureOperationParameter(obj=obj, tokenData=tokenData)

    @debugLogger
    def maintenanceProcedureOperationParameterById(self, id: str, token: str = None) -> MaintenanceProcedureOperationParameter:
        maintenanceProcedureOperationParameter = self._repo.maintenanceProcedureOperationParameterById(id=id)
        TokenService.tokenDataFromToken(token=token)
        return maintenanceProcedureOperationParameter

    @debugLogger
    def maintenanceProcedureOperationParameters(self, resultFrom: int = 0, resultSize: int = 100, order: List[dict] = None,
                        token: str = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._maintenanceProcedureOperationParameterService.maintenanceProcedureOperationParameters(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)

    @debugLogger
    def constructObject(self, id: str, name: str = None, unitId: str = None, maintenanceProcedureOperationId: str = None, minValue: float = None, maxValue: float = None) -> MaintenanceProcedureOperationParameter:
        return MaintenanceProcedureOperationParameter.createFrom(id=id, name=name, unitId=unitId, maintenanceProcedureOperationId=maintenanceProcedureOperationId, minValue=minValue, maxValue=maxValue)
