"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.role.Role import Role
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.resource.exception.RoleAlreadyExistException import RoleAlreadyExistException
from src.domain_model.resource.exception.RoleDoesNotExistException import RoleDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.resource.logging.decorator import debugLogger


class RoleService:
    def __init__(self, roleRepo: RoleRepository):
        self._repo = roleRepo

    @debugLogger
    def createRole(self, id: str = None, name: str = '', objectOnly: bool = False, tokenData: TokenData = None):
        try:
            if id == '':
                raise RoleDoesNotExistException()
            self._repo.roleById(id=id)
            raise RoleAlreadyExistException(name)
        except RoleDoesNotExistException:
            if objectOnly:
                if id == '':
                    id = None
                return Role.createFrom(id=id, name=name)
            else:
                obj: Role = Role.createFrom(id=id, name=name, publishEvent=True)
                self._repo.createRole(role=obj, tokenData=tokenData)
                return obj

    @debugLogger
    def deleteRole(self, role: Role, tokenData: TokenData = None):
        self._repo.deleteRole(role, tokenData=tokenData)
        role.publishDelete()

    @debugLogger
    def updateRole(self, oldObject: Role, newObject: Role, tokenData: TokenData = None):
        self._repo.updateRole(newObject, tokenData=tokenData)
        newObject.publishUpdate(oldObject)

    @debugLogger
    def roles(self, tokenData: TokenData = None, resultFrom: int = 0, resultSize: int = 100,
                      order: List[dict] = None):
        return self._repo.roles(tokenData=tokenData, resultFrom=resultFrom, resultSize=resultSize, order=order)
