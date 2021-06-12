"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.port_adapter.repository.resource.exception.RepositoryCodeExceptionConstant import \
    RepositoryCodeExceptionConstant


class RepositoryException(Exception):
    def __init__(
        self, message: str, code: int = RepositoryCodeExceptionConstant.REPOSITORY_EXCEPTION.value,
            extra: List[dict] = None,
    ):
        self.message = f"repository exception: {message}"
        self.extra = extra
        self.code = code
        super().__init__(self.message)
