"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4
from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.country.Country import Country


class CountryUpdated(DomainEvent):
    def __init__(self, oldObj: Country, newObj: Country):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.COUNTRY_UPDATED.value)
        self._data = {'old': oldObj.toMap(), 'new': newObj.toMap()}
