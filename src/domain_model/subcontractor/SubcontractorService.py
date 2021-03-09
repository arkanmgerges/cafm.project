"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from typing import List

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
        if objectOnly:
            return Subcontractor.createFromObject(obj=obj, generateNewId=True) if obj.id() == '' else obj
        else:
            obj: Subcontractor = Subcontractor.createFromObject(obj=obj, publishEvent=True)
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def updateSubcontractor(self, oldObject: Subcontractor, newObject: Subcontractor, tokenData: TokenData = None):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def deleteSubcontractor(self, obj: Subcontractor, tokenData: TokenData = None):
        obj.publishDelete()
        self._repo.deleteSubcontractor(obj=obj)

    @debugLogger
    def subcontractors(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
                       order: List[dict] = None):
        return self._repo.subcontractors(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
