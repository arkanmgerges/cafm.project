"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.application.lookup.common.model_data.BaseLookupModel import BaseLookupModel
from src.application.lookup.common.model_data.LookupModelAttributeData import LookupModelAttributeData
from src.domain_model.common.HasToMap import HasToMap


class SubcontractorCategory(HasToMap, BaseLookupModel):
    def __init__(self, id: str = None, name: str = None):
        self.id = id
        self.name = name

    def toMap(self) -> dict:
        return super()._toMap(SubcontractorCategory.attributes())

    def _attributeValue(self, classAttribute):
        return super()._attributeValue(classAttribute)

    @classmethod
    def attributes(cls):
        return {
            "id": LookupModelAttributeData(),
            "name": LookupModelAttributeData(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"
