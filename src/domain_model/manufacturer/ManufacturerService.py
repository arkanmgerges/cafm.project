"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, Tuple

from src.domain_model.manufacturer.Manufacturer import Manufacturer
from src.domain_model.manufacturer.ManufacturerRepository import ManufacturerRepository
from src.domain_model.resource.exception.ManufacturerAlreadyExistException import (
    ManufacturerAlreadyExistException,
)
from src.domain_model.resource.exception.ManufacturerDoesNotExistException import (
    ManufacturerDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class ManufacturerService:
    def __init__(self, repository: ManufacturerRepository):
        self._repo = repository

    @debugLogger
    def createManufacturer(
        self, obj: Manufacturer, objectOnly: bool = False, tokenData: TokenData = None
    ):
        if objectOnly:
            return (
                Manufacturer.createFromObject(obj=obj, generateNewId=True)
                if obj.id() == ""
                else obj
            )
        else:
            obj = Manufacturer.createFromObject(obj=obj, publishEvent=True)
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def deleteManufacturer(self, obj: Manufacturer, tokenData: TokenData = None):
        obj.publishDelete()
        self._repo.deleteManufacturer(obj=obj)

    @debugLogger
    def updateManufacturer(
        self,
        oldObject: Manufacturer,
        newObject: Manufacturer,
        tokenData: TokenData = None,
    ):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def bulkCreate(self, objList: List[Manufacturer]):
        self._repo.bulkSave(objList=objList)
        for obj in objList:
            Manufacturer.createFromObject(obj=obj, publishEvent=True)

    @debugLogger
    def bulkDelete(self, objList: List[Manufacturer]):
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
    def manufacturers(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.manufacturers(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )
