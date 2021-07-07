"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from typing import List, Tuple

from src.domain_model.project.equipment.Equipment import Equipment
from src.domain_model.project.equipment.EquipmentRepository import EquipmentRepository
from src.domain_model.resource.exception.EquipmentAlreadyExistException import (
    EquipmentAlreadyExistException,
)
from src.domain_model.resource.exception.EquipmentDoesNotExistException import (
    EquipmentDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class EquipmentService:
    def __init__(self, repository: EquipmentRepository):
        self._repo = repository

    @debugLogger
    def createEquipment(
        self, obj: Equipment, objectOnly: bool = False, tokenData: TokenData = None
    ):
        if objectOnly:
            return (
                Equipment.createFromObject(obj=obj, generateNewId=True)
                if obj.id() == ""
                else obj
            )
        else:
            obj = Equipment.createFromObject(obj=obj, publishEvent=True)
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def createEquipmentUsingStandardEquipmentCategoryGroup(
        self, obj: Equipment, standardEquipmentCategoryGroupId:str = "", objectOnly: bool = False, tokenData: TokenData = None
    ):
        obj = Equipment.createFromObject(obj=obj, publishEvent=True)

        from src.domain_model.project.equipment.EquipmentUsingStandardEquipmentCategoryGroupCreated import EquipmentUsingStandardEquipmentCategoryGroupCreated
        DomainPublishedEvents.addEventForPublishing(EquipmentUsingStandardEquipmentCategoryGroupCreated(obj, standardEquipmentCategoryGroupId))

        self._repo.save(obj=obj)
        return obj

    @debugLogger
    def deleteEquipment(self, obj: Equipment, tokenData: TokenData = None, ignoreRelations: bool = False):
        obj.publishDelete()
        self._repo.deleteEquipment(obj=obj, ignoreRelations=ignoreRelations)

    @debugLogger
    def updateEquipment(
        self, oldObject: Equipment, newObject: Equipment, tokenData: TokenData = None
    ):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def linkEquipmentToEquipment(self, srcObj: Equipment, dstObj: Equipment, tokenData: TokenData):
        from src.domain_model.project.equipment.EquipmentToEquipmentLinked import \
            EquipmentToEquipmentLinked
        DomainPublishedEvents.addEventForPublishing(
            EquipmentToEquipmentLinked(sourceObj=srcObj, destinationObj=dstObj))
        self._repo.linkEquipmentToEquipment(srcObj=srcObj, dstObj=dstObj, tokenData=tokenData)

    @debugLogger
    def unlinkEquipmentToEquipment(self, srcObj: Equipment, dstObj: Equipment, tokenData: TokenData):
        from src.domain_model.project.equipment.EquipmentToEquipmentUnlinked import \
            EquipmentToEquipmentUnlinked
        DomainPublishedEvents.addEventForPublishing(
            EquipmentToEquipmentUnlinked(sourceObj=srcObj, destinationObj=dstObj))
        self._repo.unlinkEquipmentToEquipment(srcObj=srcObj, dstObj=dstObj, tokenData=tokenData)

    @debugLogger
    def linkedEquipmentsByEquipmentId(self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        equipmentId: str = None):
        return self._repo.linkedEquipmentsByEquipmentId(
            tokenData=tokenData,
            equipmentId=equipmentId,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def bulkCreate(self, objList: List[Equipment]):
        self._repo.bulkSave(objList=objList)
        for obj in objList:
            Equipment.createFromObject(obj=obj, publishEvent=True)

    @debugLogger
    def bulkDelete(self, objList: List[Equipment]):
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
    def equipments(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        projectId: str = None,
        **_kwargs
    ):
        if projectId is not None:
            return self._repo.equipmentsByProjectId(
                tokenData=tokenData,
                resultFrom=resultFrom,
                resultSize=resultSize,
                order=order,
                projectId=projectId
            )

        return self._repo.equipments(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )
