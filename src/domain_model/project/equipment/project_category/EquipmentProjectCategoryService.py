"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, Tuple

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import (
    EquipmentCategoryGroup,
)
from src.domain_model.project.equipment.project_category.EquipmentProjectCategory import (
    EquipmentProjectCategory,
)
from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryRepository import (
    EquipmentProjectCategoryRepository,
)
from src.domain_model.resource.exception.EquipmentProjectCategoryAlreadyExistException import (
    EquipmentProjectCategoryAlreadyExistException,
)
from src.domain_model.resource.exception.EquipmentProjectCategoryDoesNotExistException import (
    EquipmentProjectCategoryDoesNotExistException,
)
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class EquipmentProjectCategoryService:
    def __init__(self, repository: EquipmentProjectCategoryRepository):
        self._repo = repository

    @debugLogger
    def createEquipmentProjectCategory(
        self,
        obj: EquipmentProjectCategory,
        objectOnly: bool = False,
        tokenData: TokenData = None,
    ):
        if objectOnly:
            return (
                EquipmentProjectCategory.createFromObject(obj=obj, generateNewId=True)
                if obj.id() == ""
                else obj
            )
        else:
            obj = EquipmentProjectCategory.createFromObject(obj=obj, publishEvent=True)
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def deleteEquipmentProjectCategory(
        self, obj: EquipmentProjectCategory, tokenData: TokenData = None
    ):
        obj.publishDelete()
        self._repo.deleteEquipmentProjectCategory(obj=obj)

    @debugLogger
    def updateEquipmentProjectCategory(
        self,
        oldObject: EquipmentProjectCategory,
        newObject: EquipmentProjectCategory,
        tokenData: TokenData = None,
    ):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def bulkCreate(self, objList: List[EquipmentProjectCategory]):
        self._repo.bulkSave(objList=objList)
        for obj in objList:
            EquipmentProjectCategory.createFromObject(obj=obj, publishEvent=True)

    @debugLogger
    def bulkDelete(self, objList: List[EquipmentProjectCategory]):
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
    def equipmentProjectCategories(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.equipmentProjectCategories(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def linkEquipmentProjectCategoryToGroup(
        self,
        category: EquipmentProjectCategory,
        group: EquipmentCategoryGroup,
        tokenData: TokenData = None,
    ):
        from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryGroupLinked import (
            EquipmentProjectCategoryGroupLinked,
        )

        DomainPublishedEvents.addEventForPublishing(
            EquipmentProjectCategoryGroupLinked(category=category, group=group)
        )

    @debugLogger
    def unlinkEquipmentProjectCategoryToGroup(
        self,
        category: EquipmentProjectCategory,
        group: EquipmentCategoryGroup,
        tokenData: TokenData = None,
    ):
        from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryGroupUnLinked import (
            EquipmentProjectCategoryGroupUnLinked,
        )

        DomainPublishedEvents.addEventForPublishing(
            EquipmentProjectCategoryGroupUnLinked(category=category, group=group)
        )

    def equipmentCategoryGroupsByEquipmentProjectCategoryId(
        self,
        tokenData: TokenData = None,
        id: str = "",
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.equipmentCategoryGroupsByEquipmentProjectCategoryId(
            tokenData=tokenData,
            id=id,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def equipmentProjectCategoriesByProjectId(
        self,
        projectId: str = ""
    ):
        return self._repo.equipmentProjectCategoriesByProjectId(
            projectId=projectId
        )