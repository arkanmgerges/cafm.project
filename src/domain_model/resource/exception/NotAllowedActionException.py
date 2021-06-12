"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.resource.exception.CodeExceptionConstant import (
    CodeExceptionConstant,
)
from src.domain_model.resource.exception.DomainModelException import (
    DomainModelException,
)


class NotAllowedActionException(DomainModelException):
    def __init__(self, message: str = ""):
        self.message = f"{message}, not allowed action"
        self.code = CodeExceptionConstant.NOT_ALLOWED_ACTION.value
        super().__init__(self.message, self.code)
