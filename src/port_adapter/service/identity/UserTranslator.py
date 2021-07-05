"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.common.model.UserIncludesOrganizationsAndRoles import UserIncludesOrganizationsAndRoles
from src.domain_model.common.model.UserIncludesRoles import UserIncludesRoles
from src.domain_model.role.Role import Role
from src.domain_model.user.User import User



class UserTranslator:
    @classmethod
    def toUserFromIdentityGrpcResponse(cls, response):
        return User(id=response.id, email=response.email, skipValidation=True)

    @classmethod
    def toUserIncludesRolesFromIdentityGrpcResponse(cls, response):
        return UserIncludesRoles(
            user=cls.toUserFromIdentityGrpcResponse(response=response),
            roles=[Role.createFrom(id=x.id, name=x.name, title=x.title, skipValidation=True) for x in response.roles]
        )

    @classmethod
    def toUserIncludesOrganizationsAndRolesFromIdentityGrpcResponse(cls, response):
        from src.port_adapter.service.identity.RoleTranslator import RoleTranslator
        from src.port_adapter.service.identity.OrganizationTranslator import OrganizationTranslator
        return UserIncludesOrganizationsAndRoles(
            user=cls.toUserFromIdentityGrpcResponse(response=response),
            organizations=[OrganizationTranslator.toOrganizationFromIdentityGrpcResponse(x) for x in response.realms],
            roles=[RoleTranslator.toRoleFromIdentityGrpcResponse(x) for x in response.roles]
        )