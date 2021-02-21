"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.project.equipment.Equipment import Equipment
from src.domain_model.project.equipment.EquipmentRepository import EquipmentRepository
from src.domain_model.resource.exception.EquipmentAlreadyExistException import EquipmentAlreadyExistException
from src.domain_model.resource.exception.EquipmentDoesNotExistException import EquipmentDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class EquipmentService:
    def __init__(self, repository: EquipmentRepository):
        self._repo = repository

    @debugLogger
    def createEquipment(self, obj: Equipment, objectOnly: bool = False, tokenData: TokenData = None):
        try:
            if obj.id() == '':
                raise EquipmentDoesNotExistException()
            self._repo.equipmentById(id=obj.id())
            raise EquipmentAlreadyExistException(obj.name())
        except EquipmentDoesNotExistException:
            if objectOnly:
                return Equipment.createFromObject(obj=obj, generateNewId=True) if obj.id() == '' else obj
            else:
                obj = Equipment.createFromObject(obj=obj, publishEvent=True)
                return obj

    @debugLogger
    def deleteEquipment(self, obj: Equipment, tokenData: TokenData = None):
        obj.publishDelete()

    @debugLogger
    def updateEquipment(self, oldObject: Equipment, newObject: Equipment, tokenData: TokenData = None):
        newObject.publishUpdate(oldObject)

    @debugLogger
    def equipments(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
                      order: List[dict] = None):
        return self._repo.equipments(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
