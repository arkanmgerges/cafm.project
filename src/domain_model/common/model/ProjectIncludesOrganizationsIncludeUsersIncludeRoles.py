"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.common.model.OrganizationIncludesUsersIncludeRoles import OrganizationIncludesUsersIncludeRoles
from src.domain_model.project.Project import Project


class ProjectIncludesOrganizationsIncludeUsersIncludeRoles:
    def __init__(
        self,
        organizationsIncludeUsersIncludeRoles: List[OrganizationIncludesUsersIncludeRoles] = None,
        project: Project = None,
    ):
        self._organizationsIncludeUsersIncludeRoles: List[OrganizationIncludesUsersIncludeRoles] = organizationsIncludeUsersIncludeRoles if organizationsIncludeUsersIncludeRoles is not None else []
        self._project: Project = project

    def addOrganizationIncludesUsersIncludeRoles(self, obj: OrganizationIncludesUsersIncludeRoles):
        self._organizationsIncludeUsersIncludeRoles.append(obj)

    def organizationsIncludeUsersIncludeRoles(self) -> List[OrganizationIncludesUsersIncludeRoles]:
        return self._organizationsIncludeUsersIncludeRoles

    def project(self) -> Project:
        return self._project

    def result(self) -> dict:
        return {
            "organizations_include_users_include_roles": self._organizationsIncludeUsersIncludeRoles,
            **self._project,
        }

    def toMap(self) -> dict:
        return {
            "organizations_include_users_include_roles": [x.toMap() for x in self.organizationsIncludeUsersIncludeRoles()],
            **self.project().toMap(),
        }

    def __repr__(self):
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"

    def __str__(self) -> str:
        return f"<{self.__module__} object at {hex(id(self))}> {self.toMap()}"
