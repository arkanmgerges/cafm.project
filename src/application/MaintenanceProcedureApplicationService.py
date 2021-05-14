"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.domain_model.project.equipment.EquipmentRepository import EquipmentRepository
from src.domain_model.project.maintenance.procedure.MaintenanceProcedure import (
    MaintenanceProcedure,
)
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureRepository import (
    MaintenanceProcedureRepository,
)
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureService import (
    MaintenanceProcedureService,
)
from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.resource.exception.UpdateMaintenanceProcedureFailedException import (
    UpdateMaintenanceProcedureFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.domain_model.util.DomainModelAttributeValidator import DomainModelAttributeValidator
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger


class MaintenanceProcedureApplicationService(BaseApplicationService):
    def __init__(
        self,
        repo: MaintenanceProcedureRepository,
        maintenanceProcedureService: MaintenanceProcedureService,
        equipmentRepo: EquipmentRepository,
    ):
        self._repo = repo
        self._maintenanceProcedureService = maintenanceProcedureService
        self._equipmentRepo = equipmentRepo

    @debugLogger
    def newId(self):
        return MaintenanceProcedure.createFrom(skipValidation=True).id()

    @debugLogger
    def createMaintenanceProcedure(self, token: str = None, objectOnly: bool = False, **kwargs):
        obj: MaintenanceProcedure = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        self._equipmentRepo.equipmentById(id=kwargs["equipmentId"])
        return self._maintenanceProcedureService.createMaintenanceProcedure(
            obj=obj, objectOnly=objectOnly, tokenData=tokenData
        )

    @debugLogger
    def updateMaintenanceProcedure(self, token: str = None, **kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: MaintenanceProcedure = self._repo.maintenanceProcedureById(id=kwargs["id"])
            obj: MaintenanceProcedure = self._constructObject(_sourceObject=oldObject, **kwargs)
            self._maintenanceProcedureService.updateMaintenanceProcedure(
                oldObject=oldObject, newObject=obj, tokenData=tokenData
            )
        except Exception as e:
            raise UpdateMaintenanceProcedureFailedException(message=str(e))

    @debugLogger
    def deleteMaintenanceProcedure(self, id: str, token: str = None):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.maintenanceProcedureById(id=id)
        self._maintenanceProcedureService.deleteMaintenanceProcedure(obj=obj, tokenData=tokenData)

    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True), attributeDictionary=objListParamsItem
                )
                objList.append(
                    self._constructObject(
                        **Util.snakeCaseToLowerCameCaseDict(
                            objListParamsItem, keyReplacements=[{"source": "maintenance_procedure_id", "target": "id"}]
                        )
                    )
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._maintenanceProcedureService.bulkCreate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True), attributeDictionary=objListParamsItem
                )
                objList.append(
                    self._constructObject(id=objListParamsItem["maintenance_procedure_id"], skipValidation=True)
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._maintenanceProcedureService.bulkDelete(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                DomainModelAttributeValidator.validate(
                    domainModelObject=self._constructObject(skipValidation=True), attributeDictionary=objListParamsItem
                )
                oldObject: MaintenanceProcedure = self._repo.maintenanceProcedureById(
                    id=objListParamsItem["maintenance_procedure_id"]
                )
                newObject = self._constructObject(
                    **Util.snakeCaseToLowerCameCaseDict(
                        objListParamsItem, keyReplacements=[{"source": "maintenance_procedure_id", "target": "id"}]
                    ),
                    _sourceObject=oldObject,
                )
                objList.append(
                    (newObject, oldObject),
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._maintenanceProcedureService.bulkUpdate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def maintenanceProcedureById(self, id: str, token: str = None) -> MaintenanceProcedure:
        maintenanceProcedure = self._repo.maintenanceProcedureById(id=id)
        TokenService.tokenDataFromToken(token=token)
        return maintenanceProcedure

    @debugLogger
    def maintenanceProcedures(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._maintenanceProcedureService.maintenanceProcedures(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def maintenanceProceduresByEquipmentId(
        self,
        equipmentId: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._maintenanceProcedureService.maintenanceProceduresByEquipmentId(
            tokenData=tokenData,
            equipmentId=equipmentId,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> MaintenanceProcedure:
        kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS] = MaintenanceProcedure
        return super()._constructObject(*args, **kwargs)
