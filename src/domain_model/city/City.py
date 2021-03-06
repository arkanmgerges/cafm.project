"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.common.HasToMap import HasToMap
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.resource.logging.logger import logger


class City(HasToMap):
    def __init__(self, id: int = None, name: str = None, skipValidation: bool = False):
        if not skipValidation:
            if name is None or name == "":
                from src.domain_model.resource.exception.InvalidArgumentException import InvalidArgumentException

                raise InvalidArgumentException(f"Invalid city name: {name}, for city id: {id}")

        self._id = id
        self._name = name

    @classmethod
    def createFrom(
        cls,
        id: int = None,
        name: str = None,
        publishEvent: bool = False,
        skipValidation: bool = False,
        **_kwargs,
    ):
        from src.domain_model.city.CityCreated import CityCreated

        obj = City(id=id, name=name, skipValidation=skipValidation)
        logger.debug(f"[{City.createFrom.__qualname__}] - data: {obj.toMap()} event: {publishEvent}")
        if publishEvent:
            logger.debug(f"[{City.createFrom.__qualname__}] - Create city with id: {id}")
            DomainPublishedEvents.addEventForPublishing(CityCreated(obj))
        return obj

    @classmethod
    def createFromObject(
        cls, obj: "City", publishEvent: bool = False, generateNewId: bool = False, skipValidation: bool = False
    ):
        logger.debug(f"[{City.createFromObject.__qualname__}]")
        id = None if generateNewId else obj.id()
        return cls.createFrom(id=id, name=obj.name(), skipValidation=skipValidation, publishEvent=publishEvent)

    def id(self) -> int:
        return self._id

    def name(self) -> str:
        return self._name

    def publishDelete(self):
        from src.domain_model.city.CityDeleted import CityDeleted

        DomainPublishedEvents.addEventForPublishing(CityDeleted(self))

    def publishUpdate(self, old):
        from src.domain_model.city.CityUpdated import CityUpdated

        DomainPublishedEvents.addEventForPublishing(CityUpdated(old, self))

    def toMap(self) -> dict:
        return {"city_id": self.id(), "name": self.name()}

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __eq__(self, other):
        if not isinstance(other, City):
            raise NotImplementedError(f"other: {other} can not be compared with City class")
        return self.id() == other.id() and self.name() == other.name()
