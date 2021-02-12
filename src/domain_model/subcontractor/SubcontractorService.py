"""
@author: Mohammad S. moso<moso@develoop.run>
"""

from src.domain_model.resource.exception.SubcontractorAlreadyExistException import SubcontractorAlreadyExistException
from src.domain_model.resource.exception.SubcontractorDoesNotExistException import SubcontractorDoesNotExistException
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.subcontractor.SubcontractorRepository import SubcontractorRepository
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class SubcontractorService:
    def __init__(self, subcontractorRepo: SubcontractorRepository):
        self._repo = subcontractorRepo

    @debugLogger
    def createSubcontractor(self, obj: Subcontractor, objectOnly: bool = False, tokenData: TokenData = None):
        try:
            if obj.id() == '':
                raise SubcontractorDoesNotExistException()
            self._repo.subcontractorByName(companyName=obj.companyName())
            raise SubcontractorAlreadyExistException(obj.companyName())
        except SubcontractorDoesNotExistException:
            if objectOnly:
                return Subcontractor.createFromObject(obj=obj, generateNewId=True) if obj.id() == '' else obj
            else:
                obj: Subcontractor = Subcontractor.createFromObject(obj=obj, publishEvent=True)
                return obj
