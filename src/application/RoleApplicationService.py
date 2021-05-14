"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.application.model.BaseApplicationServiceBulkData import BaseApplicationServiceBulkData
from src.application.model.BaseApplicationServiceModelData import BaseApplicationServiceModelData
from src.domain_model.resource.exception.UpdateRoleFailedException import (
    UpdateRoleFailedException,
)
from src.domain_model.role.Role import Role
from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.role.RoleService import RoleService
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger


class RoleApplicationService(BaseApplicationService):
    def __init__(self, repo: RoleRepository, domainService: RoleService):
        self._repo = repo
        self._roleService = domainService

    @debugLogger
    def newId(self):
        return Role.createFrom().id()

    @debugLogger
    def createRole(self, token: str = None, objectOnly: bool = False, **kwargs):
        obj: Role = self._constructObject(**kwargs)
        tokenData = TokenService.tokenDataFromToken(token=token)
        return self._roleService.createRole(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @debugLogger
    def roleByEmail(self, name: str, token: str = "") -> Role:
        obj = self._repo.roleByName(name=name)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        return obj

    @debugLogger
    def updateRole(
        self,
        token: str = None,
        **kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: Role = self._repo.roleById(id=kwargs["id"])
            super().callFunction(
                modelData=BaseApplicationServiceModelData(
                    function=self._roleService.updateRole,
                    kwargs={
                        "oldObject": oldObject,
                        "newObject": self._constructObject(_sourceObject=oldObject, **kwargs),
                        "tokenData": tokenData,
                    },
                )
            )

        except Exception as e:
            raise UpdateRoleFailedException(message=str(e))

    @debugLogger
    def deleteRole(self, id: str, token: str = None):
        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._roleService.deleteRole,
                kwargs={"obj": self._repo.roleById(id=id), "tokenData": TokenService.tokenDataFromToken(token=token)},
            )
        )

    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = ""):
        super()._bulkCreate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="role_id",
                domainService=self._roleService,
            )
        )

    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = ""):
        super()._bulkDelete(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="role_id",
                domainService=self._roleService,
            )
        )

    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = ""):
        super()._bulkUpdate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="role_id",
                domainService=self._roleService,
                repositoryCallbackFunction=self._repo.roleById,
            )
        )

    @debugLogger
    def roleById(self, id: str, token: str = None) -> Role:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(getterFunction=self._repo.roleById, kwargs={"id": id})
        )

    @debugLogger
    def roles(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._roleService.roles,
                kwargs={"resultFrom": resultFrom, "resultSize": resultSize, "order": order, "tokenData": tokenData},
            )
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> Role:
        kwargs[BaseApplicationService.APPLICATION_SERVICE_CLASS] = Role
        return super()._constructObject(*args, **kwargs)
