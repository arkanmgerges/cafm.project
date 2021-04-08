"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedure import StandardMaintenanceProcedure
from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedureRepository import StandardMaintenanceProcedureRepository
from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedureService import StandardMaintenanceProcedureService
from src.domain_model.resource.exception.UpdateStandardMaintenanceProcedureFailedException import UpdateStandardMaintenanceProcedureFailedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger

class StandardMaintenanceProcedureApplicationService:
    def __init__(self, repo: StandardMaintenanceProcedureRepository, standardMaintenanceProcedureService: StandardMaintenanceProcedureService,):
        self._repo = repo
        self._standardMaintenanceProcedureService = standardMaintenanceProcedureService

    @debugLogger
    def newId(self):
        return StandardMaintenanceProcedure.createFrom(skipValidation=True).id()

    @debugLogger
    def createStandardMaintenanceProcedure(self, id: str = None, name: str = None, type: str = None, subtype: str = None, frequency: str = None, startDate: str = None, organizationId: str = None, objectOnly: bool = False, token: str = ''):
        obj: StandardMaintenanceProcedure = self.constructObject(id=id, 
			name=name,
			type=type,
			subtype=subtype,
			frequency=frequency,
			startDate=startDate,
			organizationId=organizationId)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._standardMaintenanceProcedureService.createStandardMaintenanceProcedure(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateStandardMaintenanceProcedure(self, id: str, name: str = None, type: str = None, subtype: str = None, frequency: str = None, startDate: str = None, organizationId: str = None, token: str = None):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: StandardMaintenanceProcedure = self._repo.standardMaintenanceProcedureById(id=id)
            obj: StandardMaintenanceProcedure = self.constructObject(id=id, 
			name=name,
			type=type,
			subtype=subtype,
			frequency=frequency,
			startDate=startDate,
			organizationId=organizationId, _sourceObject=oldObject)
            self._standardMaintenanceProcedureService.updateStandardMaintenanceProcedure(oldObject=oldObject, newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateStandardMaintenanceProcedureFailedException(message=str(e))

    @debugLogger
    def deleteStandardMaintenanceProcedure(self, id: str, token: str = None):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.standardMaintenanceProcedureById(id=id)
        self._standardMaintenanceProcedureService.deleteStandardMaintenanceProcedure(obj=obj, tokenData=tokenData)

    @debugLogger
    def standardMaintenanceProcedureById(self, id: str, token: str = None) -> StandardMaintenanceProcedure:
        standardMaintenanceProcedure = self._repo.standardMaintenanceProcedureById(id=id)
        TokenService.tokenDataFromToken(token=token)
        return standardMaintenanceProcedure

    @debugLogger
    def standardMaintenanceProcedures(self, resultFrom: int = 0, resultSize: int = 100, order: List[dict] = None,
                        token: str = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._standardMaintenanceProcedureService.standardMaintenanceProcedures(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)

    @debugLogger
    def constructObject(self, id: str, name: str = None, type: str = None, subtype: str = None, frequency: str = None, startDate: str = None, organizationId: str = None, _sourceObject: StandardMaintenanceProcedure = None) -> StandardMaintenanceProcedure:
        if _sourceObject is not None:
            return StandardMaintenanceProcedure.createFrom(id=id, 
			name=name if name is not None else _sourceObject.name(),
			type=type if type is not None else _sourceObject.type(),
			subtype=subtype if subtype is not None else _sourceObject.subtype(),
			frequency=frequency if frequency is not None else _sourceObject.frequency(),
			startDate=startDate if startDate is not None else _sourceObject.startDate(),
			organizationId=organizationId if organizationId is not None else _sourceObject.organizationId())
        else:
            return StandardMaintenanceProcedure.createFrom(id=id, 
			name=name,
			type=type,
			subtype=subtype,
			frequency=frequency,
			startDate=startDate,
			organizationId=organizationId)
