"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.organization.Organization import Organization


class OrganizationTranslator:
    @classmethod
    def toOrganizationFromIdentityGrpcResponse(cls, response):
        return Organization(id=response.id, name=response.name, organizationType=response.realm_type, skipValidation=True)