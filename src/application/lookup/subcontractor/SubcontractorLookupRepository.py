"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain_model.subcontractor.Subcontractor import Subcontractor


class SubcontractorLookupRepository(ABC):
    @abstractmethod
    def save(self, obj: Subcontractor):
        """Save subcontractor

        Args:
            obj (Subcontractor): The subcontractor that needs to be saved

        """

    @abstractmethod
    def delete(self, obj: Subcontractor):
        """delete subcontractor

        Args:
            obj (Subcontractor): The subcontractor that needs to be deleted

        """

    @abstractmethod
    def lookup(self, resultFrom: int, resultSize: int, orders: List[dict], filters: List[dict]):
        """lookup data

        Args:
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            orders (List[dict]): A list of order e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'age', 'direction': 'desc'}]
            filters (List[dict]): A list of 'key', 'value' to pass the requested filters
        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """