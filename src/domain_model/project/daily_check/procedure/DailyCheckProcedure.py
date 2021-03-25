"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.resource.logging.logger import logger

from uuid import uuid4

class DailyCheckProcedure:
    def __init__(self, id: str = None, name: str = None, description: str = None, equipmentId: str = None, equipmentCategoryGroupId: str = None, skipValidation: bool = False):
        self._id = str(uuid4()) if id is None else id
        self._name = name
        self._description = description
        self._equipmentId = equipmentId
        self._equipmentCategoryGroupId = equipmentCategoryGroupId

        if not skipValidation:
            if name is None or name == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid daily check procedure name: {name}, for daily check procedure id: {id}')

    @classmethod
    def createFrom(cls, id: str = None, name: str = None, description: str = None, equipmentId: str = None, equipmentCategoryGroupId: str = None, publishEvent: bool = False, skipValidation: bool = False):
        from src.domain_model.project.daily_check.procedure.DailyCheckProcedureCreated import DailyCheckProcedureCreated
        obj = DailyCheckProcedure(id=id, name=name, description=description, equipmentId=equipmentId, equipmentCategoryGroupId=equipmentCategoryGroupId, skipValidation=skipValidation)

        if publishEvent:
            logger.debug(
                f'[{DailyCheckProcedure.createFrom.__qualname__}] - Create daily check procedure with id: {id}')
            DomainPublishedEvents.addEventForPublishing(DailyCheckProcedureCreated(obj))
        return obj

    @classmethod
    def createFromObject(cls, obj: 'DailyCheckProcedure', publishEvent: bool = False, generateNewId: bool = False,
                         skipValidation: bool = False):
        logger.debug(f'[{DailyCheckProcedure.createFromObject.__qualname__}]')
        id = None if generateNewId else obj.id()
        return cls.createFrom(id=id, name=obj.name(), description=obj.description(), equipmentId=obj.equipmentId(), equipmentCategoryGroupId=obj.equipmentCategoryGroupId(),
                              skipValidation=skipValidation,
                              publishEvent=publishEvent)


    def id(self) -> str:
        return self._id    
    
    def name(self) -> str:
        return self._name
    
    def description(self) -> str:
        return self._description
    
    def equipmentId(self) -> str:
        return self._equipmentId
    
    def equipmentCategoryGroupId(self) -> str:
        return self._equipmentCategoryGroupId
    

    def publishDelete(self):
        from src.domain_model.project.daily_check.procedure.DailyCheckProcedureDeleted import DailyCheckProcedureDeleted
        DomainPublishedEvents.addEventForPublishing(DailyCheckProcedureDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.project.daily_check.procedure.DailyCheckProcedureUpdated import DailyCheckProcedureUpdated
        DomainPublishedEvents.addEventForPublishing(DailyCheckProcedureUpdated(old, self))


    def toMap(self) -> dict:
        return {'daily_check_procedure_id': self.id(), 'name': self.name(), 'description': self.description(), 'equipment_id': self.equipmentId(), 'equipment_category_group_id': self.equipmentCategoryGroupId()}

    def __repr__(self):
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __str__(self) -> str:
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __eq__(self, other):
        if not isinstance(other, DailyCheckProcedure):
            raise NotImplementedError(f'other: {other} can not be compared with DailyCheckProcedure class')
        return self.id() == other.id() and self.name() == other.name() and self.description() == other.description() and self.equipmentId() == other.equipmentId() and self.equipmentCategoryGroupId() == other.equipmentCategoryGroupId()
