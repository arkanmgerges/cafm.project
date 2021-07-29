"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.project.daily_check.procedure.operation.label.DailyCheckProcedureOperationLabelService import DailyCheckProcedureOperationLabelService
from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameterService import DailyCheckProcedureOperationParameterService
from typing import List, Tuple
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperation import (
    DailyCheckProcedureOperation,
)
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationRepository import (
    DailyCheckProcedureOperationRepository,
)
from src.domain_model.resource.exception.DailyCheckProcedureOperationAlreadyExistException import (
    DailyCheckProcedureOperationAlreadyExistException,
)
from src.domain_model.resource.exception.DailyCheckProcedureOperationDoesNotExistException import (
    DailyCheckProcedureOperationDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class DailyCheckProcedureOperationService:
    def __init__(self, repository: DailyCheckProcedureOperationRepository,
        dailyCheckProcedureOperationParameterService: DailyCheckProcedureOperationParameterService,
        dailyCheckProcedureOperationLabelService: DailyCheckProcedureOperationLabelService):
        self._repo = repository
        self._dailyCheckProcedureOperationParameterService = dailyCheckProcedureOperationParameterService
        self._dailyCheckProcedureOperationLabelService = dailyCheckProcedureOperationLabelService

    @debugLogger
    def createDailyCheckProcedureOperation(
        self,
        obj: DailyCheckProcedureOperation,
        objectOnly: bool = False,
        tokenData: TokenData = None,
    ):
        if objectOnly:
            return (
                DailyCheckProcedureOperation.createFromObject(
                    obj=obj, generateNewId=True
                )
                if obj.id() == ""
                else obj
            )
        else:
            obj = DailyCheckProcedureOperation.createFromObject(
                obj=obj, publishEvent=True
            )
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def deleteDailyCheckProcedureOperation(
        self, obj: DailyCheckProcedureOperation, tokenData: TokenData = None
    ):
        obj.publishDelete()
        self._repo.deleteDailyCheckProcedureOperation(obj=obj)

    @debugLogger
    def updateDailyCheckProcedureOperation(
        self,
        oldObject: DailyCheckProcedureOperation,
        newObject: DailyCheckProcedureOperation,
        tokenData: TokenData = None,
    ):
        if newObject.type() != oldObject.type():
            if oldObject.type() == 'visual':
                crtLabels = self._dailyCheckProcedureOperationLabelService.dailyCheckProcedureOperationLabelsByDailyCheckProcedureOperationId(dailyCheckProcedureOperationId=oldObject.id(),tokenData=tokenData)
                for label in crtLabels:
                    self._dailyCheckProcedureOperationLabelService.deleteDailyCheckProcedureOperationLabel(obj=label, tokenData=tokenData)
            if oldObject.type() == 'parameter':
                crtParameters = self._dailyCheckProcedureOperationParameterService.dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationId(dailyCheckProcedureOperationId=oldObject.id(),tokenData=tokenData, resultSize=200)
                for parameter in crtParameters["items"]:
                    self._dailyCheckProcedureOperationParameterService.deleteDailyCheckProcedureOperationParameter(obj=parameter, tokenData=tokenData)

        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def bulkCreate(self, objList: List[DailyCheckProcedureOperation]):
        self._repo.bulkSave(objList=objList)
        for obj in objList:
            DailyCheckProcedureOperation.createFromObject(obj=obj, publishEvent=True)

    @debugLogger
    def bulkDelete(self, objList: List[DailyCheckProcedureOperation]):
        self._repo.bulkDelete(objList=objList)
        for obj in objList:
            obj.publishDelete()

    @debugLogger
    def bulkUpdate(self, objList: List[Tuple]):
        newObjList = list(map(lambda x: x[0], objList))
        self._repo.bulkSave(objList=newObjList)
        for obj in objList:
            newObj = obj[0]
            oldObj = obj[1]

            if newObj.type() != oldObj.type():
                if oldObj.type() == 'visual':
                    crtLabels = self._dailyCheckProcedureOperationLabelService.dailyCheckProcedureOperationLabelsByDailyCheckProcedureOperationId(dailyCheckProcedureOperationId=oldObj.id())
                    for label in crtLabels:
                        self._dailyCheckProcedureOperationLabelService.deleteDailyCheckProcedureOperationLabel(obj=label)
                if oldObj.type() == 'parameter':
                    crtParameters = self._dailyCheckProcedureOperationParameterService.dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationId(dailyCheckProcedureOperationId=oldObj.id(), resultSize=200)
                    for parameter in crtParameters["items"]:
                        self._dailyCheckProcedureOperationParameterService.deleteDailyCheckProcedureOperationParameter(obj=parameter)

            newObj.publishUpdate(oldObj)

    @debugLogger
    def dailyCheckProcedureOperations(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.dailyCheckProcedureOperations(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def dailyCheckProcedureOperationsByDailyCheckProcedureId(
        self,
        dailyCheckProcedureId: str = None,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.dailyCheckProcedureOperationsByDailyCheckProcedureId(
            tokenData=tokenData,
            dailyCheckProcedureId=dailyCheckProcedureId,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )
