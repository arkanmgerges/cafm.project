"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, Tuple

from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import (
    EquipmentCategoryGroup,
)
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupRepository import (
    EquipmentCategoryGroupRepository,
)
from src.domain_model.resource.exception.EquipmentCategoryGroupAlreadyExistException import (
    EquipmentCategoryGroupAlreadyExistException,
)
from src.domain_model.resource.exception.EquipmentCategoryGroupDoesNotExistException import (
    EquipmentCategoryGroupDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class EquipmentCategoryGroupService:
    def __init__(self, repository: EquipmentCategoryGroupRepository):
        self._repo = repository

    @debugLogger
    def createEquipmentCategoryGroup(
        self,
        obj: EquipmentCategoryGroup,
        objectOnly: bool = False,
        tokenData: TokenData = None,
    ):
        if objectOnly:
            return (
                EquipmentCategoryGroup.createFromObject(obj=obj, generateNewId=True)
                if obj.id() == ""
                else obj
            )
        else:
            obj = EquipmentCategoryGroup.createFromObject(obj=obj, publishEvent=True)
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def deleteEquipmentCategoryGroup(
        self, obj: EquipmentCategoryGroup, tokenData: TokenData = None
    ):
        obj.publishDelete()
        self._repo.deleteEquipmentCategoryGroup(obj=obj)

    @debugLogger
    def updateEquipmentCategoryGroup(
        self,
        oldObject: EquipmentCategoryGroup,
        newObject: EquipmentCategoryGroup,
        tokenData: TokenData = None,
    ):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def bulkCreate(self, objList: List[EquipmentCategoryGroup]):
        self._repo.bulkSave(objList=objList)
        for obj in objList:
            EquipmentCategoryGroup.createFromObject(obj=obj, publishEvent=True)

    @debugLogger
    def bulkDelete(self, objList: List[EquipmentCategoryGroup]):
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
    def equipmentCategoryGroups(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.equipmentCategoryGroups(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def equipmentCategoryGroupsByEquipmentProjectCategoryId(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        equipmentProjectCategoryId: str = None,
    ):
        return self._repo.equipmentCategoryGroupsByEquipmentProjectCategoryId(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            equipmentProjectCategoryId=equipmentProjectCategoryId
        )

    @debugLogger
    def equipmentCategoryGroupsByProjectId(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        projectId: str = None,
    ):
        return self._repo.equipmentCategoryGroupsByProjectId(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            projectId=projectId
        )