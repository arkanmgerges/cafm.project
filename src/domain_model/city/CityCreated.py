"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4
from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.city.City import City


class CityCreated(DomainEvent):
    def __init__(self, obj: City):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.CITY_CREATED.value)
        self._data = obj.toMap()
