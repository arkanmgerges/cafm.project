"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

import grpc

from src.domain_model.token.TokenData import TokenData
from src.port_adapter.service.identity.IdentityAndAccessAdapter import IdentityAndAccessAdapter
from src.port_adapter.service.identity.OrganizationTranslator import OrganizationTranslator
from src.port_adapter.service.identity.ProjectTranslator import ProjectTranslator
from src.port_adapter.service.identity.RoleTranslator import RoleTranslator
from src.port_adapter.service.identity.UserTranslator import UserTranslator
from src.resource.proto._generated.identity.policy_app_service_pb2 import \
    PolicyAppService_realmsIncludeUsersIncludeRolesRequest, PolicyAppService_realmsIncludeUsersIncludeRolesResponse
from src.resource.proto._generated.identity.policy_app_service_pb2_grpc import PolicyAppServiceStub
from src.resource.proto._generated.identity.project_app_service_pb2 import ProjectAppService_projectsRequest, \
    ProjectAppService_projectsResponse, ProjectAppService_projectsByRealmIdRequest, \
    ProjectAppService_projectsByRealmIdResponse, ProjectAppService_projectByIdRequest, \
    ProjectAppService_projectByIdResponse
from src.resource.proto._generated.identity.project_app_service_pb2_grpc import ProjectAppServiceStub
from src.resource.proto._generated.identity.realm_app_service_pb2 import RealmAppService_realmsResponse, \
    RealmAppService_realmsRequest, RealmAppService_realmsByTypeRequest, RealmAppService_realmsByTypeResponse
from src.resource.proto._generated.identity.realm_app_service_pb2_grpc import RealmAppServiceStub
from src.resource.proto._generated.identity.role_app_service_pb2 import RoleAppService_roleByIdRequest, \
    RoleAppService_roleByIdResponse, RoleAppService_rolesRequest, RoleAppService_rolesResponse
from src.resource.proto._generated.identity.role_app_service_pb2_grpc import RoleAppServiceStub
from src.resource.proto._generated.identity.user_app_service_pb2 import UserAppService_userByIdRequest, \
    UserAppService_userByIdResponse, UserAppService_usersRequest, UserAppService_usersResponse
from src.resource.proto._generated.identity.user_app_service_pb2_grpc import UserAppServiceStub


