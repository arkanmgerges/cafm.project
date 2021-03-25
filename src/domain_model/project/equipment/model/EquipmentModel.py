"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.resource.logging.logger import logger

"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4


class EquipmentModel:
    def __init__(self, id: str = None, name: str = None, skipValidation: bool = False):
        self._id = str(uuid4()) if id is None else id
        self._name = name

        if not skipValidation:
            if name is None or name == '':
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException
                raise InvalidArgumentException(
                    f'Invalid equipment model name: {name}, for equipment model id: {id}')

    @classmethod
    def createFrom(cls, id: str = None, name: str = '', publishEvent: bool = False, skipValidation: bool = False):
        from src.domain_model.project.equipment.model.EquipmentModelCreated import EquipmentModelCreated
        obj = EquipmentModel(id=id, name=name, skipValidation=skipValidation)

        if publishEvent:
            logger.debug(
                f'[{EquipmentModel.createFrom.__qualname__}] - Create equipment model with id: {id}')
            DomainPublishedEvents.addEventForPublishing(EquipmentModelCreated(obj))
        return obj

    @classmethod
    def createFromObject(cls, obj: 'EquipmentModel', publishEvent: bool = False, generateNewId: bool = False,
                         skipValidation: bool = False):
        logger.debug(f'[{EquipmentModel.createFromObject.__qualname__}]')
        id = None if generateNewId else obj.id()
        return cls.createFrom(id=id, name=obj.name(),
                              skipValidation=skipValidation,
                              publishEvent=publishEvent)

    def id(self) -> str:
        return self._id

    def name(self) -> str:
        return self._name

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
        from src.domain_model.project.equipment.model.EquipmentModelDeleted import EquipmentModelDeleted
        DomainPublishedEvents.addEventForPublishing(EquipmentModelDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.project.equipment.model.EquipmentModelUpdated import EquipmentModelUpdated
        DomainPublishedEvents.addEventForPublishing(EquipmentModelUpdated(old, self))

    def toMap(self) -> dict:
        return {'equipment_model_id': self.id(), 'name': self.name()}

    def __repr__(self):
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __str__(self) -> str:
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __eq__(self, other):
        if not isinstance(other, EquipmentModel):
            raise NotImplementedError(f'other: {other} can not be compared with EquipmentModel class')
        return self.id() == other.id() and self.name() == other.name()
