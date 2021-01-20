"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.organization.Organization import Organization
from src.domain_model.role.Role import Role
from src.domain_model.user.User import User


class UserLookup:
    def __init__(self, user: User = None, roles: List[Role] = None, organizations: List[Organization] = None):
        self._user: User = user
        self._roles: List[Role] = roles if roles is not None else []
        self._organizations: List[Organization] = organizations if organizations is not None else []

    def addOrganization(self, obj: Organization):
        self._organizations.append(obj)

    def addRole(self, obj: Role):
        self._roles.append(obj)

    def addUser(self, obj: User):
        self._user = obj

    def user(self) -> User:
        return self._user

    def roles(self) -> List[Role]:
        return self._roles

    def organizations(self) -> List[Organization]:
        return self._organizations

    def result(self) -> dict:
        return {'user': self._user, 'roles': self._roles, 'organizations': self._organizations}

    def toMap(self) -> dict:
        return {"user": self._user.toMap(), "roles": [x.toMap() for x in self.roles()],
                "organizations": [x.toMap() for x in self.organizations()]}

    def __repr__(self):
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'

    def __str__(self) -> str:
        return f'<{self.__module__} object at {hex(id(self))}> {self.toMap()}'