class IdentityAndAccessAdapterImpl(IdentityAndAccessAdapter):
    def __init__(self):
        self._server = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT", "")

    # region Project
    def projectById(self, tokenData: TokenData = None, id: str = None) -> dict:
        from src.resource.logging.logger import logger
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                request = ProjectAppService_projectByIdRequest(id=id)
                response: ProjectAppService_projectByIdResponse = stub.project_by_id.with_call(
                    request,
                    metadata=(
                        ("token", tokenData.token()),
                    ),
                )

                return ProjectTranslator.toProjectFromIdentityGrpcResponse(response[0].project)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                logger.info(e)
                raise e

    def projects(self, tokenData: TokenData = None) -> dict:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                request = ProjectAppService_projectsRequest(
                    result_from=0, result_size=999999
                )
                response: ProjectAppService_projectsResponse = stub.projects.with_call(
                    request,
                    metadata=(
                        ("token", tokenData.token()),
                    ),
                )

                return {"items": [ProjectTranslator.toProjectFromIdentityGrpcResponse(x) for x in response[0].projects],
                        "totalItemCount": response[0].total_item_count}
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def projectsByOrganizationId(self, tokenData: TokenData = None, organizationId: str = None) -> dict:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                request = ProjectAppService_projectsByRealmIdRequest(
                    orders=[], result_from=0, result_size=999999, realm_id=organizationId
                )
                response: ProjectAppService_projectsByRealmIdResponse = stub.projects.with_call(
                    request,
                    metadata=(
                        ("token", tokenData.token()),
                    ),
                )

                return {"items": [ProjectTranslator.toProjectFromIdentityGrpcResponse(x) for x in response[0].projects],
                        "totalItemCount": response[0].total_item_count}
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
    # endregion

    # region Organization
    def organizations(self, tokenData: TokenData = None) -> dict:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RealmAppServiceStub(channel)
            try:
                request = RealmAppService_realmsRequest(
                    result_from=0, result_size=999999
                )
                response: RealmAppService_realmsResponse = stub.realms.with_call(
                    request,
                    metadata=(
                        ("token", tokenData.token()),
                    ),
                )

                return {"items": [OrganizationTranslator.toOrganizationFromIdentityGrpcResponse(x) for x in response[0].realms],
                        "totalItemCount": response[0].total_item_count}
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def organizationById(self, tokenData: TokenData = None, id: str = None) -> dict:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RealmAppServiceStub(channel)
            try:
                request = RealmAppService_realmsRequest(id=id)
                response: RealmAppService_realmsResponse = stub.realms.with_call(
                    request,
                    metadata=(
                        ("token", tokenData.token()),
                    ),
                )

                return {"items": [OrganizationTranslator.toOrganizationFromIdentityGrpcResponse(x) for x in response[0].realms],
                        "totalItemCount": response[0].total_item_count}
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def organizationsByType(self, tokenData: TokenData = None, type: str = None) -> dict:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RealmAppServiceStub(channel)
            try:
                request = RealmAppService_realmsByTypeRequest(
                    result_from=0, result_size=999999, realm_type=type
                )
                response: RealmAppService_realmsByTypeResponse = stub.realms_by_type.with_call(
                    request,
                    metadata=(
                        ("token", tokenData.token()),
                    ),
                )

                return {"items": [OrganizationTranslator.toOrganizationFromIdentityGrpcResponse(x) for x in response[0].realms],
                        "totalItemCount": response[0].total_item_count}
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    def organizationsIncludeUsersIncludeRoles(self, tokenData: TokenData = None) -> dict:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = PolicyAppServiceStub(channel)
            try:
                request = PolicyAppService_realmsIncludeUsersIncludeRolesRequest()
                response: PolicyAppService_realmsIncludeUsersIncludeRolesResponse = stub.realms_include_users_include_roles.with_call(
                    request,
                    metadata=(
                        ("token", tokenData.token()),
                    ),
                )
                return {"items": [OrganizationTranslator.toOrganizationIncludesUsersIncludeRolesFromIdentityGrpcResponse(x) for x in response[0].realm_includes_users_include_roles_items],
                        "totalItemCount": response[0].total_item_count}
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
    # endregion
    
    # region Role
    def roleById(self, tokenData: TokenData = None, id: str = None) -> dict:
        from src.resource.logging.logger import logger
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RoleAppServiceStub(channel)
            try:
                request = RoleAppService_roleByIdRequest(id=id)
                response: RoleAppService_roleByIdResponse = stub.role_by_id.with_call(
                    request,
                    metadata=(
                        ("token", tokenData.token()),
                    ),
                )

                return RoleTranslator.toRoleFromIdentityGrpcResponse(response[0].role)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                logger.info(e)
                raise e

    def roles(self, tokenData: TokenData = None) -> dict:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = RoleAppServiceStub(channel)
            try:
                request = RoleAppService_rolesRequest(
                    result_from=0, result_size=999999
                )
                response: RoleAppService_rolesResponse = stub.roles.with_call(
                    request,
                    metadata=(
                        ("token", tokenData.token()),
                    ),
                )

                from src.resource.logging.logger import logger
                return {"items": [RoleTranslator.toRoleFromIdentityGrpcResponse(x) for x in response[0].roles],
                        "totalItemCount": response[0].total_item_count}
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

    # endregion
    
    # region User
    def userById(self, tokenData: TokenData = None, id: str = None) -> dict:
        from src.resource.logging.logger import logger
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = UserAppServiceStub(channel)
            try:
                request = UserAppService_userByIdRequest(id=id)
                response: UserAppService_userByIdResponse = stub.user_by_id.with_call(
                    request,
                    metadata=(
                        ("token", tokenData.token()),
                    ),
                )

                return UserTranslator.toUserFromIdentityGrpcResponse(response[0].user)
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                logger.info(e)
                raise e

    def users(self, tokenData: TokenData = None) -> dict:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = UserAppServiceStub(channel)
            try:
                request = UserAppService_usersRequest(
                    result_from=0, result_size=999999
                )
                response: UserAppService_usersResponse = stub.users.with_call(
                    request,
                    metadata=(
                        ("token", tokenData.token()),
                    ),
                )

                from src.resource.logging.logger import logger
                return {"items": [UserTranslator.toUserFromIdentityGrpcResponse(x) for x in response[0].users],
                        "totalItemCount": response[0].total_item_count}
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e
    # endregion