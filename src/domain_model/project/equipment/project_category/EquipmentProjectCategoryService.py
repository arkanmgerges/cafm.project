"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.equipment.project_category.EquipmentProjectCategory import EquipmentProjectCategory
from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryRepository import EquipmentProjectCategoryRepository
from src.domain_model.resource.exception.EquipmentProjectCategoryAlreadyExistException import EquipmentProjectCategoryAlreadyExistException
from src.domain_model.resource.exception.EquipmentProjectCategoryDoesNotExistException import EquipmentProjectCategoryDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class EquipmentProjectCategoryService:
    def __init__(self, repository: EquipmentProjectCategoryRepository):
        self._repo = repository

    @debugLogger
    def createEquipmentProjectCategory(self, obj: EquipmentProjectCategory, objectOnly: bool = False, tokenData: TokenData = None):
        try:
            if obj.id() == '':
                raise EquipmentProjectCategoryDoesNotExistException()
            self._repo.equipmentProjectCategoryById(id=obj.id())
            raise EquipmentProjectCategoryAlreadyExistException(obj.name())
        except EquipmentProjectCategoryDoesNotExistException:
            if objectOnly:
                return EquipmentProjectCategory.createFromObject(obj=obj, generateNewId=True) if obj.id() == '' else obj
            else:
                obj = EquipmentProjectCategory.createFromObject(obj=obj, publishEvent=True)
                return obj

    @debugLogger
    def deleteEquipmentProjectCategory(self, obj: EquipmentProjectCategory, tokenData: TokenData = None):
        obj.publishDelete()

    @debugLogger
    def updateEquipmentProjectCategory(self, oldObject: EquipmentProjectCategory, newObject: EquipmentProjectCategory, tokenData: TokenData = None):
        newObject.publishUpdate(oldObject)

    @debugLogger
    def equipmentProjectCategorys(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
                      order: List[dict] = None):
        return self._repo.equipmentProjectCategorys(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
