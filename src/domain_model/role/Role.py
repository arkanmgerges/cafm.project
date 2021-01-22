"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from copy import copy
from uuid import uuid4

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.resource.logging.logger import logger


class Role:
    def __init__(self, id: str = None, name: str = '', title: str = ''):
        anId = str(uuid4()) if id is None else id
        self._id = anId
        self._name = name
        self._title = title

    @classmethod
    def createFrom(cls, id: str = None, name: str = '', title: str = '',
                   publishEvent: bool = False):
        obj: Role = Role(id=id, name=name, title=title)
        logger.debug(f'[{Role.createFrom.__qualname__}] - data: {obj.toMap()}')
        if publishEvent:
            logger.debug(f'[{Role.createFrom.__qualname__}] - publish RoleCreated event')
            from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
            from src.domain_model.role.RoleCreated import RoleCreated
            DomainPublishedEvents.addEventForPublishing(RoleCreated(obj))
        return obj

    @classmethod
    def createFromObject(cls, obj: 'Role', publishEvent: bool = False, generateNewId: bool = False):
        logger.debug(f'[{Role.createFromObject.__qualname__}]')
        id = None if generateNewId else obj.id()
        return cls.createFrom(id=id, name=obj.name(), title=obj.title(), publishEvent=publishEvent)

    def id(self) -> str:
        return self._id

    def name(self) -> str:
        return self._name

    def title(self) -> str:
        return self._title

    def update(self, data: dict):
        updated = False
        old = copy(self)
        if 'name' in data and data['name'] != self._name and data['name'] is not None:
            updated = True
            self._name = data['name']
        if 'title' in data and data['title'] != self._title and data['title'] is not None:
            updated = True
            self._title = data['title']
        if updated:
            self.publishUpdate(old)

    def publishDelete(self):
        from src.domain_model.role.RoleDeleted import RoleDeleted
        DomainPublishedEvents.addEventForPublishing(RoleDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.role.RoleUpdated import RoleUpdated
        DomainPublishedEvents.addEventForPublishing(RoleUpdated(old, self))

    def toMap(self) -> dict:
        return {"id": self.id(), "name": self.name(), "title": self.title()}

    def __repr__(self):
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __str__(self) -> str:
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __eq__(self, other) -> bool:
        if not isinstance(other, Role):
            raise NotImplementedError(f'other: {other} can not be compared with User class')
        return self.id() == other.id() and self.name() == other.name() and self.title() == other.title()
