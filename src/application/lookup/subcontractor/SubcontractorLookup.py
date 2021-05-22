"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.application.lookup.city.CityLookup import CityLookup
from src.application.lookup.country.CountryLookup import CountryLookup
from src.application.lookup.model_data.BaseLookupModel import BaseLookupModel
from src.application.lookup.model_data.LookupModelAttributeData import LookupModelAttributeData
from src.application.lookup.state.StateLookup import StateLookup
from src.application.lookup.subcontractor.category.SubcontractorCategoryLookup import SubcontractorCategoryLookup
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
            "company_name": LookupModelAttributeData(),
            "website_url": LookupModelAttributeData(),
            "contact_person": LookupModelAttributeData(),
            "email": LookupModelAttributeData(),
            "phone_number": LookupModelAttributeData(),
            "address_one": LookupModelAttributeData(),
            "address_two": LookupModelAttributeData(),
            "subcontractor_category": LookupModelAttributeData(
                dataType=SubcontractorCategoryLookup, isLookupClass=True
            ),
            "description": LookupModelAttributeData(),
            "postal_code": LookupModelAttributeData(),
            "country": LookupModelAttributeData(dataType=CountryLookup, isLookupClass=True),
            "city": LookupModelAttributeData(dataType=CityLookup, isLookupClass=True),
            "state": LookupModelAttributeData(dataType=StateLookup, isLookupClass=True),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"
