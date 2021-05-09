"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.resource.exception.UpdateRoleFailedException import (
    UpdateRoleFailedException,
)
from src.domain_model.role.Role import Role
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.role.RoleService import RoleService
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class RoleApplicationService:
    def __init__(self, repo: RoleRepository, domainService: RoleService):
        self._repo = repo
        self._domainService = domainService

    @debugLogger
    def newId(self):
        return Role.createFrom().id()

    @debugLogger
    def createRole(
        self,
        id: str = None,
        name: str = "",
        title: str = "",
        objectOnly: bool = False,
        token: str = "",
    ) -> Role:
        obj: Role = self.constructObject(id=id, name=name, title=title)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._domainService.createRole(
            obj=obj, objectOnly=objectOnly, tokenData=tokenData
        )

    @debugLogger
    def updateRole(
        self, id: str = None, name: str = "", title: str = "", token: str = ""
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObj: Role = self._repo.roleById(id=id)
            obj: Role = self.constructObject(
                id=id, name=name, title=title, _sourceObject=oldObj
            )
            self._domainService.updateRole(
                oldObject=oldObj, newObject=obj, tokenData=tokenData
            )
        except Exception as e:
            raise UpdateRoleFailedException(message=str(e))

    @debugLogger
    def deleteRole(self, id: str, token: str = ""):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.roleById(id=id)
        self._domainService.deleteRole(obj=obj, tokenData=tokenData)

    @debugLogger
    def roleByEmail(self, name: str, token: str = "") -> Role:
        obj = self._repo.roleByName(name=name)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return obj

    @debugLogger
    def roleById(self, id: str, token: str = "") -> Role:
        obj = self._repo.roleById(id=id)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return obj

    @debugLogger
    def roles(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        token: str = "",
        order: List[dict] = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._domainService.roles(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
        )

    @debugLogger
    def constructObject(
        self,
        id: str = None,
        name: str = "",
        title: str = "",
        _sourceObject: Role = None,
        skipValidation: bool = False,
    ) -> Role:
        if _sourceObject is not None:
            return Role.createFrom(
                id=id,
                name=name if name is not None else _sourceObject.name(),
                title=title if title is not None else _sourceObject.title(),
                skipValidation=skipValidation,
            )
        else:
            return Role.createFrom(
                id=id,
                name=name,
                title=title,
                skipValidation=skipValidation,
            )
