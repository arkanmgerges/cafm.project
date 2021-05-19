"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.common.HasToMap import HasToMap
from src.domain_model.organization.Organization import Organization
from src.domain_model.role.Role import Role
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.subcontractor.category.SubcontractorCategory import SubcontractorCategory
from src.domain_model.user.User import User
from src.resource.common.Util import Util


class SubcontractorLookup(HasToMap):
    def __init__(
        self,
        **kwargs
    ):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def toMap(self) -> dict:
        classAttributes = SubcontractorLookup.attributes()
        result = {}
        for classAttribute in classAttributes:
            result[Util.camelCaseToLowerSnakeCase(classAttribute)] = getattr(self, classAttribute, None)
        return result

    @classmethod
    def attributes(cls):
        return [
            "id",
            "companyName",
            "websiteUrl",
            "contactPerson",
            "email",
            "phoneNumber",
            "addressOne",
            "addressTwo",
            "subcontractorCategoryId",
            "subcontractorCategoryName",
            "description",
            "postalCode",
            "countryId",
            "countryName",
            "cityId",
            "cityName",
            "stateId",
            "stateName",]

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"
