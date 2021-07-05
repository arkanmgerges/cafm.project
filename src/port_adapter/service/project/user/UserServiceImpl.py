"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.application.lookup.user.UserLookupRepository import UserLookupRepository
from src.domain_model.resource.exception.UserDoesNotExistException import UserDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.domain_model.user.UserRepository import UserRepository
from src.domain_model.user.UserService import UserService
from src.port_adapter.service.identity.IdentityAndAccessAdapter import IdentityAndAccessAdapter
from src.resource.logging.decorator import debugLogger


class UserServiceImpl(UserService):
    def __init__(self, userRepo: UserRepository,
                 lookupUserRepo: UserLookupRepository,
                 identityAndAccessAdapter: IdentityAndAccessAdapter):
        self._repo = userRepo
        self._lookupRepo = lookupUserRepo
        self._identityAndAccessAdapter = identityAndAccessAdapter

    @debugLogger
    def userById(
            self,
            tokenData: TokenData = None,
            id: str = "",
    ):
        try:
            _ = self._identityAndAccessAdapter.userById(tokenData=tokenData, id=id)
        except:
            raise UserDoesNotExistException(f'user id: {id}')
        return self._repo.userById(id = id,)

    @debugLogger
    def users(
            self,
            tokenData: TokenData = None,
            resultFrom: int = 0,
            resultSize: int = 100,
            order: List[dict] = None,
    ):
        userList = self._identityAndAccessAdapter.users(tokenData=tokenData)["items"]
        return self._repo.usersFilteredByUserList(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            userList=userList,
        )

    @debugLogger
    def usersByOrganizationId(
        self,
        organizationId: str,
        tokenData: TokenData = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
    ):
        # userList = self._identityAndAccessAdapter.usersByOrganizationId(tokenData=tokenData,
        #                                                                       organizationId=organizationId)["items"]
        # return self._repo.usersFilteredByUserList(
        #     tokenData=tokenData,
        #     resultFrom=resultFrom,
        #     resultSize=resultSize,
        #     order=order,
        #     userList=userList,
        # )
        pass

    def usersIncludeOrganizationsAndRoles(self,
        tokenData: TokenData = None,
        type: str = None,
        resultFrom: int = 0,
        resultSize: int = 100,
        order: List[dict] = None,
        filter: List[dict] = None,) -> dict:

        response = self._identityAndAccessAdapter.usersIncludeOrganizationsAndRoles(tokenData=tokenData)["items"]
        return self._lookupRepo.usersFilteredByUsersIncludeOrganizationsAndRoles(
            tokenData=tokenData,
            resultFrom=resultFrom,
            resultSize=resultSize,
            order=order,
            filter=filter,
            usersIncludeOrganizationsAndRoles=response,
        )