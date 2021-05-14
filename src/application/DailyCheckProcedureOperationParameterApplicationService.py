"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.application.model.BaseApplicationServiceBulkData import BaseApplicationServiceBulkData
from src.application.model.BaseApplicationServiceModelData import BaseApplicationServiceModelData
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationRepository import (
    DailyCheckProcedureOperationRepository,
)
from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameter import (
    DailyCheckProcedureOperationParameter,
)
from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameterRepository import (
    DailyCheckProcedureOperationParameterRepository,
)
from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameterService import (
    DailyCheckProcedureOperationParameterService,
)
from src.domain_model.project.unit.UnitRepository import UnitRepository
from src.domain_model.resource.exception.UpdateDailyCheckProcedureOperationParameterFailedException import (
    UpdateDailyCheckProcedureOperationParameterFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class DailyCheckProcedureOperationParameterApplicationService(BaseApplicationService):
    def __init__(
        self,
        repo: DailyCheckProcedureOperationParameterRepository,
        dailyCheckProcedureOperationParameterService: DailyCheckProcedureOperationParameterService,
        unitRepo: UnitRepository,
        dailyCheckProcedureOperationRepo: DailyCheckProcedureOperationRepository,
    ):
        self._repo = repo
        self._dailyCheckProcedureOperationParameterService = dailyCheckProcedureOperationParameterService
        self._unitRepo = unitRepo
        self._dailyCheckProcedureOperationRepo = dailyCheckProcedureOperationRepo

    @debugLogger
    def newId(self):
        return DailyCheckProcedureOperationParameter.createFrom(skipValidation=True).id()

    @debugLogger
    def createDailyCheckProcedureOperationParameter(
        self,
        token: str = None,
        objectOnly: bool = False,
        **kwargs,
    ):
        obj: DailyCheckProcedureOperationParameter = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        self._unitRepo.unitById(id=kwargs["unitId"])
        self._dailyCheckProcedureOperationRepo.dailyCheckProcedureOperationById(
            id=kwargs["dailyCheckProcedureOperationId"]
        )
        return self._dailyCheckProcedureOperationParameterService.createDailyCheckProcedureOperationParameter(
            obj=obj, objectOnly=objectOnly, tokenData=tokenData
        )

    @debugLogger
    def dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationId(
        self,
        dailyCheckProcedureOperationId: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._dailyCheckProcedureOperationParameterService.dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationId(
            tokenData=tokenData,
            dailyCheckProcedureOperationId=dailyCheckProcedureOperationId,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def updateDailyCheckProcedureOperationParameter(
        self,
        token: str = None,
        **kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: DailyCheckProcedureOperationParameter = self._repo.dailyCheckProcedureOperationParameterById(
                id=kwargs["id"]
            )
            super().callFunction(
                modelData=BaseApplicationServiceModelData(
                    function=self._dailyCheckProcedureOperationParameterService.updateDailyCheckProcedureOperationParameter,
                    kwargs={
                        "oldObject": oldObject,
                        "newObject": self._constructObject(_sourceObject=oldObject, **kwargs),
                        "tokenData": tokenData,
                    },
                )
            )

        except Exception as e:
            raise UpdateDailyCheckProcedureOperationParameterFailedException(message=str(e))

    @debugLogger
    def deleteDailyCheckProcedureOperationParameter(self, id: str, token: str = None):
        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._dailyCheckProcedureOperationParameterService.deleteDailyCheckProcedureOperationParameter,
                kwargs={
                    "obj": self._repo.dailyCheckProcedureOperationParameterById(id=id),
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
                sourceId="daily_check_procedure_operation_parameter_id",
                domainService=self._dailyCheckProcedureOperationParameterService,
            )
        )

    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = ""):
        super()._bulkDelete(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="daily_check_procedure_operation_parameter_id",
                domainService=self._dailyCheckProcedureOperationParameterService,
            )
        )

    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = ""):
        super()._bulkUpdate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="daily_check_procedure_operation_parameter_id",
                domainService=self._dailyCheckProcedureOperationParameterService,
                repositoryCallbackFunction=self._repo.dailyCheckProcedureOperationParameterById,
            )
        )

    @debugLogger
    def dailyCheckProcedureOperationParameterById(
        self, id: str, token: str = None
    ) -> DailyCheckProcedureOperationParameter:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._repo.dailyCheckProcedureOperationParameterById, kwargs={"id": id}
            )
        )

    @debugLogger
    def dailyCheckProcedureOperationParameters(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._dailyCheckProcedureOperationParameterService.dailyCheckProcedureOperationParameters,
                kwargs={"resultFrom": resultFrom, "resultSize": resultSize, "order": order, "tokenData": tokenData},
            )
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> DailyCheckProcedureOperationParameter:
        kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS] = DailyCheckProcedureOperationParameter
        return super()._constructObject(*args, **kwargs)
