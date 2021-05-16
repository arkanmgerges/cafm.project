"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.application.model.BaseApplicationServiceBulkData import BaseApplicationServiceBulkData
from src.application.model.BaseApplicationServiceModelData import BaseApplicationServiceModelData
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
from src.domain_model.resource.exception.UpdateMaintenanceProcedureFailedException import (
    UpdateMaintenanceProcedureFailedException,
)
from src.domain_model.token.TokenService import TokenService
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
    def maintenanceProceduresByEquipmentId(
        self,
        equipmentId: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
        **_kwargs,
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
    def updateMaintenanceProcedure(
        self,
        token: str = None,
        **kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: MaintenanceProcedure = self._repo.maintenanceProcedureById(id=kwargs["id"])
            super().callFunction(
                modelData=BaseApplicationServiceModelData(
                    function=self._maintenanceProcedureService.updateMaintenanceProcedure,
                    kwargs={
                        "oldObject": oldObject,
                        "newObject": self._constructObject(_sourceObject=oldObject, **kwargs),
                        "tokenData": tokenData,
                    },
                )
            )

        except Exception as e:
            raise UpdateMaintenanceProcedureFailedException(message=str(e))

    @debugLogger
    def deleteMaintenanceProcedure(self, id: str, token: str = None, **_kwargs):
        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._maintenanceProcedureService.deleteMaintenanceProcedure,
                kwargs={
                    "obj": self._repo.maintenanceProcedureById(id=id),
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
                sourceId="maintenance_procedure_id",
                domainService=self._maintenanceProcedureService,
            )
        )

    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = ""):
        super()._bulkDelete(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="maintenance_procedure_id",
                domainService=self._maintenanceProcedureService,
            )
        )

    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = ""):
        super()._bulkUpdate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="maintenance_procedure_id",
                domainService=self._maintenanceProcedureService,
                repositoryCallbackFunction=self._repo.maintenanceProcedureById,
            )
        )

    @debugLogger
    def maintenanceProcedureById(self, id: str, token: str = None, **_kwargs) -> MaintenanceProcedure:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._repo.maintenanceProcedureById, kwargs={"id": id}
            )
        )

    @debugLogger
    def maintenanceProcedures(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
        **_kwargs,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._maintenanceProcedureService.maintenanceProcedures,
                kwargs={"resultFrom": resultFrom, "resultSize": resultSize, "order": order, "tokenData": tokenData},
            )
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> MaintenanceProcedure:
        kwargs[BaseApplicationService.DOMAIN_MODEL_CLASS] = MaintenanceProcedure
        return super()._constructObject(*args, **kwargs)
