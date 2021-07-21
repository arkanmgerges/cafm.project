"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.domain_model.project.maintenance.procedure.operation.label.MaintenanceProcedureOperationLabel import MaintenanceProcedureOperationLabel
from src.domain_model.project.maintenance.procedure.operation.label.MaintenanceProcedureOperationLabelRepository import MaintenanceProcedureOperationLabelRepository
from src.domain_model.project.maintenance.procedure.operation.label.MaintenanceProcedureOperationLabelService import MaintenanceProcedureOperationLabelService
from src.domain_model.resource.exception.UpdateMaintenanceProcedureOperationLabelFailedException import UpdateMaintenanceProcedureOperationLabelFailedException
from src.domain_model.token.TokenService import TokenService
from src.application.BaseApplicationService import BaseApplicationService
from src.application.lifecycle.decorator.readOnly import readOnly
from src.application.lifecycle.decorator.transactional import transactional
from src.application.model.BaseApplicationServiceBulkData import BaseApplicationServiceBulkData
from src.application.model.BaseApplicationServiceModelData import BaseApplicationServiceModelData
from src.resource.logging.decorator import debugLogger

class MaintenanceProcedureOperationLabelApplicationService(BaseApplicationService):
    def __init__(self, repo: MaintenanceProcedureOperationLabelRepository, maintenanceProcedureOperationLabelService: MaintenanceProcedureOperationLabelService,):
        self._repo = repo
        self._maintenanceProcedureOperationLabelService = maintenanceProcedureOperationLabelService

    @debugLogger
    def newId(self, **_kwargs):
        return MaintenanceProcedureOperationLabel.createFrom(skipValidation=True).id()

    @transactional
    @debugLogger
    def createMaintenanceProcedureOperationLabel(self, token: str = None, objectOnly: bool = False, **kwargs):
        obj: MaintenanceProcedureOperationLabel = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._maintenanceProcedureOperationLabelService.createMaintenanceProcedureOperationLabel(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @transactional
    @debugLogger
    def updateMaintenanceProcedureOperationLabel(
        self,
        token: str = None,
        **kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: MaintenanceProcedureOperationLabel = self._repo.maintenanceProcedureOperationLabelById(id=kwargs["id"])
            super().callFunction(
                modelData=BaseApplicationServiceModelData(
                    function=self._maintenanceProcedureOperationLabelService.updateMaintenanceProcedureOperationLabel,
                    kwargs={
                        "oldObject": oldObject,
                        "newObject": self._constructObject(_sourceObject=oldObject, **kwargs),
                        "tokenData": tokenData,
                    },
                )
            )

        except Exception as e:
            raise UpdateMaintenanceProcedureOperationLabelFailedException(message=str(e))

    @transactional
    @debugLogger
    def deleteMaintenanceProcedureOperationLabel(self, id: str, token: str = None, **_kwargs):
        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._maintenanceProcedureOperationLabelService.deleteMaintenanceProcedureOperationLabel,
                kwargs={
                    "obj": self._repo.maintenanceProcedureOperationLabelById(id=id),
                    "tokenData": TokenService.tokenDataFromToken(token=token),
                },
            )
        )

    @transactional
    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = "", **_kwargs):
        super()._bulkCreate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="maintenance_procedure_operation_label_id",
                domainService=self._maintenanceProcedureOperationLabelService,
            )
        )

    @transactional
    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = "", **_kwargs):
        super()._bulkDelete(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="maintenance_procedure_operation_label_id",
                domainService=self._maintenanceProcedureOperationLabelService,
            )
        )

    @transactional
    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = "", **_kwargs):
        super()._bulkUpdate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="maintenance_procedure_operation_label_id",
                domainService=self._maintenanceProcedureOperationLabelService,
                repositoryCallbackFunction=self._repo.maintenanceProcedureOperationLabelById,
            )
        )

    @readOnly
    @debugLogger
    def maintenanceProcedureOperationLabelById(self, id: str, token: str = None, **_kwargs) -> MaintenanceProcedureOperationLabel:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(getterFunction=self._repo.maintenanceProcedureOperationLabelById, kwargs={"id": id})
        )

    @readOnly
    @debugLogger
    def maintenanceProcedureOperationLabels(
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
                getterFunction=self._maintenanceProcedureOperationLabelService.maintenanceProcedureOperationLabels,
                kwargs={"resultFrom": resultFrom, "resultSize": resultSize, "order": order, "tokenData": tokenData},
            )
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> MaintenanceProcedureOperationLabel:
        kwargs[BaseApplicationService.DOMAIN_MODEL_CLASS] = MaintenanceProcedureOperationLabel
        return super()._constructObject(*args, **kwargs)
