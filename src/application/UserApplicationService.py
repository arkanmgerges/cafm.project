"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.BaseApplicationService import BaseApplicationService
from src.application.lifecycle.decorator.readOnly import readOnly
from src.application.lifecycle.decorator.transactional import transactional
from src.application.model.BaseApplicationServiceBulkData import BaseApplicationServiceBulkData
from src.application.model.BaseApplicationServiceModelData import BaseApplicationServiceModelData
from src.domain_model.resource.exception.UpdateUserFailedException import (
    UpdateUserFailedException,
)
from src.domain_model.token.TokenService import TokenService
from src.domain_model.user.User import User
from src.domain_model.user.UserRepository import UserRepository
from src.domain_model.user.UserService import UserService
from src.resource.logging.decorator import debugLogger


class UserApplicationService(BaseApplicationService):
    def __init__(self, repo: UserRepository, userService: UserService):
        self._repo = repo
        self._userService = userService

    @debugLogger
    def newId(self):
        return User.createFrom().id()

    @transactional
    @debugLogger
    def createUser(self, token: str = None, objectOnly: bool = False, **kwargs):
        tokenData = TokenService.tokenDataFromToken(token=token)
        obj: User = self._constructObject(**kwargs)
        return self._userService.createUser(obj=obj, objectOnly=objectOnly, tokenData=tokenData)

    @readOnly
    @debugLogger
    def userByEmail(self, email: str, token: str = "", **_kwargs) -> User:
        user = self._repo.userByEmail(email=email)
        _tokenData = TokenService.tokenDataFromToken(token=token)
        return user

    @transactional
    @debugLogger
    def updateUser(
        self,
        token: str = None,
        **kwargs,
    ):
        tokenData = TokenService.tokenDataFromToken(token=token)
        try:
            oldObject: User = self._repo.userById(id=kwargs["id"])
            super().callFunction(
                modelData=BaseApplicationServiceModelData(
                    function=self._userService.updateUser,
                    kwargs={
                        "oldObject": oldObject,
                        "newObject": self._constructObject(_sourceObject=oldObject, **kwargs),
                        "tokenData": tokenData,
                    },
                )
            )

        except Exception as e:
            raise UpdateUserFailedException(message=str(e))

    @transactional
    @debugLogger
    def deleteUser(self, id: str, token: str = None, **_kwargs):
        super().callFunction(
            modelData=BaseApplicationServiceModelData(
                function=self._userService.deleteUser,
                kwargs={"obj": self._repo.userById(id=id), "tokenData": TokenService.tokenDataFromToken(token=token)},
            )
        )

    @transactional
    @debugLogger
    def bulkCreate(self, objListParams: List[dict], token: str = ""):
        super()._bulkCreate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="user_id",
                domainService=self._userService,
            )
        )

    @transactional
    @debugLogger
    def bulkDelete(self, objListParams: List[dict], token: str = ""):
        super()._bulkDelete(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="user_id",
                domainService=self._userService,
            )
        )

    @transactional
    @debugLogger
    def bulkUpdate(self, objListParams: List[dict], token: str = ""):
        super()._bulkUpdate(
            baseBulkData=BaseApplicationServiceBulkData(
                objListParams=objListParams,
                token=token,
                sourceId="user_id",
                domainService=self._userService,
                repositoryCallbackFunction=self._repo.userById,
            )
        )

    @readOnly
    @debugLogger
    def userById(self, id: str, token: str = None, **_kwargs) -> User:
        TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(getterFunction=self._repo.userById, kwargs={"id": id})
        )

    @readOnly
    @debugLogger
    def users(
        self,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
        **_kwargs,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._userService.users,
                kwargs={"resultFrom": resultFrom, "resultSize": resultSize, "order": order, "tokenData": tokenData},
            )
        )

    @readOnly
    @debugLogger
    def usersByOrganizationId(
        self,
        organizationId: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        token: str = None,
        **_kwargs,
    ) -> dict:
        tokenData = TokenService.tokenDataFromToken(token=token)
        return super().callGetterFunction(
            modelData=BaseApplicationServiceModelData(
                getterFunction=self._userService.usersByOrganizationId,
                kwargs={"organizationId": organizationId, "resultFrom": resultFrom, "resultSize": resultSize, "order": order, "tokenData": tokenData},
            )
        )

    @debugLogger
    def _constructObject(self, *args, **kwargs) -> User:
        kwargs[BaseApplicationService.DOMAIN_MODEL_CLASS] = User
        return super()._constructObject(*args, **kwargs)
