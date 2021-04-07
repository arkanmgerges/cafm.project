"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.resource.logging.logger import logger

from uuid import uuid4

class StandardMaintenanceProcedure:
    def __init__(self, id: str = None, name: str = None, type: str = None, subtype: str = None, frequency: str = None, startDate: int = None, organizationId: str = None, skipValidation: bool = False):
        if not skipValidation:
            if name is None or name == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid standard maintenance procedure name: {name}, for standard maintenance procedure id: {id}')
            if type is None or type == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid standard maintenance procedure type: {type}, for standard maintenance procedure id: {id}')
            if subtype is None or subtype == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid standard maintenance procedure subtype: {subtype}, for standard maintenance procedure id: {id}')
            if frequency is None or frequency == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid standard maintenance procedure frequency: {frequency}, for standard maintenance procedure id: {id}')
            if organizationId is None or organizationId == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid standard maintenance procedure organization_id: {organizationId}, for standard maintenance procedure id: {id}')

        self._id = str(uuid4()) if id is None else id
        self._name = name
        self._type = type
        self._subtype = subtype
        self._frequency = frequency
        self._startDate = startDate
        self._organizationId = organizationId



    @classmethod
    def createFrom(cls, id: str = None, name: str = None, type: str = None, subtype: str = None, frequency: str = None, startDate: int = None, organizationId: str = None, publishEvent: bool = False, skipValidation: bool = False):
        from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedureCreated import StandardMaintenanceProcedureCreated
        obj = StandardMaintenanceProcedure(id=id, 
			name=name,
			type=type,
			subtype=subtype,
			frequency=frequency,
			startDate=startDate,
			organizationId=organizationId, skipValidation=skipValidation)

        if publishEvent:
            logger.debug(
                f'[{StandardMaintenanceProcedure.createFrom.__qualname__}] - Create standard maintenance procedure with id: {id}')
            DomainPublishedEvents.addEventForPublishing(StandardMaintenanceProcedureCreated(obj))
        return obj

    @classmethod
    def createFromObject(cls, obj: 'StandardMaintenanceProcedure', publishEvent: bool = False, generateNewId: bool = False,
                         skipValidation: bool = False):
        logger.debug(f'[{StandardMaintenanceProcedure.createFromObject.__qualname__}]')
        id = None if generateNewId else obj.id()
        return cls.createFrom(id=id, 
            name=obj.name(),
            type=obj.type(),
            subtype=obj.subtype(),
            frequency=obj.frequency(),
            startDate=obj.startDate(),
            organizationId=obj.organizationId(),
            skipValidation=skipValidation,
            publishEvent=publishEvent)


    def id(self) -> str:
        return self._id    
    
    def name(self) -> str:
        return self._name
    
    def type(self) -> str:
        return self._type
    
    def subtype(self) -> str:
        return self._subtype
    
    def frequency(self) -> str:
        return self._frequency
    
    def startDate(self) -> int:
        return self._startDate
    
    def organizationId(self) -> str:
        return self._organizationId
    

    def publishDelete(self):
        from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedureDeleted import StandardMaintenanceProcedureDeleted
        DomainPublishedEvents.addEventForPublishing(StandardMaintenanceProcedureDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedureUpdated import StandardMaintenanceProcedureUpdated
        DomainPublishedEvents.addEventForPublishing(StandardMaintenanceProcedureUpdated(old, self))


    def toMap(self) -> dict:
        return {'standard_maintenance_procedure_id': self.id(), 'name': self.name(), 'type': self.type(), 'subtype': self.subtype(), 'frequency': self.frequency(), 'start_date': self.startDate(), 'organization_id': self.organizationId()}

    def __repr__(self):
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __str__(self) -> str:
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __eq__(self, other):
        if not isinstance(other, StandardMaintenanceProcedure):
            raise NotImplementedError(f'other: {other} can not be compared with StandardMaintenanceProcedure class')
        return self.id() == other.id() and self.name() == other.name() and self.type() == other.type() and self.subtype() == other.subtype() and self.frequency() == other.frequency() and self.startDate() == other.startDate() and self.organizationId() == other.organizationId()
