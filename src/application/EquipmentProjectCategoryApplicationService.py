"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.domain_model.project.equipment.project_category.EquipmentProjectCategory import EquipmentProjectCategory
from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryRepository import EquipmentProjectCategoryRepository
from src.domain_model.project.equipment.project_category.EquipmentProjectCategoryService import EquipmentProjectCategoryService
from src.domain_model.resource.exception.UpdateEquipmentProjectCategoryFailedException import UpdateEquipmentProjectCategoryFailedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class EquipmentProjectCategoryApplicationService:
    def __init__(self, repo: EquipmentProjectCategoryRepository, equipmentProjectCategoryService: EquipmentProjectCategoryService):
        self._repo = repo
        self._equipmentProjectCategoryService = equipmentProjectCategoryService

    @debugLogger
    def createEquipmentProjectCategory(self, id: str = None, name: str = None, objectOnly: bool = False, token: str = ''):
        obj: EquipmentProjectCategory = self.constructObject(id=id, name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentProjectCategoryService.createEquipmentProjectCategory(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateEquipmentProjectCategory(self, id: str, name: str = None, token: str = None):
        obj: EquipmentProjectCategory = self.constructObject(id=id, name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: EquipmentProjectCategory = self._repo.equipmentProjectCategoryById(id=id)
            self._equipmentProjectCategoryService.updateEquipmentProjectCategory(oldObject=oldObject, newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateEquipmentProjectCategoryFailedException(message=str(e))

    @debugLogger
    def deleteEquipmentProjectCategory(self, id: str, token: str = None):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.equipmentProjectCategoryById(id=id)
        self._equipmentProjectCategoryService.deleteEquipmentProjectCategory(obj=obj, tokenData=tokenData)

    @debugLogger
    def equipmentProjectCategoryById(self, id: str, token: str = None) -> EquipmentProjectCategory:
        equipmentProjectCategory = self._repo.equipmentProjectCategoryById(id=id)
        TokenService.tokenDataFromToken(token=token)
        return equipmentProjectCategory

    @debugLogger
    def equipmentProjectCategorys(self, resultFrom: int = 0, resultSize: int = 100, order: List[dict] = None,
                        token: str = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentProjectCategoryService.equipmentProjectCategorys(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)

    @debugLogger
    def constructObject(self, id: str, name: str = None) -> EquipmentProjectCategory:
        return EquipmentProjectCategory.createFrom(id=id, name=name)
