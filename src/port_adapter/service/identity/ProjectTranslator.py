"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.project.Project import Project


class ProjectTranslator:
    @classmethod
    def toProjectFromIdentityGrpcResponse(cls, response):
        return Project(id=response.id, name=response.name, skipValidation=True)