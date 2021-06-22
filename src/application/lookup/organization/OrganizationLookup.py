"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.organization.Organization import Organization
from src.domain_model.project.Project import Project
from src.domain_model.role.Role import Role
from src.domain_model.user.User import User


class OrganizationLookup:
    def __init__(
        self,
        projects: List[Project] = None,
        users: List[User] = None,
        roles: List[Role] = None,
        organization: Organization = None,
    ):
        self._projects: List[Project] = projects if projects is not None else []
        self._users: List[User] = users if users is not None else []
        self._roles: List[Role] = roles if roles is not None else []
        self._organization: Organization = organization

    def addOrganization(self, obj: Organization):
        self._organization = obj

    def addRole(self, obj: Role):
        self._roles.append(obj)

    def addProject(self, obj: Project):
        self._projects.append(obj)

    def addUser(self, obj: User):
        self._users.append(obj)

    def users(self) -> List[User]:
        return self._users

    def roles(self) -> List[Role]:
        return self._roles

    def projects(self) -> List[Project]:
        return self._projects

    def organization(self) -> Organization:
        return self._organization

    def result(self) -> dict:
        return {
            "users": self._users,
            "roles": self._roles,
            "projects": self._projects,
            "organization": self._organization,
        }

    def toMap(self) -> dict:
        return {
            "projects": [x.toMap() for x in self.projects()],
            "users": [x.toMap() for x in self.users()],
            "roles": [x.toMap() for x in self.roles()],
            "organization": self.organization().toMap(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"
