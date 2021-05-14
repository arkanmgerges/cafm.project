"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.domain_model.resource.exception.UpdateRoleFailedException import (
    UpdateRoleFailedException,
)
from src.domain_model.role.Role import Role
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.role.RoleService import RoleService
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger


class RoleApplicationService(BaseApplicationService):
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
        obj: Role = self._constructObject(id=id, name=name, title=title)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._domainService.createRole(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def updateRole(self, id: str = None, name: str = "", title: str = "", token: str = ""):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObj: Role = self._repo.roleById(id=id)
            obj: Role = self._constructObject(id=id, name=name, title=title, _sourceObject=oldObj)
            self._domainService.updateRole(oldObject=oldObj, newObject=obj, tokenData=tokenData)
        except Exception as e:
            logger.warn(
                f"[{RoleApplicationService.__init__.__qualname__}] Could not update role with \
                    id: {id}, name: {name}, title: {title}"
            )
            raise UpdateRoleFailedException(message=str(e))

    @debugLogger
    def deleteRole(self, id: str, token: str = ""):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj = self._repo.roleById(id=id)
        self._domainService.deleteRole(obj=obj, tokenData=tokenData)

    @debugLogger
    def roleByEmail(self, name: str, token: str = "") -> Role:
        obj = self._repo.roleByName(name=name)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        return obj

    @debugLogger
    def roleById(self, id: str, token: str = "") -> Role:
        obj = self._repo.roleById(id=id)
        _tokenData = TokenService.tokenDataFromToken(token=token)
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
    def _constructObject(self, *args, **kwargs) -> Role:
        kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS] = Role
        return super()._constructObject(*args, **kwargs)
