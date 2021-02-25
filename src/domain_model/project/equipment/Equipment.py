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
    def __init__(self, id: str = None,
                 name: str = None,
                 projectId: str = None,
                 equipmentProjectCategoryId: str = None,
                 equipmentCategoryId: str = None,
                 equipmentCategoryGroupId: str = None,
                 buildingId: str = None,
                 buildingLevelId: str = None,
                 buildingLevelRoomId: str = None,
                 manufacturerId: str = None,
                 equipmentModelId: str = None,
                 skipValidation: bool = False, quantity: int = 0):
        self._id = str(uuid4()) if id is None else id
        self._name = name
        self._projectId = projectId
        self._manufacturerId = manufacturerId
        self._equipmentModelId = equipmentModelId
        self._equipmentCategoryId = equipmentCategoryId
        self._equipmentProjectCategoryId = equipmentProjectCategoryId
        self._equipmentCategoryGroupId = equipmentCategoryGroupId
        self._buildingId = buildingId
        self._buildingLevelId = buildingLevelId
        self._buildingLevelRoomId = buildingLevelRoomId
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
            if buildingLevelId is None or buildingLevelId == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(f'Invalid equipment level id: {buildingLevelId}, for equipment id: {id}')
            if buildingLevelRoomId is None or buildingLevelRoomId == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(f'Invalid equipment room id: {buildingLevelRoomId}, for equipment id: {id}')

            if quantity <= -1:
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(f'Invalid equipment quantity: {quantity}, for equipment id: {id}')

    @classmethod
    def createFrom(cls, id: str = None, name: str = '', projectId: str = None, equipmentProjectCategoryId: str = None,
                   equipmentCategoryId: str = None,
                   equipmentCategoryGroupId: str = None,
                   buildingId: str = None, buildingLevelId: str = None, buildingLevelRoomId: str = None, manufacturerId: str = None,
                   equipmentModelId: str = None, publishEvent: bool = False, quantity: int = -1, skipValidation: bool = False):
        from src.domain_model.project.equipment.EquipmentCreated import EquipmentCreated
        obj = Equipment(id=id, name=name, projectId=projectId, equipmentProjectCategoryId=equipmentProjectCategoryId,
                        equipmentCategoryId=equipmentCategoryId,
                        equipmentCategoryGroupId=equipmentCategoryGroupId,
                        buildingId=buildingId, buildingLevelId=buildingLevelId, buildingLevelRoomId=buildingLevelRoomId, manufacturerId=manufacturerId,
                        equipmentModelId=equipmentModelId, quantity=quantity, skipValidation=skipValidation)

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
                              buildingId=obj.buildingId(), buildingLevelId=obj.buildingLevelId(), buildingLevelRoomId=obj.buildingLevelRoomId(),
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

    def buildingLevelId(self) -> str:
        return self._buildingLevelId

    def buildingLevelRoomId(self) -> str:
        return self._buildingLevelRoomId

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
                'building_id': self.buildingId(), 'building_level_id': self.buildingLevelId(), 'building_level_room_id': self.buildingLevelRoomId(),
                'manufacturer_id': self.manufacturerId(), 'equipment_model_id': self.equipmentModelId(), 'quantity': self.quantity()}

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
               self.buildingLevelId() == other.buildingLevelId() and self.buildingLevelRoomId() == other.buildingLevelRoomId() and \
               self.manufacturerId() == other.manufacturerId()
