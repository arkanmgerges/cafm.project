"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import abstractmethod, ABC
from typing import List

from src.domain_model.token.TokenData import TokenData

class OrganizationLookupRepository(ABC):
    @abstractmethod
    def lookup(
        self,
        tokenData: TokenData,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        filter: List[dict] = None
    ) -> dict:
        """Get list of project lookups

        Args:
            tokenData (TokenData): A token data object
            resultFrom (int): The start offset of the result item
            resultSize (int): The size of the items in the result
            order (List[dict]): A list of orders e.g. [{'orderBy': 'name', 'direction': 'asc'},
                                {'orderBy': 'age', 'direction': 'desc'}]
            filter (List[dict]): A list of filters e.g. [{'user.name': 'John', 'user.age': '38'},]

        Returns:
            dict: A dict that has {"items": [], "totalItemCount": 0}
        """
