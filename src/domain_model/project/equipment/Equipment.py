"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.resource.logging.logger import logger

"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4


class Equipment:
    def __init__(self, id: str = None, name: str = None, projectId: str = None, equipmentProjectCategoryId: str = None,
                 equipmentCategoryId: str = None,
                 equipmentCategoryGroupId: str = None,
                 buildingId: str = None, levelId: str = None, roomId: str = None, manufacturerId: str = None,
                 equipmentModelId: str = None, skipValidation: bool = False, quantity: int = 0):
        self._id = str(uuid4()) if id is None else id
        self._name = name
        self._projectId = projectId
        self._manufacturerId = manufacturerId
        self._equipmentModelId = equipmentModelId
        self._equipmentCategoryId = equipmentCategoryId
        self._equipmentProjectCategoryId = equipmentProjectCategoryId
        self._equipmentCategoryGroupId = equipmentCategoryGroupId
        self._buildingId = buildingId
        self._levelId = levelId
        self._roomId = roomId
        self._quantity = quantity
        if not skipValidation:
            if projectId is None or projectId == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid equipment project id: {projectId}, for equipment id: {id}')
            if equipmentProjectCategoryId is None or equipmentProjectCategoryId == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid equipment project category id: {equipmentProjectCategoryId}, for equipment id: {id}')
            if equipmentCategoryId is None or equipmentCategoryId == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(f'Invalid equipment category id: {equipmentCategoryId}, for equipment id: {id}')
            if equipmentCategoryGroupId is None or equipmentCategoryGroupId == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(f'Invalid equipment group id: {equipmentCategoryGroupId}, for equipment id: {id}')

            if buildingId is None or buildingId == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(f'Invalid equipment building id: {buildingId}, for equipment id: {id}')
            if levelId is None or levelId == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(f'Invalid equipment level id: {levelId}, for equipment id: {id}')
            if roomId is None or roomId == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(f'Invalid equipment room id: {roomId}, for equipment id: {id}')

    @classmethod
    def createFrom(cls, id: str = None, name: str = '', projectId: str = None, equipmentProjectCategoryId: str = None,
                   equipmentCategoryId: str = None,
                   equipmentCategoryGroupId: str = None,
                   buildingId: str = None, levelId: str = None, roomId: str = None, manufacturerId: str = None,
                   equipmentModelId: str = None, publishEvent: bool = False, skipValidation: bool = False, quantity: int = 0):
        from src.domain_model.project.equipment.EquipmentCreated import EquipmentCreated
        obj = Equipment(id=id, name=name, projectId=projectId, equipmentProjectCategoryId=equipmentProjectCategoryId,
                        equipmentCategoryId=equipmentCategoryId,
                        equipmentCategoryGroupId=equipmentCategoryGroupId,
                        buildingId=buildingId, levelId=levelId, roomId=roomId, manufacturerId=manufacturerId,
                        equipmentModelId=equipmentModelId, skipValidation=skipValidation, quantity=quantity)

        if publishEvent:
            from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
            logger.debug(
                f'[{Equipment.createFrom.__qualname__}] - Create equipment with id: {id}')
            DomainPublishedEvents.addEventForPublishing(EquipmentCreated(obj))
        return obj

    @classmethod
    def createFromObject(cls, obj: 'Equipment', publishEvent: bool = False, generateNewId: bool = False,
                         skipValidation: bool = False):
        logger.debug(f'[{Equipment.createFromObject.__qualname__}]')
        id = None if generateNewId else obj.id()
        return cls.createFrom(id=id, name=obj.name(), projectId=obj.projectId(),
                              equipmentProjectCategoryId=obj.equipmentProjectCategoryId(),
                              equipmentCategoryId=obj.equipmentCategoryId(), equipmentCategoryGroupId=obj.equipmentCategoryGroupId(),
                              buildingId=obj.buildingId(), levelId=obj.levelId(), roomId=obj.roomId(),
                              manufacturerId=obj.manufacturerId(), equipmentModelId=obj.equipmentModelId(), quantity=obj.quantity(),
                              skipValidation=skipValidation,
                              publishEvent=publishEvent)

    def id(self) -> str:
        return self._id

    def name(self) -> str:
        return self._name

    def projectId(self) -> str:
        return self._projectId

    def equipmentCategoryId(self) -> str:
        return self._equipmentCategoryId

    def equipmentProjectCategoryId(self) -> str:
        return self._equipmentProjectCategoryId

    def equipmentCategoryGroupId(self) -> str:
        return self._equipmentCategoryGroupId

    def buildingId(self) -> str:
        return self._buildingId

    def levelId(self) -> str:
        return self._levelId

    def roomId(self) -> str:
        return self._roomId

    def manufacturerId(self) -> str:
        return self._manufacturerId

    def equipmentModelId(self) -> str:
        return self._equipmentModelId

    def quantity(self) -> int:
        return self._quantity

    def update(self, data: dict):
        from copy import copy
        updated = False
        old = copy(self)
        # if 'name' in data and data['name'] != self._name:
        #     updated = True
        #     self._name = data['name']
        if updated:
            pass
        # self.publishUpdate(old)

    def publishDelete(self):
        from src.domain_model.project.equipment.EquipmentDeleted import EquipmentDeleted
        DomainPublishedEvents.addEventForPublishing(EquipmentDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.project.equipment.EquipmentUpdated import EquipmentUpdated
        DomainPublishedEvents.addEventForPublishing(EquipmentUpdated(old, self))

    def toMap(self) -> dict:
        return {'id': self.id(), 'name': self.name(), 'project_id': self.projectId(),
                'equipment_project_category_id': self.equipmentProjectCategoryId(),
                'equipment_category_id': self.equipmentCategoryId(), 'equipment_category_group_id': self.equipmentCategoryGroupId(),
                'building_id': self.buildingId(), 'level_id': self.levelId(), 'room_id': self.roomId(),
                'manufacturer_id': self.manufacturerId(), 'equipment_model_id': self.equipmentModelId()}

    def __repr__(self):
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __str__(self) -> str:
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __eq__(self, other):
        if not isinstance(other, Equipment):
            raise NotImplementedError(f'other: {other} can not be compared with Equipment class')
        return self.id() == other.id() and self.name() == other.name() and self.projectId() == other.projectId() and \
               self.equipmentProjectCategoryId() == other.equipmentProjectCategoryId() and \
               self.equipmentCategoryId() == other.equipmentCategoryId() \
               and self.equipmentCategoryGroupId() == other.equipmentCategoryGroupId() and self.buildingId() == other.buildingId() and \
               self.levelId() == other.levelId() and self.roomId() == other.roomId() and \
               self.manufacturerId() == other.manufacturerId()
