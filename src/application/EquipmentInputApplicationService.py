"""
The file is generated by scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from typing import List

from src.domain_model.project.equipment.input.EquipmentInput import EquipmentInput
from src.domain_model.project.equipment.input.EquipmentInputRepository import EquipmentInputRepository
from src.domain_model.project.equipment.input.EquipmentInputService import EquipmentInputService
from src.domain_model.resource.exception.UpdateEquipmentInputFailedException import UpdateEquipmentInputFailedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger

class EquipmentInputApplicationService:
    def __init__(self, repo: EquipmentInputRepository, equipmentInputService: EquipmentInputService,):
        self._repo = repo
        self._equipmentInputService = equipmentInputService

    @debugLogger
    def newId(self):
        return EquipmentInput.createFrom(skipValidation=True).id()

    @debugLogger
    def createEquipmentInput(self, id: str = None, name: str = None, value: str = None, unitId: str = None, equipmentId: str = None, objectOnly: bool = False, token: str = ''):
        obj: EquipmentInput = self.constructObject(id=id, name=name, value=value, unitId=unitId, equipmentId=equipmentId)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentInputService.createEquipmentInput(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateEquipmentInput(self, id: str, name: str = None, value: str = None, unitId: str = None, equipmentId: str = None, token: str = None):
        obj: EquipmentInput = self.constructObject(id=id, name=name, value=value, unitId=unitId, equipmentId=equipmentId)
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: EquipmentInput = self._repo.equipmentInputById(id=id)
            self._equipmentInputService.updateEquipmentInput(oldObject=oldObject, newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateEquipmentInputFailedException(message=str(e))

    @debugLogger
    def deleteEquipmentInput(self, id: str, token: str = None):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.equipmentInputById(id=id)
        self._equipmentInputService.deleteEquipmentInput(obj=obj, tokenData=tokenData)

    @debugLogger
    def equipmentInputById(self, id: str, token: str = None) -> EquipmentInput:
        equipmentInput = self._repo.equipmentInputById(id=id)
        TokenService.tokenDataFromToken(token=token)
        return equipmentInput

    @debugLogger
    def equipmentInputs(self, resultFrom: int = 0, resultSize: int = 100, order: List[dict] = None,
                        token: str = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentInputService.equipmentInputs(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)

    @debugLogger
    def constructObject(self, id: str, name: str = None, value: str = None, unitId: str = None, equipmentId: str = None) -> EquipmentInput:
        return EquipmentInput.createFrom(id=id, name=name, value=value, unitId=unitId, equipmentId=equipmentId)
