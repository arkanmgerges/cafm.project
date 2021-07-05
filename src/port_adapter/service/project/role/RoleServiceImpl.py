"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List

from src.domain_model.role.RoleRepository import RoleRepository
from src.domain_model.role.RoleService import RoleService
from src.domain_model.resource.exception.RoleDoesNotExistException import RoleDoesNotExistException
from src.domain_model.token.TokenData import TokenData
from src.port_adapter.service.identity.IdentityAndAccessAdapter import IdentityAndAccessAdapter
from src.resource.logging.decorator import debugLogger


class RoleServiceImpl(RoleService):
    def __init__(self, roleRepo: RoleRepository, identityAndAccessAdapter: IdentityAndAccessAdapter):
        self._repo = roleRepo
        self._identityAndAccessAdapter = identityAndAccessAdapter

    # @debugLogger
    # def roleById(
    #         self,
    #         tokenData: TokenData = None,
    #         id: str = "",
    # ):
    #     try:
    #         _ = self._identityAndAccessAdapter.roleById(tokenData=tokenData, id=id)
    #     except:
    #         raise RoleDoesNotExistException(f'role id: {id}')
    #     return self._repo.roleById(id = id,)
    #
    # @debugLogger
    # def roles(
    #         self,
    #         tokenData: TokenData = None,
    #         resultFrom: int = 0,
    #         resultSize: int = 100,
    #         order: List[dict] = None,
    # ):
    #     roleList = self._identityAndAccessAdapter.roles(tokenData=tokenData)["items"]
    #     return self._repo.rolesFilteredByRoleList(
    #         tokenData=tokenData,
    #         resultFrom=resultFrom,
    #         resultSize=resultSize,
    #         order=order,
    #         roleList=roleList,
    #     )

    # @debugLogger
    # def rolesByTagName(
    #         self,
    #         tagName: str = None,
    #         tokenData: TokenData = None,
    #         resultFrom: int = 0,
    #         resultSize: int = 100,
    #         order: List[dict] = None,
    # ):
    #     roleList = self._identityAndAccessAdapter.rolesByTagName(tokenData=tokenData)["items"]
    #     return self._repo.rolesByFilteredByRoleList(
    #         tokenData=tokenData,
    #         resultFrom=resultFrom,
    #         resultSize=resultSize,
    #         order=order,
    #         roleList=roleList,
    #     )
    #
    # @debugLogger
    # def rolesByOrganizationType(
    #     self,
    #     organizationType: str,
    #     tokenData: TokenData = None,
    #     resultFrom: int = 0,
    #     resultSize: int = 100,
    #     order: List[dict] = None,
    # ):
    #     roleList = self._identityAndAccessAdapter.rolesByOrganizationType(tokenData=tokenData,
    #                                                                           organizationType=organizationType)["items"]
    #     return self._repo.rolesFilteredByRoleList(
    #         tokenData=tokenData,
    #         resultFrom=resultFrom,
    #         resultSize=resultSize,
    #         order=order,
    #         roleList=roleList,
    #     )