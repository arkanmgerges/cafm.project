"""
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
    def createEquipmentProjectCategory(self, id: str = None, name: str = '', objectOnly: bool = False, token: str = ''):
        obj: EquipmentProjectCategory = self.constructObject(id=id, name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentProjectCategoryService.createEquipmentProjectCategory(obj=obj,
                                                  objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateEquipmentProjectCategory(self, id: str, name: str, cityId: int, countryId: int, addressLine: str, beneficiaryId: str,
                      token: str = ''):
        obj: EquipmentProjectCategory = self.constructObject(id=id, name=name, cityId=cityId, countryId=countryId,
                                            addressLine=addressLine,
                                            beneficiaryId=beneficiaryId)
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: EquipmentProjectCategory = self._repo.equipmentProjectCategoryById(id=id)
            self._equipmentProjectCategoryService.updateEquipmentProjectCategory(oldObject=oldObject,
                                               newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateEquipmentProjectCategoryFailedException(message=str(e))

    @debugLogger
    def deleteEquipmentProjectCategory(self, id: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.equipmentProjectCategoryById(id=id)
        self._equipmentProjectCategoryService.deleteEquipmentProjectCategory(obj=obj, tokenData=tokenData)

    @debugLogger
    def equipmentProjectCategoryByName(self, name: str, token: str = '') -> EquipmentProjectCategory:
        equipmentProjectCategory = self._repo.equipmentProjectCategoryByName(name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return equipmentProjectCategory

    @debugLogger
    def equipmentProjectCategoryById(self, id: str, token: str = '') -> EquipmentProjectCategory:
        equipmentProjectCategory = self._repo.equipmentProjectCategoryById(id=id)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return equipmentProjectCategory

    @debugLogger
    def equipmentProjectCategorys(self, resultFrom: int = 0, resultSize: int = 100, token: str = '',
                 order: List[dict] = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentProjectCategoryService.equipmentProjectCategorys(tokenData=tokenData,
                                             resultFrom=resultFrom,
                                             resultSize=resultSize,
                                             order=order)

    @debugLogger
    def constructObject(self, id: str, name: str) -> EquipmentProjectCategory:
        return EquipmentProjectCategory.createFrom(id=id, name=name)
