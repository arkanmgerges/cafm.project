"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.equipment.category.EquipmentCategory import EquipmentCategory
from src.domain_model.project.equipment.category.EquipmentCategoryRepository import EquipmentCategoryRepository
from src.domain_model.resource.exception.EquipmentCategoryAlreadyExistException import EquipmentCategoryAlreadyExistException
from src.domain_model.resource.exception.EquipmentCategoryDoesNotExistException import EquipmentCategoryDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class EquipmentCategoryService:
    def __init__(self, repository: EquipmentCategoryRepository):
        self._repo = repository

    @debugLogger
    def createEquipmentCategory(self, obj: EquipmentCategory, objectOnly: bool = False, tokenData: TokenData = None):
        try:
            if obj.id() == '':
                raise EquipmentCategoryDoesNotExistException()
            self._repo.equipmentCategoryById(id=obj.id())
            raise EquipmentCategoryAlreadyExistException(obj.name())
        except EquipmentCategoryDoesNotExistException:
            if objectOnly:
                return EquipmentCategory.createFromObject(obj=obj, generateNewId=True) if obj.id() == '' else obj
            else:
                obj = EquipmentCategory.createFromObject(obj=obj, publishEvent=True)
                return obj

    @debugLogger
    def deleteEquipmentCategory(self, obj: EquipmentCategory, tokenData: TokenData = None):
        obj.publishDelete()

    @debugLogger
    def updateEquipmentCategory(self, oldObject: EquipmentCategory, newObject: EquipmentCategory, tokenData: TokenData = None):
        newObject.publishUpdate(oldObject)

    @debugLogger
    def equipmentCategorys(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
                      order: List[dict] = None):
        return self._repo.equipmentCategorys(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
