"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from logging import Logger
from typing import List

from src.domain_model.project.daily_check.procedure.operation.label.DailyCheckProcedureOperationLabel import DailyCheckProcedureOperationLabel
from src.domain_model.project.daily_check.procedure.operation.label.DailyCheckProcedureOperationLabelRepository import DailyCheckProcedureOperationLabelRepository
from src.domain_model.project.daily_check.procedure.operation.label.DailyCheckProcedureOperationLabelService import DailyCheckProcedureOperationLabelService
from src.domain_model.resource.exception.UpdateDailyCheckProcedureOperationLabelFailedException import UpdateDailyCheckProcedureOperationLabelFailedException
from src.domain_model.token.TokenService import TokenService
from src.application.BaseApplicationService import BaseApplicationService
from src.application.lifecycle.decorator.readOnly import readOnly
from src.application.lifecycle.decorator.transactional import transactional
from src.application.model.BaseApplicationServiceBulkData import BaseApplicationServiceBulkData
from src.application.model.BaseApplicationServiceModelData import BaseApplicationServiceModelData
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class DailyCheckProcedureOperationLabelApplicationService(BaseApplicationService):
    def __init__(self, repo: DailyCheckProcedureOperationLabelRepository, dailyCheckProcedureOperationLabelService: DailyCheckProcedureOperationLabelService,):
        self._repo = repo
        self._dailyCheckProcedureOperationLabelService = dailyCheckProcedureOperationLabelService

    @debugLogger
    def newId(self, **_kwargs):
        return DailyCheckProcedureOperationLabel.createFrom(skipValidation=True).id()

    @transactional
    @debugLogger
    def createDailyCheckProcedureOperationLabel(self, token: str = None, objectOnly: bool = False, **kwargs):
        obj: DailyCheckProcedureOperationLabel = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._dailyCheckProcedureOperationLabelService.createDailyCheckProcedureOperationLabel(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @transactional
    @debugLogger
    def updateDailyCheckProcedureOperationLabel(
        self,
        token: str = None,
        **kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: DailyCheckProcedureOperationLabel = self._repo.dailyCheckProcedureOperationLabelById(id=kwargs["id"])
            super().callFunction(
                modelData=BaseApplicationServiceModelData(
                    function=self._dailyCheckProcedureOperationLabelService.updateDailyCheckProcedureOperationLabel,
                    kwargs={
                        "oldObject": oldObject,
                        "newObject": self._constructObject(_sourceObject=oldObject, **kwargs),
                        "tokenData": tokenData,
                    },
                )
            )

        except Exception as e:
            raise UpdateDailyCheckProcedureOperationLabelFailedException(message=str(e))

    @transactional
    @debugLogger
    def deleteDailyCheckProcedureOperationLabel(self, id: str, token: str = None, **_kwargs):
        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._dailyCheckProcedureOperationLabelService.deleteDailyCheckProcedureOperationLabel,
                kwargs={
                    "obj": self._repo.dailyCheckProcedureOperationLabelById(id=id),
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
                sourceId="daily_check_procedure_operation_label_id",
                domainService=self._dailyCheckProcedureOperationLabelService,
            )
        )

    @transactional
    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = "", **_kwargs):
        super()._bulkDelete(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="daily_check_procedure_operation_label_id",
                domainService=self._dailyCheckProcedureOperationLabelService,
            )
        )

    @transactional
    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = "", **_kwargs):
        super()._bulkUpdate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="daily_check_procedure_operation_label_id",
                domainService=self._dailyCheckProcedureOperationLabelService,
                repositoryCallbackFunction=self._repo.dailyCheckProcedureOperationLabelById,
            )
        )

    @readOnly
    @debugLogger
    def dailyCheckProcedureOperationLabelById(self, id: str, token: str = None, **_kwargs) -> DailyCheckProcedureOperationLabel:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(getterFunction=self._repo.dailyCheckProcedureOperationLabelById, kwargs={"id": id})
        )

    @readOnly
    @debugLogger
    def dailyCheckProcedureOperationLabels(
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
                getterFunction=self._dailyCheckProcedureOperationLabelService.dailyCheckProcedureOperationLabels,
                kwargs={"resultFrom": resultFrom, "resultSize": resultSize, "order": order, "tokenData": tokenData},
            )
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> DailyCheckProcedureOperationLabel:
        kwargs[BaseApplicationService.DOMAIN_MODEL_CLASS] = DailyCheckProcedureOperationLabel
        return super()._constructObject(*args, **kwargs)
