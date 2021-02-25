"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.domain_model.project.equipment.Equipment import Equipment
from src.domain_model.project.equipment.EquipmentRepository import EquipmentRepository
from src.domain_model.project.equipment.EquipmentService import EquipmentService
from src.domain_model.resource.exception.UpdateEquipmentFailedException import UpdateEquipmentFailedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class EquipmentApplicationService:
    def __init__(self, repo: EquipmentRepository, equipmentService: EquipmentService):
        self._repo = repo
        self._equipmentService = equipmentService

    @debugLogger
    def createEquipment(self, id: str = None, name: str = None, projectId: str = None, equipmentProjectCategoryId: str = None, equipmentCategoryId: str = None, equipmentCategoryGroupId: str = None, buildingId: str = None, buildingLevelId: str = None, buildingLevelRoomId: str = None, manufacturerId: str = None, equipmentModelId: str = None, quantity: int = None, objectOnly: bool = False, token: str = ''):
        obj: Equipment = self.constructObject(id=id, name=name, projectId=projectId, equipmentProjectCategoryId=equipmentProjectCategoryId, equipmentCategoryId=equipmentCategoryId, equipmentCategoryGroupId=equipmentCategoryGroupId, buildingId=buildingId, buildingLevelId=buildingLevelId, buildingLevelRoomId=buildingLevelRoomId, manufacturerId=manufacturerId, equipmentModelId=equipmentModelId, quantity=quantity)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentService.createEquipment(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateEquipment(self, id: str, name: str = None, projectId: str = None, equipmentProjectCategoryId: str = None, equipmentCategoryId: str = None, equipmentCategoryGroupId: str = None, buildingId: str = None, buildingLevelId: str = None, buildingLevelRoomId: str = None, manufacturerId: str = None, equipmentModelId: str = None, quantity: int = None, token: str = None):
        obj: Equipment = self.constructObject(id=id, name=name, projectId=projectId, equipmentProjectCategoryId=equipmentProjectCategoryId, equipmentCategoryId=equipmentCategoryId, equipmentCategoryGroupId=equipmentCategoryGroupId, buildingId=buildingId, buildingLevelId=buildingLevelId, buildingLevelRoomId=buildingLevelRoomId, manufacturerId=manufacturerId, equipmentModelId=equipmentModelId, quantity=quantity)
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Equipment = self._repo.equipmentById(id=id)
            self._equipmentService.updateEquipment(oldObject=oldObject, newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateEquipmentFailedException(message=str(e))

    @debugLogger
    def deleteEquipment(self, id: str, token: str = None):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.equipmentById(id=id)
        self._equipmentService.deleteEquipment(obj=obj, tokenData=tokenData)

    @debugLogger
    def equipmentById(self, id: str, token: str = None) -> Equipment:
        equipment = self._repo.equipmentById(id=id)
        TokenService.tokenDataFromToken(token=token)
        return equipment

    @debugLogger
    def equipments(self, resultFrom: int = 0, resultSize: int = 100, order: List[dict] = None,
                        token: str = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentService.equipments(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)

    @debugLogger
    def constructObject(self, id: str, name: str = None, projectId: str = None, equipmentProjectCategoryId: str = None, equipmentCategoryId: str = None, equipmentCategoryGroupId: str = None, buildingId: str = None, buildingLevelId: str = None, buildingLevelRoomId: str = None, manufacturerId: str = None, equipmentModelId: str = None, quantity: int = None) -> Equipment:
        return Equipment.createFrom(id=id, name=name, projectId=projectId, equipmentProjectCategoryId=equipmentProjectCategoryId, equipmentCategoryId=equipmentCategoryId, equipmentCategoryGroupId=equipmentCategoryGroupId, buildingId=buildingId, buildingLevelId=buildingLevelId, buildingLevelRoomId=buildingLevelRoomId, manufacturerId=manufacturerId, equipmentModelId=equipmentModelId, quantity=quantity)
