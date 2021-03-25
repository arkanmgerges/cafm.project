"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.resource.logging.logger import logger

from uuid import uuid4

class DailyCheckProcedureOperation:
    def __init__(self, id: str = None, name: str = None, description: str = None, type: str = None, dailyCheckProcedureId: str = None, skipValidation: bool = False):
        self._id = str(uuid4()) if id is None else id
        self._name = name
        self._description = description
        self._type = type
        self._dailyCheckProcedureId = dailyCheckProcedureId

        if not skipValidation:
            if name is None or name == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid daily check procedure operation name: {name}, for daily check procedure operation id: {id}')
            if type is None or type == '' or not self._isType(type):
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid daily check procedure operation type: {type}, for daily check procedure operation id: {id}')
            if dailyCheckProcedureId is None or dailyCheckProcedureId == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid daily check procedure operation daily_check_procedure_id: {dailyCheckProcedureId}, for daily check procedure operation id: {id}')

    @classmethod
    def createFrom(cls, id: str = None, name: str = None, description: str = None, type: str = None, dailyCheckProcedureId: str = None, publishEvent: bool = False, skipValidation: bool = False):
        from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationCreated import DailyCheckProcedureOperationCreated
        obj = DailyCheckProcedureOperation(id=id, name=name, description=description, type=type, dailyCheckProcedureId=dailyCheckProcedureId, skipValidation=skipValidation)

        if publishEvent:
            logger.debug(
                f'[{DailyCheckProcedureOperation.createFrom.__qualname__}] - Create daily check procedure operation with id: {id}')
            DomainPublishedEvents.addEventForPublishing(DailyCheckProcedureOperationCreated(obj))
        return obj

    @classmethod
    def createFromObject(cls, obj: 'DailyCheckProcedureOperation', publishEvent: bool = False, generateNewId: bool = False,
                         skipValidation: bool = False):
        logger.debug(f'[{DailyCheckProcedureOperation.createFromObject.__qualname__}]')
        id = None if generateNewId else obj.id()
        return cls.createFrom(id=id, name=obj.name(), description=obj.description(), type=obj.type(), dailyCheckProcedureId=obj.dailyCheckProcedureId(),
                              skipValidation=skipValidation,
                              publishEvent=publishEvent)


    def id(self) -> str:
        return self._id    
    
    def name(self) -> str:
        return self._name
    
    def description(self) -> str:
        return self._description
    
    def type(self) -> str:
        return self._type
    
    def dailyCheckProcedureId(self) -> str:
        return self._dailyCheckProcedureId

    def _isType(self, type) -> bool:
        from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationType import DailyCheckProcedureOperationType
        return type in DailyCheckProcedureOperationType._value2member_map_

    def publishDelete(self):
        from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationDeleted import DailyCheckProcedureOperationDeleted
        DomainPublishedEvents.addEventForPublishing(DailyCheckProcedureOperationDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperationUpdated import DailyCheckProcedureOperationUpdated
        DomainPublishedEvents.addEventForPublishing(DailyCheckProcedureOperationUpdated(old, self))


    def toMap(self) -> dict:
        return {'daily_check_procedure_operation_id': self.id(), 'name': self.name(), 'description': self.description(), 'type': self.type(), 'daily_check_procedure_id': self.dailyCheckProcedureId()}

    def __repr__(self):
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __str__(self) -> str:
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __eq__(self, other):
        if not isinstance(other, DailyCheckProcedureOperation):
            raise NotImplementedError(f'other: {other} can not be compared with DailyCheckProcedureOperation class')
        return self.id() == other.id() and self.name() == other.name() and self.description() == other.description() and self.type() == other.type() and self.dailyCheckProcedureId() == other.dailyCheckProcedureId()
