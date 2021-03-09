"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.resource.exception.RoleAlreadyExistException import RoleAlreadyExistException
from src.domain_model.resource.exception.RoleDoesNotExistException import RoleDoesNotExistException
from src.domain_model.role.Role import Role
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class RoleService:
    def __init__(self, roleRepo: RoleRepository):
        self._repo = roleRepo

    @debugLogger
    def createRole(self, obj: Role, objectOnly: bool = False, tokenData: TokenData = None):
        if objectOnly:
            return Role.createFromObject(obj=obj, generateNewId=True) if obj.id() == '' else obj
        else:
            obj: Role = Role.createFromObject(obj=obj, publishEvent=True)
            self._repo.save(obj=obj)
            return obj

    @debugLogger
    def deleteRole(self, obj: Role, tokenData: TokenData = None):
        obj.publishDelete()
        self._repo.deleteRole(obj=obj)

    @debugLogger
    def updateRole(self, oldObject: Role, newObject: Role, tokenData: TokenData = None):
        newObject.publishUpdate(oldObject)
        self._repo.save(obj=newObject)

    @debugLogger
    def roles(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
              order: List[dict] = None):
        return self._repo.roles(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
