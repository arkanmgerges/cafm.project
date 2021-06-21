from abc import ABC, abstractmethod
from typing import List

from src.domain_model.tag.Tag import Tag
from src.domain_model.token.TokenData import TokenData


class TagRepository(ABC):
    @abstractmethod
    def tagByName(self, name: str, tokenData: TokenData) -> Tag:
        """Get tag by name

        Args:
            name (Tag): The tag name to get
            tokenData (TokenData): Token data used for updating the project state
        """
