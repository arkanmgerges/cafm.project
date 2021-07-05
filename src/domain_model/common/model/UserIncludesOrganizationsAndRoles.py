"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.organization.Organization import Organization
from src.domain_model.role.Role import Role
from src.domain_model.user.User import User


class UserIncludesOrganizationsAndRoles:
    def __init__(
        self,
        user: User = None,
        organizations: List[Organization] = None,
        roles: List[Role] = None,
    ):
        self._user: User = user
        self._organizations: List[Organization] = organizations if organizations is not None else []
        self._roles: List[Role] = roles if roles is not None else []

    def addRole(self, obj: Role):
        self._roles.append(obj)

    def addOrganization(self, obj: Organization):
        self._organizations.append(obj)

    def user(self) -> User:
        return self._user

    def roles(self) -> List[Role]:
        return self._roles

    def organizations(self) -> List[Organization]:
        return self._organizations

    def result(self) -> dict:
        return {
            "user": self._user,
            "organizations": self._organizations,
            "roles": self._roles,
        }

    def toMap(self) -> dict:
        return {
            **self.user().toMap(),
            "organizations": [x.toMap() for x in self.organizations()],
            "roles": [x.toMap() for x in self.roles()],
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"
