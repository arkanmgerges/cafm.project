"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureFrequency import MaintenanceProcedureFrequency
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureHardSubType import \
    MaintenanceProcedureHardSubType
from src.domain_model.project.maintenance.procedure.MaintenanceProcedureType import MaintenanceProcedureType
from src.resource.logging.logger import logger

from uuid import uuid4

class StandardMaintenanceProcedure:
    def __init__(self, id: str = None, name: str = None, type: str = None, subtype: str = None, frequency: str = None, startDate: int = None, organizationId: str = None, skipValidation: bool = False):
        subtypeList = list(subtype)
        if not skipValidation:
            if name is None or name == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid standard maintenance procedure name: {name}, for standard maintenance procedure id: {id}')
            if type is None or type == '' or not self._isType(type):
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid standard maintenance procedure type: {type}, for standard maintenance procedure id: {id}')
            if not self._isSubtype(type, subtypeList):
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid standard maintenance procedure subtype: {subtype}, for standard maintenance procedure id: {id}, '
                    f'only these types are supported: ' + ', '.join([e.value for e in MaintenanceProcedureHardSubType]) +
                    ' when type is set as hard')
            if frequency is None or frequency == '' or not self._isFrequency(frequency):
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
        self._subtype = "".join(subtypeList)
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

    def _isType(self, type) -> bool:
        return type in MaintenanceProcedureType._value2member_map_

    def _isSubtype(self, type, subtypeList) -> bool:
        if type != MaintenanceProcedureType.HARD.value:
            subtypeList.clear()
            return True

        subtype = "".join(subtypeList)
        return subtype in MaintenanceProcedureHardSubType._value2member_map_

    def _isFrequency(self, frequency: str) -> bool:
        return frequency in MaintenanceProcedureFrequency._value2member_map_

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
