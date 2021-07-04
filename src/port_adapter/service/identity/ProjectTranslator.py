"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.common.model.ProjectIncludesOrganizationsIncludeUsersIncludeRoles import \
    ProjectIncludesOrganizationsIncludeUsersIncludeRoles
from src.domain_model.project.Project import Project
from src.port_adapter.service.identity.OrganizationTranslator import OrganizationTranslator


class ProjectTranslator:
    @classmethod
    def toProjectFromIdentityGrpcResponse(cls, response):
        return Project(id=response.id, name=response.name, skipValidation=True)

    @classmethod
    def toProjectIncludesOrganizationsIncludeUsersIncludeRolesFromIdentityGrpcResponse(cls, response):
        return ProjectIncludesOrganizationsIncludeUsersIncludeRoles(
            project=cls.toProjectFromIdentityGrpcResponse(response=response),
            organizationsIncludeUsersIncludeRoles=[OrganizationTranslator.toOrganizationIncludesUsersIncludeRolesFromIdentityGrpcResponse(x) for x in response.realms_include_users_include_roles]
        )