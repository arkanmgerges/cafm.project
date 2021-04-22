"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from src.domain_model.resource.exception.CodeExceptionConstant import (
    CodeExceptionConstant,
)
from src.domain_model.resource.exception.DomainModelException import (
    DomainModelException,
)


class SubcontractorAlreadyExistException(DomainModelException):
    def __init__(self, message: str = ""):
        self.message = f"{message} already exist"
        self.code = CodeExceptionConstant.OBJECT_ALREADY_EXIST.value
        super().__init__(self.message, self.code)
