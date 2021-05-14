"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.application.model.BaseApplicationServiceBulkData import BaseApplicationServiceBulkData
from src.application.model.BaseApplicationServiceModelData import BaseApplicationServiceModelData
from src.domain_model.project.equipment.model.EquipmentModel import EquipmentModel
from src.domain_model.project.equipment.model.EquipmentModelRepository import (
    EquipmentModelRepository,
)
from src.domain_model.project.equipment.model.EquipmentModelService import (
    EquipmentModelService,
)
from src.domain_model.resource.exception.UpdateEquipmentModelFailedException import (
    UpdateEquipmentModelFailedException,
)
from src.domain_model.token.TokenService import TokenService
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
    def equipmentModelByName(self, name: str, token: str = "") -> EquipmentModel:
        equipmentModel = self._repo.equipmentModelByName(name=name)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        return equipmentModel

    @debugLogger
    def updateEquipmentModel(
        self,
        token: str = None,
        **kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: EquipmentModel = self._repo.equipmentModelById(id=kwargs["id"])
            super().callFunction(
                modelData=BaseApplicationServiceModelData(
                    function=self._equipmentModelService.updateEquipmentModel,
                    kwargs={
                        "oldObject": oldObject,
                        "newObject": self._constructObject(_sourceObject=oldObject, **kwargs),
                        "tokenData": tokenData,
                    },
                )
            )

        except Exception as e:
            raise UpdateEquipmentModelFailedException(message=str(e))

    @debugLogger
    def deleteEquipmentModel(self, id: str, token: str = None):
        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._equipmentModelService.deleteEquipmentModel,
                kwargs={
                    "obj": self._repo.equipmentModelById(id=id),
                    "tokenData": TokenService.tokenDataFromToken(token=token),
                },
            )
        )

    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = ""):
        super()._bulkCreate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="equipment_model_id",
                domainService=self._equipmentModelService,
            )
        )

    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = ""):
        super()._bulkDelete(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="equipment_model_id",
                domainService=self._equipmentModelService,
            )
        )

    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = ""):
        super()._bulkUpdate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="equipment_model_id",
                domainService=self._equipmentModelService,
                repositoryCallbackFunction=self._repo.equipmentModelById,
            )
        )

    @debugLogger
    def equipmentModelById(self, id: str, token: str = None) -> EquipmentModel:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(getterFunction=self._repo.equipmentModelById, kwargs={"id": id})
        )

    @debugLogger
    def equipmentModels(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._equipmentModelService.equipmentModels,
                kwargs={"resultFrom": resultFrom, "resultSize": resultSize, "order": order, "tokenData": tokenData},
            )
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> EquipmentModel:
        kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS] = EquipmentModel
        return super()._constructObject(*args, **kwargs)
