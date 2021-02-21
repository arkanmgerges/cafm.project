"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import EquipmentCategoryGroup
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupRepository import EquipmentCategoryGroupRepository
from src.domain_model.resource.exception.EquipmentCategoryGroupAlreadyExistException import EquipmentCategoryGroupAlreadyExistException
from src.domain_model.resource.exception.EquipmentCategoryGroupDoesNotExistException import EquipmentCategoryGroupDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class EquipmentCategoryGroupService:
    def __init__(self, repository: EquipmentCategoryGroupRepository):
        self._repo = repository

    @debugLogger
    def createEquipmentCategoryGroup(self, obj: EquipmentCategoryGroup, objectOnly: bool = False, tokenData: TokenData = None):
        try:
            if obj.id() == '':
                raise EquipmentCategoryGroupDoesNotExistException()
            self._repo.equipmentCategoryGroupById(id=obj.id())
            raise EquipmentCategoryGroupAlreadyExistException(obj.name())
        except EquipmentCategoryGroupDoesNotExistException:
            if objectOnly:
                return EquipmentCategoryGroup.createFromObject(obj=obj, generateNewId=True) if obj.id() == '' else obj
            else:
                obj = EquipmentCategoryGroup.createFromObject(obj=obj, publishEvent=True)
                return obj

    @debugLogger
    def deleteEquipmentCategoryGroup(self, obj: EquipmentCategoryGroup, tokenData: TokenData = None):
        obj.publishDelete()

    @debugLogger
    def updateEquipmentCategoryGroup(self, oldObject: EquipmentCategoryGroup, newObject: EquipmentCategoryGroup, tokenData: TokenData = None):
        newObject.publishUpdate(oldObject)

    @debugLogger
    def equipmentCategoryGroups(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
                      order: List[dict] = None):
        return self._repo.equipmentCategoryGroups(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
