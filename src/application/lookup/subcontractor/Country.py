"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.application.lookup.common.model_data.BaseLookupModel import BaseLookupModel
from src.application.lookup.common.model_data.LookupModelAttributeData import LookupModelAttributeData
from src.domain_model.common.HasToMap import HasToMap


class Country(HasToMap, BaseLookupModel):
    __slots__ = ["id", "name"]

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def toMap(self) -> dict:
        return super()._toMap(Country.attributes())

    def _attributeValue(self, classAttribute):
        return super()._attributeValue(classAttribute)

    @classmethod
    def attributes(cls):
        return {
            "id": LookupModelAttributeData(dataType=int, protoDataType=int),
            "name": LookupModelAttributeData(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"
