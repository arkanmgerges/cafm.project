"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.common.model.UserIncludesRoles import UserIncludesRoles
from src.domain_model.organization.Organization import Organization


class OrganizationIncludesUsersIncludeRoles:
    def __init__(
        self,
        usersIncludeRoles: List[UserIncludesRoles] = None,
        organization: Organization = None,
    ):
        self._usersIncludeRoles: List[UserIncludesRoles] = usersIncludeRoles if usersIncludeRoles is not None else []
        self._organization: Organization = organization

    def addUserIncludesRoles(self, obj: UserIncludesRoles):
        self._usersIncludeRoles.append(obj)

    def usersIncludeRoles(self) -> List[UserIncludesRoles]:
        return self._usersIncludeRoles

    def organization(self) -> Organization:
        return self._organization

    def result(self) -> dict:
        return {
            "users_include_roles": self._usersIncludeRoles,
            "organization": self._organization,
        }

    def toMap(self) -> dict:
        return {
            "users_include_roles": [x.toMap() for x in self.usersIncludeRoles()],
            **self.organization().toMap(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"
