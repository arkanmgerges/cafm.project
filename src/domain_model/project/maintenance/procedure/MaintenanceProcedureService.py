"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, Tuple
from src.domain_model.project.maintenance.procedure.MaintenanceProcedure import (
    MaintenanceProcedure,
)
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureRepository import (
    MaintenanceProcedureRepository,
)
from src.domain_model.resource.exception.MaintenanceProcedureAlreadyExistException import (
    MaintenanceProcedureAlreadyExistException,
)
from src.domain_model.resource.exception.MaintenanceProcedureDoesNotExistException import (
    MaintenanceProcedureDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class MaintenanceProcedureService:
    def __init__(self, repository: MaintenanceProcedureRepository):
        self._repo = repository

    @debugLogger
    def createMaintenanceProcedure(
        self,
        obj: MaintenanceProcedure,
        objectOnly: bool = False,
        tokenData: TokenData = None,
    ):
        if objectOnly:
            return (
                MaintenanceProcedure.createFromObject(obj=obj, generateNewId=True)
                if obj.id() == ""
                else obj
            )
        else:
            obj = MaintenanceProcedure.createFromObject(obj=obj, publishEvent=True)
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def deleteMaintenanceProcedure(
        self, obj: MaintenanceProcedure, tokenData: TokenData = None
    ):
        obj.publishDelete()
        self._repo.deleteMaintenanceProcedure(obj=obj)

    @debugLogger
    def updateMaintenanceProcedure(
        self,
        oldObject: MaintenanceProcedure,
        newObject: MaintenanceProcedure,
        tokenData: TokenData = None,
    ):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def bulkCreate(self, objList: List[MaintenanceProcedure]):
        self._repo.bulkSave(objList=objList)
        for obj in objList:
            MaintenanceProcedure.createFromObject(obj=obj, publishEvent=True)

    @debugLogger
    def bulkDelete(self, objList: List[MaintenanceProcedure]):
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
            newObj.publishUpdate(oldObj)

    @debugLogger
    def maintenanceProcedures(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.maintenanceProcedures(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def maintenanceProceduresByEquipmentId(
        self,
        equipmentId: str = None,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.maintenanceProceduresByEquipmentId(
            tokenData=tokenData,
            equipmentId=equipmentId,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )
