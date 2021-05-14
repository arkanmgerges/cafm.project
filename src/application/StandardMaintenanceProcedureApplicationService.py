"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroupRepository import (
    StandardEquipmentCategoryGroupRepository,
)
from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.resource.exception.UpdateStandardMaintenanceProcedureFailedException import (
    UpdateStandardMaintenanceProcedureFailedException,
)
from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedure import (
    StandardMaintenanceProcedure,
)
from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedureRepository import (
    StandardMaintenanceProcedureRepository,
)
from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedureService import (
    StandardMaintenanceProcedureService,
)
from src.domain_model.token.TokenService import TokenService
from src.domain_model.util.DomainModelAttributeValidator import DomainModelAttributeValidator
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger


class StandardMaintenanceProcedureApplicationService(BaseApplicationService):
    def __init__(
        self,
        repo: StandardMaintenanceProcedureRepository,
        standardMaintenanceProcedureService: StandardMaintenanceProcedureService,
        orgRepo: OrganizationRepository,
        standardEquipmentCategoryGroupRepo: StandardEquipmentCategoryGroupRepository,
    ):
        self._repo = repo
        self._standardMaintenanceProcedureService = standardMaintenanceProcedureService
        self._orgRepo = orgRepo
        self._standardEquipmentCategoryGroupRepo = standardEquipmentCategoryGroupRepo

    @debugLogger
    def newId(self):
        return StandardMaintenanceProcedure.createFrom(skipValidation=True).id()

    @debugLogger
    def createStandardMaintenanceProcedure(self, token: str = None, objectOnly: bool = False, **kwargs):
        obj: StandardMaintenanceProcedure = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        self._orgRepo.organizationById(id=kwargs['organizationId'])
        self._standardEquipmentCategoryGroupRepo.standardEquipmentCategoryGroupById(id=kwargs['standardEquipmentCategoryGroupId'])
        return self._standardMaintenanceProcedureService.createStandardMaintenanceProcedure(
            obj=obj, objectOnly=objectOnly, tokenData=tokenData
        )

    @debugLogger
    def updateStandardMaintenanceProcedure(self, token: str = None, **kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: StandardMaintenanceProcedure = self._repo.standardMaintenanceProcedureById(id=kwargs["id"])
            obj: StandardMaintenanceProcedure = self._constructObject(_sourceObject=oldObject, **kwargs)
            self._standardMaintenanceProcedureService.updateStandardMaintenanceProcedure(
                oldObject=oldObject, newObject=obj, tokenData=tokenData
            )
        except Exception as e:
            raise UpdateStandardMaintenanceProcedureFailedException(message=str(e))

    @debugLogger
    def deleteStandardMaintenanceProcedure(self, id: str, token: str = None):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.standardMaintenanceProcedureById(id=id)
        self._standardMaintenanceProcedureService.deleteStandardMaintenanceProcedure(obj=obj, tokenData=tokenData)

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
                            objListParamsItem, keyReplacements=[{"source": "standard_maintenance_procedure_id", "target": "id"}]
                        )
                    )
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._standardMaintenanceProcedureService.bulkCreate(objList=objList)
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
                    self._constructObject(
                        id=objListParamsItem["standard_maintenance_procedure_id"], skipValidation=True
                    )
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._standardMaintenanceProcedureService.bulkDelete(objList=objList)
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
                oldObject: StandardMaintenanceProcedure = self._repo.standardMaintenanceProcedureById(
                    id=objListParamsItem["standard_maintenance_procedure_id"]
                )
                newObject = self._constructObject(
                    **Util.snakeCaseToLowerCameCaseDict(
                        objListParamsItem,
                        keyReplacements=[{"source": "standard_maintenance_procedure_id", "target": "id"}]
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
            self._standardMaintenanceProcedureService.bulkUpdate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def standardMaintenanceProcedureById(self, id: str, token: str = None) -> StandardMaintenanceProcedure:
        standardMaintenanceProcedure = self._repo.standardMaintenanceProcedureById(id=id)
        TokenService.tokenDataFromToken(token=token)
        return standardMaintenanceProcedure

    @debugLogger
    def standardMaintenanceProcedures(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._standardMaintenanceProcedureService.standardMaintenanceProcedures(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> StandardMaintenanceProcedure:
        kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS] = StandardMaintenanceProcedure
        return super()._constructObject(*args, **kwargs)
