"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.equipment.model.EquipmentModel import EquipmentModel
from src.domain_model.project.equipment.model.EquipmentModelRepository import EquipmentModelRepository
from src.domain_model.resource.exception.EquipmentModelAlreadyExistException import EquipmentModelAlreadyExistException
from src.domain_model.resource.exception.EquipmentModelDoesNotExistException import EquipmentModelDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class EquipmentModelService:
    def __init__(self, repository: EquipmentModelRepository):
        self._repo = repository

    @debugLogger
    def createEquipmentModel(self, obj: EquipmentModel, objectOnly: bool = False, tokenData: TokenData = None):
        try:
            if obj.id() == '':
                raise EquipmentModelDoesNotExistException()
            self._repo.equipmentModelById(id=obj.id())
            raise EquipmentModelAlreadyExistException(obj.name())
        except EquipmentModelDoesNotExistException:
            if objectOnly:
                return EquipmentModel.createFromObject(obj=obj, generateNewId=True) if obj.id() == '' else obj
            else:
                obj = EquipmentModel.createFromObject(obj=obj, publishEvent=True)
                return obj

    @debugLogger
    def deleteEquipmentModel(self, obj: EquipmentModel, tokenData: TokenData = None):
        obj.publishDelete()

    @debugLogger
    def updateEquipmentModel(self, oldObject: EquipmentModel, newObject: EquipmentModel, tokenData: TokenData = None):
        newObject.publishUpdate(oldObject)

    @debugLogger
    def equipmentModels(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
                      order: List[dict] = None):
        return self._repo.equipmentModels(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
