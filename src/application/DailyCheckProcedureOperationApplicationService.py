"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperation import (
    DailyCheckProcedureOperation,
)
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationRepository import (
    DailyCheckProcedureOperationRepository,
)
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationService import (
    DailyCheckProcedureOperationService,
)
from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.resource.exception.UpdateDailyCheckProcedureOperationFailedException import (
    UpdateDailyCheckProcedureOperationFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.domain_model.project.daily_check.procedure.DailyCheckProcedureRepository import (
    DailyCheckProcedureRepository,
)


class DailyCheckProcedureOperationApplicationService:
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
        id: str = None,
        name: str = None,
        description: str = None,
        type: str = None,
        dailyCheckProcedureId: str = None,
        objectOnly: bool = False,
        token: str = "",
    ):
        obj: DailyCheckProcedureOperation = self.constructObject(
            id=id,
            name=name,
            description=description,
            type=type,
            dailyCheckProcedureId=dailyCheckProcedureId,
        )
        tokenData = TokenService.tokenDataFromToken(token=token)
        self._dailyCheckProcedureRepo.dailyCheckProcedureById(id=dailyCheckProcedureId)
        return self._dailyCheckProcedureOperationService.createDailyCheckProcedureOperation(
            obj=obj, objectOnly=objectOnly, tokenData=tokenData
        )

    @debugLogger
    def updateDailyCheckProcedureOperation(
        self,
        id: str,
        name: str = None,
        description: str = None,
        type: str = None,
        dailyCheckProcedureId: str = None,
        token: str = None,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: DailyCheckProcedureOperation = (
                self._repo.dailyCheckProcedureOperationById(id=id)
            )
            obj: DailyCheckProcedureOperation = self.constructObject(
                id=id,
                name=name,
                description=description,
                type=type,
                dailyCheckProcedureId=dailyCheckProcedureId,
                _sourceObject=oldObject,
            )
            self._dailyCheckProcedureOperationService.updateDailyCheckProcedureOperation(
                oldObject=oldObject, newObject=obj, tokenData=tokenData
            )
        except Exception as e:
            raise UpdateDailyCheckProcedureOperationFailedException(message=str(e))

    @debugLogger
    def deleteDailyCheckProcedureOperation(self, id: str, token: str = None):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.dailyCheckProcedureOperationById(id=id)
        self._dailyCheckProcedureOperationService.deleteDailyCheckProcedureOperation(
            obj=obj, tokenData=tokenData
        )

    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = ""):
        objList = []
        exceptions = []
        for objListParamsItem in objListParams:
            try:
                objList.append(self.constructObject(id=objListParamsItem["daily_check_procedure_operation_id"],
                                                    name=objListParamsItem["name"],
                                                    description=objListParamsItem["description"],
                                                    type=objListParamsItem["type"],
                                                    dailyCheckProcedureId=objListParamsItem[
                                                        "daily_check_procedure_id"]))
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._dailyCheckProcedureOperationService.bulkCreate(objList=objList)
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
                objList.append(self.constructObject(id=objListParamsItem["daily_check_procedure_operation_id"],
                                                    skipValidation=True))
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._dailyCheckProcedureOperationService.bulkDelete(objList=objList)
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
                oldObject: DailyCheckProcedureOperation = self._repo.dailyCheckProcedureOperationById(
                    id=objListParamsItem["daily_check_procedure_operation_id"])
                newObject = self.constructObject(id=objListParamsItem["daily_check_procedure_operation_id"],
                                                 name=objListParamsItem[
                                                     "name"] if "name" in objListParamsItem else None,
                                                 description=objListParamsItem[
                                                     "description"] if "description" in objListParamsItem else None,
                                                 type=objListParamsItem[
                                                     "type"] if "type" in objListParamsItem else None,
                                                 dailyCheckProcedureId=objListParamsItem[
                                                     "daily_check_procedure_id"] if "daily_check_procedure_id" in objListParamsItem else None,
                                                 _sourceObject=oldObject)
                objList.append((newObject, oldObject), )
            except DomainModelException as e:
                exceptions.append({"reason": {"message": e.message, "code": e.code}})
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            self._dailyCheckProcedureOperationService.bulkUpdate(objList=objList)
            if len(exceptions) > 0:
                raise ProcessBulkDomainException(messages=exceptions)
        except DomainModelException as e:
            exceptions.append({"reason": {"message": e.message, "code": e.code}})
            raise ProcessBulkDomainException(messages=exceptions)

    @debugLogger
    def dailyCheckProcedureOperationById(
        self, id: str, token: str = None
    ) -> DailyCheckProcedureOperation:
        dailyCheckProcedureOperation = self._repo.dailyCheckProcedureOperationById(
            id=id
        )
        TokenService.tokenDataFromToken(token=token)
        return dailyCheckProcedureOperation

    @debugLogger
    def dailyCheckProcedureOperations(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._dailyCheckProcedureOperationService.dailyCheckProcedureOperations(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def dailyCheckProcedureOperationsByDailyCheckProcedureId(
        self,
        dailyCheckProcedureId: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
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
    def constructObject(
        self,
        id: str,
        name: str = None,
        description: str = None,
        type: str = None,
        dailyCheckProcedureId: str = None,
        _sourceObject: DailyCheckProcedureOperation = None,
    ) -> DailyCheckProcedureOperation:
        if _sourceObject is not None:
            return DailyCheckProcedureOperation.createFrom(
                id=id,
                name=name if name is not None else _sourceObject.name(),
                description=description
                if description is not None
                else _sourceObject.description(),
                type=type if type is not None else _sourceObject.type(),
                dailyCheckProcedureId=dailyCheckProcedureId
                if dailyCheckProcedureId is not None
                else _sourceObject.dailyCheckProcedureId(),
            )
        else:
            return DailyCheckProcedureOperation.createFrom(
                id=id,
                name=name,
                description=description,
                type=type,
                dailyCheckProcedureId=dailyCheckProcedureId,
            )
