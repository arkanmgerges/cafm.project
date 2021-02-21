"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.equipment.category.group.EquipmentCategoryGroup import EquipmentCategoryGroup
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupRepository import \
    EquipmentCategoryGroupRepository
from src.domain_model.project.equipment.category.group.EquipmentCategoryGroupService import \
    EquipmentCategoryGroupService
from src.domain_model.resource.exception.UpdateEquipmentCategoryGroupFailedException import \
    UpdateEquipmentCategoryGroupFailedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class EquipmentCategoryGroupApplicationService:
    def __init__(self, repo: EquipmentCategoryGroupRepository,
                 equipmentCategoryGroupService: EquipmentCategoryGroupService):
        self._repo = repo
        self._equipmentCategoryGroupService = equipmentCategoryGroupService

    @debugLogger
    def createEquipmentCategoryGroup(self, id: str = None, name: str = '', equipmentCategoryId: str = None,
                                     objectOnly: bool = False, token: str = ''):
        obj: EquipmentCategoryGroup = self.constructObject(id=id, name=name, equipmentCategoryId=equipmentCategoryId)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentCategoryGroupService.createEquipmentCategoryGroup(obj=obj,
                                                                                objectOnly=objectOnly,
                                                                                tokenData=tokenData)

    @debugLogger
    def updateEquipmentCategoryGroup(self, id: str, name: str, equipmentCategoryId: str = None, token: str = ''):
        obj: EquipmentCategoryGroup = self.constructObject(id=id, name=name, equipmentCategoryId=equipmentCategoryId)
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: EquipmentCategoryGroup = self._repo.equipmentCategoryGroupById(id=id)
            self._equipmentCategoryGroupService.updateEquipmentCategoryGroup(oldObject=oldObject,
                                                                             newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateEquipmentCategoryGroupFailedException(message=str(e))

    @debugLogger
    def deleteEquipmentCategoryGroup(self, id: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.equipmentCategoryGroupById(id=id)
        self._equipmentCategoryGroupService.deleteEquipmentCategoryGroup(obj=obj, tokenData=tokenData)

    @debugLogger
    def equipmentCategoryGroupByName(self, name: str, token: str = '') -> EquipmentCategoryGroup:
        equipmentCategoryGroup = self._repo.equipmentCategoryGroupByName(name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return equipmentCategoryGroup

    @debugLogger
    def equipmentCategoryGroupById(self, id: str, token: str = '') -> EquipmentCategoryGroup:
        equipmentCategoryGroup = self._repo.equipmentCategoryGroupById(id=id)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return equipmentCategoryGroup

    @debugLogger
    def equipmentCategoryGroups(self, resultFrom: int = 0, resultSize: int = 100, token: str = '',
                                order: List[dict] = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentCategoryGroupService.equipmentCategoryGroups(tokenData=tokenData,
                                                                           resultFrom=resultFrom,
                                                                           resultSize=resultSize,
                                                                           order=order)

    @debugLogger
    def constructObject(self, id: str, name: str, equipmentCategoryId: str) -> EquipmentCategoryGroup:
        return EquipmentCategoryGroup.createFrom(id=id, name=name, equipmentCategoryId=equipmentCategoryId)
