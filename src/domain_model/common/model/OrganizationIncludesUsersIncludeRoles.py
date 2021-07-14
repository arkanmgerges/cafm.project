"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.common.model.UserIncludesRoles import UserIncludesRoles
from src.domain_model.organization.Organization import Organization
from src.domain_model.organization.OrganizationLocation import OrganizationLocation


class OrganizationIncludesUsersIncludeRoles:
    def __init__(
        self,
        usersIncludeRoles: List[UserIncludesRoles] = None,
        organization: Organization = None,
        locations: List[dict] = None
    ):
        self._usersIncludeRoles: List[UserIncludesRoles] = usersIncludeRoles if usersIncludeRoles is not None else []
        self._organization: Organization = organization
        self._locations: List[OrganizationLocation] = locations


    def addUserIncludesRoles(self, obj: UserIncludesRoles):
        self._usersIncludeRoles.append(obj)

    def addLocation(self, obj: OrganizationLocation):
        if self._locations is None:
            self._locations = []
        self._locations.append(obj)

    def usersIncludeRoles(self) -> List[UserIncludesRoles]:
        return self._usersIncludeRoles

    def organization(self) -> Organization:
        return self._organization

    def locations(self) -> List[OrganizationLocation]:
        return self._locations

    def result(self) -> dict:
        return {
            "users_include_roles": self._usersIncludeRoles,
            "organization": self._organization,
            "locations": self._locations,
        }

    def toMap(self) -> dict:
        locations = []
        if self.locations() is not None:
            locations = self.locations()
        return {
            "users_include_roles": [x.toMap() for x in self.usersIncludeRoles()],
            "locations": locations,
            **self.organization().toMap(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"
