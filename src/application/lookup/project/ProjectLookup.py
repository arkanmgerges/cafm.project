"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.organization.Organization import Organization
from src.domain_model.project.Project import Project
from src.domain_model.role.Role import Role
from src.domain_model.user.User import User


class ProjectLookup:
    def __init__(
        self,
        project: Project = None,
        users: List[User] = None,
        roles: List[Role] = None,
        organizations: List[Organization] = None,
    ):
        self._project: Project = project
        self._users: List[User] = users if users is not None else []
        self._roles: List[Role] = roles if roles is not None else []
        self._organizations: List[Organization] = (
            organizations if organizations is not None else []
        )

    def addOrganization(self, obj: Organization):
        self._organizations.append(obj)

    def addRole(self, obj: Role):
        self._roles.append(obj)

    def addProject(self, obj: Project):
        self._project = obj

    def addUser(self, obj: User):
        self._users.append(obj)

    def users(self) -> List[User]:
        return self._users

    def roles(self) -> List[Role]:
        return self._roles

    def project(self) -> Project:
        return self._project

    def organizations(self) -> List[Organization]:
        return self._organizations

    def result(self) -> dict:
        return {
            "users": self._users,
            "roles": self._roles,
            "project": self._project,
            "organizations": self._organizations,
        }

    def toMap(self) -> dict:
        return {
            "project": self.project().toMap(),
            "users": [x.toMap() for x in self.users()],
            "roles": [x.toMap() for x in self.roles()],
            "organizations": [x.toMap() for x in self.organizations()],
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"
