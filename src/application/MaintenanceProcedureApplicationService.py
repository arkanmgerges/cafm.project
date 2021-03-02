"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.domain_model.project.maintenance.procedure.MaintenanceProcedure import MaintenanceProcedure
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureRepository import MaintenanceProcedureRepository
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureService import MaintenanceProcedureService
from src.domain_model.resource.exception.UpdateMaintenanceProcedureFailedException import UpdateMaintenanceProcedureFailedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.domain_model.project.equipment.EquipmentRepository import EquipmentRepository

class MaintenanceProcedureApplicationService:
    def __init__(self, repo: MaintenanceProcedureRepository, maintenanceProcedureService: MaintenanceProcedureService,
            equipmentRepo: EquipmentRepository,):
        self._repo = repo
        self._maintenanceProcedureService = maintenanceProcedureService
        self._equipmentRepo = equipmentRepo

    @debugLogger
    def createMaintenanceProcedure(self, id: str = None, name: str = None, type: str = None, frequency: str = None, startDate: int = None, subcontractorId: str = None, equipmentId: str = None, objectOnly: bool = False, token: str = ''):
        obj: MaintenanceProcedure = self.constructObject(id=id, name=name, type=type, frequency=frequency, startDate=startDate, subcontractorId=subcontractorId, equipmentId=equipmentId)
        tokenData = TokenService.tokenDataFromToken(token=token)
        self._equipmentRepo.equipmentById(id=equipmentId)
        return self._maintenanceProcedureService.createMaintenanceProcedure(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateMaintenanceProcedure(self, id: str, name: str = None, type: str = None, frequency: str = None, startDate: int = None, subcontractorId: str = None, equipmentId: str = None, token: str = None):
        obj: MaintenanceProcedure = self.constructObject(id=id, name=name, type=type, frequency=frequency, startDate=startDate, subcontractorId=subcontractorId, equipmentId=equipmentId)
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: MaintenanceProcedure = self._repo.maintenanceProcedureById(id=id)
            self._maintenanceProcedureService.updateMaintenanceProcedure(oldObject=oldObject, newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateMaintenanceProcedureFailedException(message=str(e))

    @debugLogger
    def deleteMaintenanceProcedure(self, id: str, token: str = None):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.maintenanceProcedureById(id=id)
        self._maintenanceProcedureService.deleteMaintenanceProcedure(obj=obj, tokenData=tokenData)

    @debugLogger
    def maintenanceProcedureById(self, id: str, token: str = None) -> MaintenanceProcedure:
        maintenanceProcedure = self._repo.maintenanceProcedureById(id=id)
        TokenService.tokenDataFromToken(token=token)
        return maintenanceProcedure

    @debugLogger
    def maintenanceProcedures(self, resultFrom: int = 0, resultSize: int = 100, order: List[dict] = None,
                        token: str = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._maintenanceProcedureService.maintenanceProcedures(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)

    @debugLogger
    def maintenanceProceduresByEquipmentId(self, equipmentId: str = None, resultFrom: int = 0, resultSize: int = 100, order: List[dict] = None,
                        token: str = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._maintenanceProcedureService.maintenanceProceduresByEquipmentId(tokenData=tokenData, equipmentId=equipmentId, resultFrom=resultFrom, resultSize=resultSize, order=order)

    @debugLogger
    def constructObject(self, id: str, name: str = None, type: str = None, frequency: str = None, startDate: int = None, subcontractorId: str = None, equipmentId: str = None) -> MaintenanceProcedure:
        return MaintenanceProcedure.createFrom(id=id, name=name, type=type, frequency=frequency, startDate=startDate, subcontractorId=subcontractorId, equipmentId=equipmentId)
