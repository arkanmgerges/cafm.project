"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod

from src.domain_model.subcontractor.Subcontractor import Subcontractor


class SubcontractorLookupRepository(ABC):
    @abstractmethod
    def save(self, obj: Subcontractor):
        """Save subcontractor

        Args:
            obj (Subcontractor): The subcontractor that needs to be saved

        """