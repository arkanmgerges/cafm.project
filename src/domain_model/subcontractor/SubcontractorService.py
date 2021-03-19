"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from typing import List

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.organization.Organization import Organization
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
    def assignSubcontractor(self, subcontractor: Subcontractor, organization: Organization,
                            tokenData: TokenData = None):
        from src.domain_model.subcontractor.SubcontractorAssigned import SubcontractorAssigned
        DomainPublishedEvents.addEventForPublishing(
            SubcontractorAssigned(subcontractor=subcontractor, organization=organization))
        self._repo.assignSubcontractoroOrganization(subcontractor=subcontractor, organization=organization,
                                                    tokenData=tokenData)

    @debugLogger
    def revokeSubcontractor(self, subcontractor: Subcontractor, organization: Organization,
                            tokenData: TokenData = None):
        from src.domain_model.subcontractor.SubcontractorRevoked import SubcontractorRevoked
        DomainPublishedEvents.addEventForPublishing(
            SubcontractorRevoked(subcontractor=subcontractor, organization=organization))
        self._repo.revokeRoleToUserAssignment(subcontractor=subcontractor, organization=organization,
                                              tokenData=tokenData)

    @debugLogger
    def subcontractors(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
                       order: List[dict] = None):
        return self._repo.subcontractors(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
