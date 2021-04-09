"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.resource.logging.logger import logger

from uuid import uuid4

class SubcontractorCategory:
    def __init__(self, id: str = None, name: str = None, skipValidation: bool = False):
        if not skipValidation:
            if name is None or name == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid subcontractor category name: {name}, for subcontractor category id: {id}')

        self._id = str(uuid4()) if id is None else id
        self._name = name



    @classmethod
    def createFrom(cls, id: str = None, name: str = None, publishEvent: bool = False, skipValidation: bool = False):
        from src.domain_model.subcontractor.category.SubcontractorCategoryCreated import SubcontractorCategoryCreated
        obj = SubcontractorCategory(id=id, 
			name=name, skipValidation=skipValidation)

        if publishEvent:
            logger.debug(
                f'[{SubcontractorCategory.createFrom.__qualname__}] - Create subcontractor category with id: {id}')
            DomainPublishedEvents.addEventForPublishing(SubcontractorCategoryCreated(obj))
        return obj

    @classmethod
    def createFromObject(cls, obj: 'SubcontractorCategory', publishEvent: bool = False, generateNewId: bool = False,
                         skipValidation: bool = False):
        logger.debug(f'[{SubcontractorCategory.createFromObject.__qualname__}]')
        id = None if generateNewId else obj.id()
        return cls.createFrom(id=id, 
			name=obj.name(),
                              skipValidation=skipValidation,
                              publishEvent=publishEvent)


    def id(self) -> str:
        return self._id    
    
    def name(self) -> str:
        return self._name
    

    def publishDelete(self):
        from src.domain_model.subcontractor.category.SubcontractorCategoryDeleted import SubcontractorCategoryDeleted
        DomainPublishedEvents.addEventForPublishing(SubcontractorCategoryDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.subcontractor.category.SubcontractorCategoryUpdated import SubcontractorCategoryUpdated
        DomainPublishedEvents.addEventForPublishing(SubcontractorCategoryUpdated(old, self))


    def toMap(self) -> dict:
        return {'subcontractorCategory': self.id(), 'name': self.name()}

    def __repr__(self):
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __str__(self) -> str:
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __eq__(self, other):
        if not isinstance(other, SubcontractorCategory):
            raise NotImplementedError(f'other: {other} can not be compared with SubcontractorCategory class')
        return self.id() == other.id() and self.name() == other.name()
