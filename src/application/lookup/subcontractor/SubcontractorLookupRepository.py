"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.application.user_lookup.UserLookup import UserLookup
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.token.TokenData import TokenData


class SubcontractorLookupRepository(ABC):
    @abstractmethod
    def saveBySource(self, source: Subcontractor):
        """Save the target based on the source

        Args:
            source (Subcontractor): Source to save the target

        """
