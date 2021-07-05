"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.role.Role import Role


class RoleTranslator:
    @classmethod
    def toRoleFromIdentityGrpcResponse(cls, response):
        return Role(id=response.id, name=response.name, title=response.title, skipValidation=True)