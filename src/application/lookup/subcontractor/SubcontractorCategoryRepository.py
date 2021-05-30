"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod

from src.domain_model.subcontractor.category.SubcontractorCategory import SubcontractorCategory


class SubcontractorCategoryRepository(ABC):
    @abstractmethod
    def save(self, obj: SubcontractorCategory):
        """Save subcontractor category

        Args:
            obj (SubcontractorCategory): The subcontractor category that needs to be saved

        """