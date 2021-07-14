"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from copy import copy
from uuid import uuid4

from src.domain_model.common.HasToMap import HasToMap
from src.domain_model.event.DomainPublishedEvents import DomainPublishedEvents
from src.domain_model.organization.OrganizationType import OrganizationType
from src.resource.logging.logger import logger


class OrganizationLocation(HasToMap):
    def __init__(
        self,
        organizationId: str = None,
        buildingId: str = None,
        buildingName: str = None,
        buildingLevelId: str = None,
        buildingLevelName: str = None,
        buildingLevelRoomId: str = None,
        buildingLevelRoomName: str = None,
    ):
        self._organizationId=organizationId
        self._buildingId = buildingId
        self._buildingName = buildingName
        self._buildingLevelId = buildingLevelId
        self._buildingLevelName = buildingLevelName
        self._buildingLevelRoomId = buildingLevelRoomId
        self._buildingLevelRoomName = buildingLevelRoomName


    def organizationId(self) -> str:
        return self._organizationId

    def buildingId(self) -> str:
        return self._buildingId

    def buildingName(self) -> str:
        return self._buildingName

    def buildingLevelId(self) -> str:
        return self._buildingLevelId

    def buildingLevelName(self) -> str:
        return self._buildingLevelName

    def buildingLevelRoomId(self) -> str:
        return self._buildingLevelRoomId

    def buildingLevelRoomName(self) -> str:
        return self._buildingLevelRoomName

    def toMap(self) -> dict:
        return {
            "organization_id": self.organizationId(),
            "building_id": self.buildingId(),
            "building_name": self.buildingName(),
            "building_level_id": self.buildingLevelId(),
            "building_level_name": self.buildingLevelName(),
            "building_level_room_id": self.buildingLevelRoomId(),
            "building_level_room_name": self.buildingLevelRoomName(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __eq__(self, other) -> bool:
        return (
            self.organizationId() == other.organizationId()
            and self.buildingId() == other.buildingId()
            and self.buildingName() == other.buildingName()
            and self.buildingLevelId() == other.buildingLevelId()
            and self.buildingLevelName() == other.buildingLevelName()
            and self.buildingLevelRoomId() == other.buildingLevelRoomId()
            and self.buildingLevelRoomName() == other.buildingLevelRoomName()
        )
