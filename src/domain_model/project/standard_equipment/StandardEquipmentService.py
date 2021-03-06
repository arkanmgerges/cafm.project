"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, Tuple
from src.domain_model.project.standard_equipment.StandardEquipment import (
    StandardEquipment,
)
from src.domain_model.project.standard_equipment.StandardEquipmentRepository import (
    StandardEquipmentRepository,
)
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class StandardEquipmentService:
    def __init__(self, repository: StandardEquipmentRepository):
        self._repo = repository

    @debugLogger
    def createStandardEquipment(
        self,
        obj: StandardEquipment,
        objectOnly: bool = False,
        tokenData: TokenData = None,
    ):
        if objectOnly:
            return (
                StandardEquipment.createFromObject(obj=obj, generateNewId=True)
                if obj.id() == ""
                else obj
            )
        else:
            obj = StandardEquipment.createFromObject(obj=obj, publishEvent=True)
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def deleteStandardEquipment(
        self, obj: StandardEquipment, tokenData: TokenData = None
    ):
        obj.publishDelete()
        self._repo.deleteStandardEquipment(obj=obj)

    @debugLogger
    def updateStandardEquipment(
        self,
        oldObject: StandardEquipment,
        newObject: StandardEquipment,
        tokenData: TokenData = None,
    ):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def bulkCreate(self, objList: List[StandardEquipment]):
        self._repo.bulkSave(objList=objList)
        for obj in objList:
            StandardEquipment.createFromObject(obj=obj, publishEvent=True)

    @debugLogger
    def bulkDelete(self, objList: List[StandardEquipment]):
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
    def standardEquipments(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.standardEquipments(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )
