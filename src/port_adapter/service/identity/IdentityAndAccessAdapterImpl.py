"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

import grpc

from src.domain_model.token.TokenData import TokenData
from src.port_adapter.service.identity.IdentityAndAccessAdapter import IdentityAndAccessAdapter
from src.port_adapter.service.identity.OrganizationTranslator import OrganizationTranslator
from src.port_adapter.service.identity.ProjectTranslator import ProjectTranslator
from src.resource.proto._generated.identity.project_app_service_pb2 import ProjectAppService_projectsRequest, \
    ProjectAppService_projectsResponse, ProjectAppService_projectsByRealmIdRequest, \
    ProjectAppService_projectsByRealmIdResponse, ProjectAppService_projectByIdRequest, \
    ProjectAppService_projectByIdResponse
from src.resource.proto._generated.identity.project_app_service_pb2_grpc import ProjectAppServiceStub
from src.resource.proto._generated.identity.realm_app_service_pb2 import RealmAppService_realmsResponse, \
    RealmAppService_realmsRequest, RealmAppService_realmsByTypeRequest, RealmAppService_realmsByTypeResponse
from src.resource.proto._generated.identity.realm_app_service_pb2_grpc import RealmAppServiceStub


class IdentityAndAccessAdapterImpl(IdentityAndAccessAdapter):
    def __init__(self):
        self._server = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT", "")

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

                from src.resource.logging.logger import logger
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

                from src.resource.logging.logger import logger
                return {"items": [ProjectTranslator.toProjectFromIdentityGrpcResponse(x) for x in response[0].projects],
                        "totalItemCount": response[0].total_item_count}
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e

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

                from src.resource.logging.logger import logger
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

                from src.resource.logging.logger import logger
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

                from src.resource.logging.logger import logger
                return {"items": [OrganizationTranslator.toOrganizationFromIdentityGrpcResponse(x) for x in response[0].realms],
                        "totalItemCount": response[0].total_item_count}
            except Exception as e:
                channel.unsubscribe(lambda ch: ch.close())
                raise e