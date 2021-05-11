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


class SubcontractorLookup(HasToMap):
    def __init__(
        self,
        subcontractor: Subcontractor = None,
        subcontractorCategory: SubcontractorCategory = None,
    ):
        self._subcontractor: Subcontractor = subcontractor
        self._subcontractorCategory: SubcontractorCategory = subcontractorCategory

    def subcontractor(self) -> Subcontractor:
        return self._subcontractor

    def subcontractorCategory(self) -> SubcontractorCategory:
        return self._subcontractorCategory

    def result(self) -> dict:
        return self.toMap()

    def toMap(self) -> dict:
        return {
            "subcontractor": self._subcontractor.toMap(),
            "subcontractor_category": self._subcontractorCategory.toMap(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"
