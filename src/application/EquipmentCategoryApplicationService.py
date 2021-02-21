"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.equipment.category.EquipmentCategory import EquipmentCategory
from src.domain_model.project.equipment.category.EquipmentCategoryRepository import EquipmentCategoryRepository
from src.domain_model.project.equipment.category.EquipmentCategoryService import EquipmentCategoryService
from src.domain_model.resource.exception.UpdateEquipmentCategoryFailedException import UpdateEquipmentCategoryFailedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class EquipmentCategoryApplicationService:
    def __init__(self, repo: EquipmentCategoryRepository, equipmentCategoryService: EquipmentCategoryService):
        self._repo = repo
        self._equipmentCategoryService = equipmentCategoryService

    @debugLogger
    def createEquipmentCategory(self, id: str = None, name: str = '', objectOnly: bool = False, token: str = ''):
        obj: EquipmentCategory = self.constructObject(id=id, name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentCategoryService.createEquipmentCategory(obj=obj,
                                                                objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateEquipmentCategory(self, id: str, name: str, token: str = ''):
        obj: EquipmentCategory = self.constructObject(id=id, name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: EquipmentCategory = self._repo.equipmentCategoryById(id=id)
            self._equipmentCategoryService.updateEquipmentCategory(oldObject=oldObject,
                                                             newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateEquipmentCategoryFailedException(message=str(e))

    @debugLogger
    def deleteEquipmentCategory(self, id: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.equipmentCategoryById(id=id)
        self._equipmentCategoryService.deleteEquipmentCategory(obj=obj, tokenData=tokenData)

    @debugLogger
    def equipmentCategoryByName(self, name: str, token: str = '') -> EquipmentCategory:
        equipmentCategory = self._repo.equipmentCategoryByName(name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return equipmentCategory

    @debugLogger
    def equipmentCategoryById(self, id: str, token: str = '') -> EquipmentCategory:
        equipmentCategory = self._repo.equipmentCategoryById(id=id)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return equipmentCategory

    @debugLogger
    def equipmentCategorys(self, resultFrom: int = 0, resultSize: int = 100, token: str = '',
                        order: List[dict] = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentCategoryService.equipmentCategorys(tokenData=tokenData,
                                                           resultFrom=resultFrom,
                                                           resultSize=resultSize,
                                                           order=order)

    @debugLogger
    def constructObject(self, id: str, name: str) -> EquipmentCategory:
        return EquipmentCategory.createFrom(id=id, name=name)
