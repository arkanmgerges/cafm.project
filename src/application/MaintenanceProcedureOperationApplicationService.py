"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.application.model.BaseApplicationServiceBulkData import BaseApplicationServiceBulkData
from src.application.model.BaseApplicationServiceModelData import BaseApplicationServiceModelData
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureRepository import (
    MaintenanceProcedureRepository,
)
from src.domain_model.project.maintenance.procedure.operation.MaintenanceProcedureOperation import (
    MaintenanceProcedureOperation,
)
from src.domain_model.project.maintenance.procedure.operation.MaintenanceProcedureOperationRepository import (
    MaintenanceProcedureOperationRepository,
)
from src.domain_model.project.maintenance.procedure.operation.MaintenanceProcedureOperationService import (
    MaintenanceProcedureOperationService,
)
from src.domain_model.resource.exception.UpdateMaintenanceProcedureOperationFailedException import (
    UpdateMaintenanceProcedureOperationFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class MaintenanceProcedureOperationApplicationService(BaseApplicationService):
    def __init__(
        self,
        repo: MaintenanceProcedureOperationRepository,
        maintenanceProcedureOperationService: MaintenanceProcedureOperationService,
        maintenanceProcedureRepo: MaintenanceProcedureRepository,
    ):
        self._repo = repo
        self._maintenanceProcedureOperationService = maintenanceProcedureOperationService
        self._maintenanceProcedureRepo = maintenanceProcedureRepo

    @debugLogger
    def newId(self):
        return MaintenanceProcedureOperation.createFrom(skipValidation=True).id()

    @debugLogger
    def createMaintenanceProcedureOperation(self, token: str = None, objectOnly: bool = False, **kwargs):
        obj: MaintenanceProcedureOperation = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        self._maintenanceProcedureRepo.maintenanceProcedureById(id=kwargs["maintenanceProcedureId"])
        return self._maintenanceProcedureOperationService.createMaintenanceProcedureOperation(
            obj=obj, objectOnly=objectOnly, tokenData=tokenData
        )

    @debugLogger
    def maintenanceProcedureOperationsByMaintenanceProcedureId(
        self,
        maintenanceProcedureId: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
        **_kwargs,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._maintenanceProcedureOperationService.maintenanceProcedureOperationsByMaintenanceProcedureId(
            tokenData=tokenData,
            maintenanceProcedureId=maintenanceProcedureId,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def updateMaintenanceProcedureOperation(
        self,
        token: str = None,
        **kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: MaintenanceProcedureOperation = self._repo.maintenanceProcedureOperationById(id=kwargs["id"])
            super().callFunction(
                modelData=BaseApplicationServiceModelData(
                    function=self._maintenanceProcedureOperationService.updateMaintenanceProcedureOperation,
                    kwargs={
                        "oldObject": oldObject,
                        "newObject": self._constructObject(_sourceObject=oldObject, **kwargs),
                        "tokenData": tokenData,
                    },
                )
            )

        except Exception as e:
            raise UpdateMaintenanceProcedureOperationFailedException(message=str(e))

    @debugLogger
    def deleteMaintenanceProcedureOperation(self, id: str, token: str = None, **_kwargs):
        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._maintenanceProcedureOperationService.deleteMaintenanceProcedureOperation,
                kwargs={
                    "obj": self._repo.maintenanceProcedureOperationById(id=id),
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
                sourceId="maintenance_procedure_operation_id",
                domainService=self._maintenanceProcedureOperationService,
            )
        )

    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = ""):
        super()._bulkDelete(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="maintenance_procedure_operation_id",
                domainService=self._maintenanceProcedureOperationService,
            )
        )

    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = ""):
        super()._bulkUpdate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="maintenance_procedure_operation_id",
                domainService=self._maintenanceProcedureOperationService,
                repositoryCallbackFunction=self._repo.maintenanceProcedureOperationById,
            )
        )

    @debugLogger
    def maintenanceProcedureOperationById(self, id: str, token: str = None, **_kwargs) -> MaintenanceProcedureOperation:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._repo.maintenanceProcedureOperationById, kwargs={"id": id}
            )
        )

    @debugLogger
    def maintenanceProcedureOperations(
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
                getterFunction=self._maintenanceProcedureOperationService.maintenanceProcedureOperations,
                kwargs={"resultFrom": resultFrom, "resultSize": resultSize, "order": order, "tokenData": tokenData},
            )
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> MaintenanceProcedureOperation:
        kwargs[BaseApplicationService.DOMAIN_MODEL_CLASS] = MaintenanceProcedureOperation
        return super()._constructObject(*args, **kwargs)
