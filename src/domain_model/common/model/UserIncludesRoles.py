"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.role.Role import Role
from src.domain_model.user.User import User


class UserIncludesRoles:
    def __init__(
        self,
        user: User = None,
        roles: List[Role] = None,
    ):
        self._user: User = user
        self._roles: List[Role] = roles if roles is not None else []

    def addRole(self, obj: Role):
        self._roles.append(obj)

    def user(self) -> User:
        return self._user

    def roles(self) -> List[Role]:
        return self._roles

    def result(self) -> dict:
        return {
            "user": self._user,
            "roles": self._roles,
        }

    def toMap(self) -> dict:
        return {
            "roles": [x.toMap() for x in self.roles()],
            **self.user().toMap(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"
