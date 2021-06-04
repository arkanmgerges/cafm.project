"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.application.model.BaseApplicationServiceBulkData import (
    BaseApplicationServiceBulkData,
)
from src.application.model.BaseApplicationServiceModelData import (
    BaseApplicationServiceModelData,
)
from src.domain_model.project.daily_check.procedure.DailyCheckProcedureRepository import (
    DailyCheckProcedureRepository,
)
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperation import (
    DailyCheckProcedureOperation,
)
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationRepository import (
    DailyCheckProcedureOperationRepository,
)
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationService import (
    DailyCheckProcedureOperationService,
)
from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameterService import (
    DailyCheckProcedureOperationParameterService,
)
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationType import (
    DailyCheckProcedureOperationType,
)
from src.domain_model.resource.exception.UpdateDailyCheckProcedureOperationFailedException import (
    UpdateDailyCheckProcedureOperationFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class DailyCheckProcedureOperationApplicationService(BaseApplicationService):
    def __init__(
        self,
        repo: DailyCheckProcedureOperationRepository,
        dailyCheckProcedureOperationService: DailyCheckProcedureOperationService,
        dailyCheckProcedureRepo: DailyCheckProcedureRepository,
    ):
        self._repo = repo
        self._dailyCheckProcedureOperationService = dailyCheckProcedureOperationService
        self._dailyCheckProcedureRepo = dailyCheckProcedureRepo

    @debugLogger
    def newId(self):
        return DailyCheckProcedureOperation.createFrom(skipValidation=True).id()

    @debugLogger
    def createDailyCheckProcedureOperation(
        self,
        token: str = None,
        objectOnly: bool = False,
        **kwargs,
    ):
        obj: DailyCheckProcedureOperation = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        self._dailyCheckProcedureRepo.dailyCheckProcedureById(
            id=kwargs["dailyCheckProcedureId"]
        )
        return self._dailyCheckProcedureOperationService.createDailyCheckProcedureOperation(
            obj=obj, objectOnly=objectOnly, tokenData=tokenData
        )

    @debugLogger
    def dailyCheckProcedureOperationsByDailyCheckProcedureId(
        self,
        dailyCheckProcedureId: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
        **_kwargs,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._dailyCheckProcedureOperationService.dailyCheckProcedureOperationsByDailyCheckProcedureId(
            tokenData=tokenData,
            dailyCheckProcedureId=dailyCheckProcedureId,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def updateDailyCheckProcedureOperation(
        self,
        token: str = None,
        **kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: DailyCheckProcedureOperation = (
                self._repo.dailyCheckProcedureOperationById(id=kwargs["id"])
            )
            super().callFunction(
                modelData=BaseApplicationServiceModelData(
                    function=self._dailyCheckProcedureOperationService.updateDailyCheckProcedureOperation,
                    kwargs={
                        "oldObject": oldObject,
                        "newObject": self._constructObject(
                            _sourceObject=oldObject, **kwargs
                        ),
                        "tokenData": tokenData,
                    },
                )
            )

        except Exception as e:
            raise UpdateDailyCheckProcedureOperationFailedException(message=str(e))

    @debugLogger
    def deleteDailyCheckProcedureOperation(self, id: str, token: str = None, **_kwargs):
        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._dailyCheckProcedureOperationService.deleteDailyCheckProcedureOperation,
                kwargs={
                    "obj": self._repo.dailyCheckProcedureOperationById(id=id),
                    "tokenData": TokenService.tokenDataFromToken(token=token),
                },
            )
        )

    @debugLogger
    def validateMaintenanceProcedureOperationType(
        self, token: str = None, objectOnly: bool = False, **kwargs
    ):
        import src.port_adapter.AppDi as AppDi

        dailyCheckProcedureOperationParameterService: DailyCheckProcedureOperationParameterService = AppDi.instance.get(
            DailyCheckProcedureOperationParameterService
        )
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj: DailyCheckProcedureOperation = self._repo.dailyCheckProcedureOperationById(
            id=kwargs["id"]
        )

        if obj.type() == DailyCheckProcedureOperationType.VISUAL.value:
            result = dailyCheckProcedureOperationParameterService.dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationId(
                dailyCheckProcedureOperationId=kwargs["id"]
            )
            opParameters = result["items"]

            for parameter in opParameters:
                dailyCheckProcedureOperationParameterService.deleteDailyCheckProcedureOperationParameter(
                    obj=parameter
                )

    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = ""):
        super()._bulkCreate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="daily_check_procedure_operation_id",
                domainService=self._dailyCheckProcedureOperationService,
            )
        )

    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = ""):
        super()._bulkDelete(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="daily_check_procedure_operation_id",
                domainService=self._dailyCheckProcedureOperationService,
            )
        )

    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = ""):
        super()._bulkUpdate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="daily_check_procedure_operation_id",
                domainService=self._dailyCheckProcedureOperationService,
                repositoryCallbackFunction=self._repo.dailyCheckProcedureOperationById,
            )
        )

    @debugLogger
    def dailyCheckProcedureOperationById(
        self, id: str, token: str = None, **_kwargs
    ) -> DailyCheckProcedureOperation:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._repo.dailyCheckProcedureOperationById,
                kwargs={"id": id},
            )
        )

    @debugLogger
    def dailyCheckProcedureOperations(
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
                getterFunction=self._dailyCheckProcedureOperationService.dailyCheckProcedureOperations,
                kwargs={
                    "resultFrom": resultFrom,
                    "resultSize": resultSize,
                    "order": order,
                    "tokenData": tokenData,
                },
            )
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> DailyCheckProcedureOperation:
        kwargs[BaseApplicationService.DOMAIN_MODEL_CLASS] = DailyCheckProcedureOperation
        return super()._constructObject(*args, **kwargs)
