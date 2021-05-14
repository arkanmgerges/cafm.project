"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.domain_model.project.equipment.model.EquipmentModel import EquipmentModel
from src.domain_model.project.equipment.model.EquipmentModelRepository import (
    EquipmentModelRepository,
)
from src.domain_model.project.equipment.model.EquipmentModelService import (
    EquipmentModelService,
)
from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.resource.exception.UpdateEquipmentModelFailedException import (
    UpdateEquipmentModelFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.domain_model.util.DomainModelAttributeValidator import DomainModelAttributeValidator
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger


class EquipmentModelApplicationService(BaseApplicationService):
    def __init__(
        self,
        repo: EquipmentModelRepository,
        equipmentModelService: EquipmentModelService,
    ):
        self._repo = repo
        self._equipmentModelService = equipmentModelService

    @debugLogger
    def newId(self):
        return EquipmentModel.createFrom(skipValidation=True).id()

    @debugLogger
    def createEquipmentModel(self, token: str = None, objectOnly: bool = False, **kwargs):
        obj: EquipmentModel = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentModelService.createEquipmentModel(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateEquipmentModel(self, token: str = None, **kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: EquipmentModel = self._repo.equipmentModelById(id=kwargs["id"])
            obj: EquipmentModel = self._constructObject(_sourceObject=oldObject, **kwargs)
            self._equipmentModelService.updateEquipmentModel(oldObject=oldObject, newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateEquipmentModelFailedException(message=str(e))

    @debugLogger
    def deleteEquipmentModel(self, id: str, token: str = ""):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.equipmentModelById(id=id)
        self._equipmentModelService.deleteEquipmentModel(obj=obj, tokenData=tokenData)

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
                            objListParamsItem, keyReplacements=[{"source": "equipment_model_id", "target": "id"}]
                        )
                    )
                )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._equipmentModelService.bulkCreate(objList=objList)
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
                objList.append(self._constructObject(id=objListParamsItem["equipment_model_id"], skipValidation=True))
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        _tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._equipmentModelService.bulkDelete(objList=objList)
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
                oldObject: EquipmentModel = self._repo.equipmentModelById(id=objListParamsItem["equipment_model_id"])
                newObject = self._constructObject(
                    **Util.snakeCaseToLowerCameCaseDict(
                        objListParamsItem, keyReplacements=[{"source": "equipment_model_id", "target": "id"}]
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
            self._equipmentModelService.bulkUpdate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def equipmentModelByName(self, name: str, token: str = "") -> EquipmentModel:
        equipmentModel = self._repo.equipmentModelByName(name=name)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        return equipmentModel

    @debugLogger
    def equipmentModelById(self, id: str, token: str = "") -> EquipmentModel:
        equipmentModel = self._repo.equipmentModelById(id=id)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        return equipmentModel

    @debugLogger
    def equipmentModels(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentModelService.equipmentModels(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> EquipmentModel:
        kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS] = EquipmentModel
        return super()._constructObject(*args, **kwargs)
