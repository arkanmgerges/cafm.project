"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.resource.exception.CodeExceptionConstant import (
    CodeExceptionConstant,
)
from src.domain_model.resource.exception.DomainModelException import (
    DomainModelException,
)


class ObjectIdenticalException(DomainModelException):
    def __init__(self, message: str = ""):
        self.message = f"{message} The object is identical"
        self.code = CodeExceptionConstant.OBJECT_IDENTICAL.value
        super().__init__(self.message, self.code)
