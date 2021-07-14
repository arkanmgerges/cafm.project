"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import abstractmethod, ABC
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.Building import Building
from typing import List, Tuple

from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationRepository import OrganizationRepository
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class OrganizationService(ABC):
    @debugLogger
    def createOrganization(
        self, obj: Organization, objectOnly: bool = False, tokenData: TokenData = None
    ):
        if objectOnly:
            return (
                Organization.createFromObject(obj=obj, generateNewId=True)
                if obj.id() == ""
                else obj
            )
        else:
            obj: Organization = Organization.createFromObject(
                obj=obj, publishEvent=True
            )
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def deleteOrganization(self, obj: Organization, tokenData: TokenData = None):
        obj.publishDelete()
        self._repo.deleteOrganization(obj=obj)

    @debugLogger
    def updateOrganization(
        self,
        oldObject: Organization,
        newObject: Organization,
        tokenData: TokenData = None,
    ):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def bulkCreate(self, objList: List[Organization]):
        self._repo.bulkSave(objList=objList)
        for obj in objList:
            Organization.createFromObject(obj=obj, publishEvent=True)

    @debugLogger
    def bulkDelete(self, objList: List[Organization]):
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
    @abstractmethod
    def organizations(
        self,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        pass

    @debugLogger
    def organizationsByType(
        self,
        tokenData: TokenData = None,
        type: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        pass

    def organizationsIncludeUsersIncludeRoles(self,
                                              tokenData: TokenData = None,
                                              type: str = None,
                                              resultFrom: int = 0,
                                              resultSize: int = 100,
                                              order: List[dict] = None,
                                              filter: List[dict] = None,) -> dict:
        pass

    @debugLogger
    def linkOrganizationToBuilding(self,  organization: Organization,
                                 building: Building,
                                 buildingLevel: BuildingLevel,
                                 buildingLevelRoom: BuildingLevelRoom, tokenData: TokenData):

        from src.domain_model.organization.BuildingToOrganizationLinked import \
            BuildingToOrganizationLinked
        DomainPublishedEvents.addEventForPublishing(
            BuildingToOrganizationLinked(organizationId=organization.id,buildingId=building.id,buildingLevelId=buildingLevel.id, buildingLevelRoomId=buildingLevelRoom.id))
        self._repo.linkOrganizationToBuilding(
            organization=organization, building=building, buildingLevel=buildingLevel, buildingLevelRoom=buildingLevelRoom, tokenData=tokenData)

    @debugLogger
    def unlinkOrganizationToBuilding(self,  organization: Organization,
                                 building: Building,
                                 buildingLevel: BuildingLevel,
                                 buildingLevelRoom: BuildingLevelRoom, tokenData: TokenData):
        from src.domain_model.organization.BuildingToOrganizationUnlinked import \
            BuildingToOrganizationUnlinked
        DomainPublishedEvents.addEventForPublishing(
            BuildingToOrganizationUnlinked(organizationId=organization.id,buildingId=building.id,buildingLevelId=buildingLevel.id, buildingLevelRoomId=buildingLevelRoom.id))
        self._repo.unlinkOrganizationToBuilding(
            organization=organization, building=building, buildingLevel=buildingLevel, buildingLevelRoom=buildingLevelRoom, tokenData=tokenData)

