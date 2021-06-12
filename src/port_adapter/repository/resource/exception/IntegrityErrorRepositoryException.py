"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from src.port_adapter.repository.resource.exception.RepositoryCodeExceptionConstant import \
    RepositoryCodeExceptionConstant
from src.port_adapter.repository.resource.exception.RepositoryException import RepositoryException


class IntegrityErrorRepositoryException(RepositoryException):
    def __init__(self, message: str = ""):
        self.message = f"{message}"
        self.code = RepositoryCodeExceptionConstant.DB_INTEGRITY_ERROR_EXCEPTION.value
        super().__init__(message=self.message, code=self.code)
