"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List, Tuple

from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.organization.Organization import Organization
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.subcontractor.SubcontractorRepository import (
    SubcontractorRepository,
)
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class SubcontractorService:
    def __init__(self, repository: SubcontractorRepository):
        self._repo = repository

    @debugLogger
    def createSubcontractor(
        self, obj: Subcontractor, objectOnly: bool = False, tokenData: TokenData = None
    ):
        if objectOnly:
            return (
                Subcontractor.createFromObject(obj=obj, generateNewId=True)
                if obj.id() == ""
                else obj
            )
        else:
            obj: Subcontractor = Subcontractor.createFromObject(
                obj=obj, publishEvent=True
            )
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def deleteSubcontractor(self, obj: Subcontractor, tokenData: TokenData = None):
        obj.publishDelete()
        self._repo.deleteSubcontractor(obj=obj)

    @debugLogger
    def updateSubcontractor(
        self,
        oldObject: Subcontractor,
        newObject: Subcontractor,
        tokenData: TokenData = None,
    ):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def bulkCreate(self, objList: List[Subcontractor]):
        self._repo.bulkSave(objList=objList)
        for obj in objList:
            Subcontractor.createFromObject(obj=obj, publishEvent=True)

    @debugLogger
    def bulkDelete(self, objList: List[Subcontractor]):
        self._repo.bulkDelete(objList=objList)
        for obj in objList:
            obj.publishDelete()

    @debugLogger
    def bulkUpdate(self, objList: List[Tuple]):
        newObjList = list(map(lambda x: x[0], objList))
        self._repo.bulkSave(objList=newObjList)
        for obj in objList:
            newObj = obj[0]
            oldObj = obj[1]
            newObj.publishUpdate(oldObj)

    @debugLogger
    def subcontractors(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.subcontractors(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def subcontractorsBySubcontractorCategoryId(
        self,
        subcontractorCategoryId: str = None,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.subcontractorsBySubcontractorCategoryId(
            tokenData=tokenData,
            subcontractorCategoryId=subcontractorCategoryId,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def assignSubcontractor(
        self,
        subcontractor: Subcontractor,
        organization: Organization,
        tokenData: TokenData = None,
    ):
        from src.domain_model.subcontractor.SubcontractorAssigned import (
            SubcontractorAssigned,
        )

        DomainPublishedEvents.addEventForPublishing(
            SubcontractorAssigned(
                subcontractor=subcontractor, organization=organization
            )
        )
        self._repo.assignSubcontractorToOrganization(
            subcontractor=subcontractor, organization=organization, tokenData=tokenData
        )

    @debugLogger
    def revokeSubcontractor(
        self,
        subcontractor: Subcontractor,
        organization: Organization,
        tokenData: TokenData = None,
    ):
        from src.domain_model.subcontractor.SubcontractorRevoked import (
            SubcontractorRevoked,
        )

        DomainPublishedEvents.addEventForPublishing(
            SubcontractorRevoked(subcontractor=subcontractor, organization=organization)
        )
        self._repo.revokeRoleToUserAssignment(
            subcontractor=subcontractor, organization=organization, tokenData=tokenData
        )

    @debugLogger
    def subcontractorsByOrganizationId(
        self,
        organizationId: str,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        return self._repo.subcontractorsByOrganizationId(
            organizationId=organizationId,
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )
