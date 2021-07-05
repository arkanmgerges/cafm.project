"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.application.lookup.subcontractor.City import City
from src.application.lookup.subcontractor.Country import Country
from src.application.lookup.common.model_data.BaseLookupModel import BaseLookupModel
from src.application.lookup.common.model_data.LookupModelAttributeData import (
    LookupModelAttributeData,
)
from src.application.lookup.subcontractor.State import State
from src.application.lookup.subcontractor.SubcontractorCategory import (
    SubcontractorCategory,
)
from src.domain_model.common.HasToMap import HasToMap


class SubcontractorLookup(HasToMap, BaseLookupModel):
    __slots__ = [
        "id",
        "companyName",
        "websiteUrl",
        "contactPerson",
        "email",
        "phoneNumber",
        "addressOne",
        "addressTwo",
        "subcontractorCategory",
        "postalCode",
        "country",
        "city",
        "state",
    ]

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def toMap(self) -> dict:
        return super()._toMap(SubcontractorLookup.attributes())

    def _attributeValue(self, classAttribute):
        return super()._attributeValue(classAttribute)

    @classmethod
    def attributes(cls):
        return {
            "id": LookupModelAttributeData(),
            "companyName": LookupModelAttributeData(),
            "websiteUrl": LookupModelAttributeData(),
            "contactPerson": LookupModelAttributeData(),
            "email": LookupModelAttributeData(),
            "phoneNumber": LookupModelAttributeData(),
            "addressOne": LookupModelAttributeData(),
            "addressTwo": LookupModelAttributeData(),
            "subcontractorCategory": LookupModelAttributeData(
                dataType=SubcontractorCategory, isClass=True
            ),
            "description": LookupModelAttributeData(),
            "postalCode": LookupModelAttributeData(),
            "country": LookupModelAttributeData(dataType=Country, isClass=True),
            "city": LookupModelAttributeData(dataType=City, isClass=True),
            "state": LookupModelAttributeData(dataType=State, isClass=True),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"
