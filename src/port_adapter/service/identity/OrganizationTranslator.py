"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.common.model.OrganizationIncludesUsersIncludeRoles import OrganizationIncludesUsersIncludeRoles
from src.domain_model.organization.Organization import Organization
from src.port_adapter.service.identity.UserTranslator import UserTranslator


class OrganizationTranslator:
    @classmethod
    def toOrganizationFromIdentityGrpcResponse(cls, response):
        return Organization(id=response.id, name=response.name, organizationType=response.realm_type, skipValidation=True)

    @classmethod
    def toOrganizationIncludesUsersIncludeRolesFromIdentityGrpcResponse(cls, response):
        return OrganizationIncludesUsersIncludeRoles(
            organization=cls.toOrganizationFromIdentityGrpcResponse(response=response),
            usersIncludeRoles=[UserTranslator.toUserIncludesRolesFromIdentityGrpcResponse(x) for x in response.users_include_roles]
        )