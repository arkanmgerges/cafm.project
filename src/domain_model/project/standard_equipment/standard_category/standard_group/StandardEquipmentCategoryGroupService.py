"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List
from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroup import StandardEquipmentCategoryGroup
from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroupRepository import StandardEquipmentCategoryGroupRepository
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class StandardEquipmentCategoryGroupService:
    def __init__(self, repository: StandardEquipmentCategoryGroupRepository):
        self._repo = repository

    @debugLogger
    def createStandardEquipmentCategoryGroup(self, obj: StandardEquipmentCategoryGroup, objectOnly: bool = False, tokenData: TokenData = None):
        if objectOnly:
            return StandardEquipmentCategoryGroup.createFromObject(obj=obj, generateNewId=True) if obj.id() == '' else obj
        else:
            obj = StandardEquipmentCategoryGroup.createFromObject(obj=obj, publishEvent=True)
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def deleteStandardEquipmentCategoryGroup(self, obj: StandardEquipmentCategoryGroup, tokenData: TokenData = None):
        obj.publishDelete()
        self._repo.deleteStandardEquipmentCategoryGroup(obj=obj)

    @debugLogger
    def updateStandardEquipmentCategoryGroup(self, oldObject: StandardEquipmentCategoryGroup, newObject: StandardEquipmentCategoryGroup, tokenData: TokenData = None):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def standardEquipmentCategoryGroups(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
                      order: List[dict] = None):
        return self._repo.standardEquipmentCategoryGroups(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
