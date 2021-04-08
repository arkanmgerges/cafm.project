"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.resource.logging.logger import logger

from uuid import uuid4

class StandardEquipmentCategoryGroup:
    def __init__(self, id: str = None, name: str = None, standardEquipmentCategoryId: str = None, skipValidation: bool = False):
        if not skipValidation:
            if name is None or name == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid standard equipment category group name: {name}, for standard equipment category group id: {id}')
            if standardEquipmentCategoryId is None or standardEquipmentCategoryId == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid standard equipment category group standard_equipment_category_id: {standardEquipmentCategoryId}, for standard equipment category group id: {id}')

        self._id = str(uuid4()) if id is None else id
        self._name = name
        self._standardEquipmentCategoryId = standardEquipmentCategoryId



    @classmethod
    def createFrom(cls, id: str = None, name: str = None, standardEquipmentCategoryId: str = None, publishEvent: bool = False, skipValidation: bool = False):
        from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroupCreated import StandardEquipmentCategoryGroupCreated
        obj = StandardEquipmentCategoryGroup(id=id, 
			name=name,
			standardEquipmentCategoryId=standardEquipmentCategoryId, skipValidation=skipValidation)

        if publishEvent:
            logger.debug(
                f'[{StandardEquipmentCategoryGroup.createFrom.__qualname__}] - Create standard equipment category group with id: {id}')
            DomainPublishedEvents.addEventForPublishing(StandardEquipmentCategoryGroupCreated(obj))
        return obj

    @classmethod
    def createFromObject(cls, obj: 'StandardEquipmentCategoryGroup', publishEvent: bool = False, generateNewId: bool = False,
                         skipValidation: bool = False):
        logger.debug(f'[{StandardEquipmentCategoryGroup.createFromObject.__qualname__}]')
        id = None if generateNewId else obj.id()
        return cls.createFrom(id=id, 
			name=obj.name(),
			standardEquipmentCategoryId=obj.standardEquipmentCategoryId(),
                              skipValidation=skipValidation,
                              publishEvent=publishEvent)


    def id(self) -> str:
        return self._id    
    
    def name(self) -> str:
        return self._name
    
    def standardEquipmentCategoryId(self) -> str:
        return self._standardEquipmentCategoryId
    

    def publishDelete(self):
        from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroupDeleted import StandardEquipmentCategoryGroupDeleted
        DomainPublishedEvents.addEventForPublishing(StandardEquipmentCategoryGroupDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.project.standard_equipment.standard_category.standard_group.StandardEquipmentCategoryGroupUpdated import StandardEquipmentCategoryGroupUpdated
        DomainPublishedEvents.addEventForPublishing(StandardEquipmentCategoryGroupUpdated(old, self))


    def toMap(self) -> dict:
        return {'standard_equipment_category_group_id': self.id(), 'name': self.name(), 'standard_equipment_category_id': self.standardEquipmentCategoryId()}

    def __repr__(self):
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __str__(self) -> str:
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __eq__(self, other):
        if not isinstance(other, StandardEquipmentCategoryGroup):
            raise NotImplementedError(f'other: {other} can not be compared with StandardEquipmentCategoryGroup class')
        return self.id() == other.id() and self.name() == other.name() and self.standardEquipmentCategoryId() == other.standardEquipmentCategoryId()
