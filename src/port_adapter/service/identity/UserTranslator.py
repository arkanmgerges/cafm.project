"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.domain_model.user.User import User


class UserTranslator:
    @classmethod
    def toUserFromIdentityGrpcResponse(cls, response):
        return User(id=response.id, email=response.email, skipValidation=True)