"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.equipment.model.EquipmentModel import EquipmentModel
from src.domain_model.project.equipment.model.EquipmentModelRepository import EquipmentModelRepository
from src.domain_model.project.equipment.model.EquipmentModelService import EquipmentModelService
from src.domain_model.resource.exception.UpdateEquipmentModelFailedException import UpdateEquipmentModelFailedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class EquipmentModelApplicationService:
    def __init__(self, repo: EquipmentModelRepository, equipmentModelService: EquipmentModelService):
        self._repo = repo
        self._equipmentModelService = equipmentModelService

    @debugLogger
    def newId(self):
        return EquipmentModel.createFrom(skipValidation=True).id()

    @debugLogger
    def createEquipmentModel(self, id: str = None, name: str = '', objectOnly: bool = False, token: str = ''):
        obj: EquipmentModel = self.constructObject(id=id, name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentModelService.createEquipmentModel(obj=obj,
                                                                objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateEquipmentModel(self, id: str, name: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: EquipmentModel = self._repo.equipmentModelById(id=id)
            obj: EquipmentModel = self.constructObject(id=id, name=name, _sourceObject = oldObject)
            self._equipmentModelService.updateEquipmentModel(oldObject=oldObject,
                                                             newObject=obj, tokenData=tokenData)
        except Exception as e:
            raise UpdateEquipmentModelFailedException(message=str(e))

    @debugLogger
    def deleteEquipmentModel(self, id: str, token: str = ''):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.equipmentModelById(id=id)
        self._equipmentModelService.deleteEquipmentModel(obj=obj, tokenData=tokenData)

    @debugLogger
    def equipmentModelByName(self, name: str, token: str = '') -> EquipmentModel:
        equipmentModel = self._repo.equipmentModelByName(name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return equipmentModel

    @debugLogger
    def equipmentModelById(self, id: str, token: str = '') -> EquipmentModel:
        equipmentModel = self._repo.equipmentModelById(id=id)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return equipmentModel

    @debugLogger
    def equipmentModels(self, resultFrom: int = 0, resultSize: int = 100, token: str = '',
                        order: List[dict] = None) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._equipmentModelService.equipmentModels(tokenData=tokenData,
                                                           resultFrom=resultFrom,
                                                           resultSize=resultSize,
                                                           order=order)

    @debugLogger
    def constructObject(self, id: str, name: str, _sourceObject: EquipmentModel = None) -> EquipmentModel:
        if _sourceObject is not None:
            return EquipmentModel.createFrom(id=id, name=name if name is not None else _sourceObject.name())
        else:
            return EquipmentModel.createFrom(id=id, name=name)
