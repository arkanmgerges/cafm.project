"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import os

import grpc

from src.domain_model.token.TokenData import TokenData
from src.port_adapter.service.identity.IdentityAndAccessAdapter import IdentityAndAccessAdapter
from src.port_adapter.service.identity.ProjectTranslator import ProjectTranslator
from src.resource.proto._generated.identity.project_app_service_pb2 import ProjectAppService_projectsRequest, \
    ProjectAppService_projectsResponse, ProjectAppService_projectsByRealmIdRequest, \
    ProjectAppService_projectsByRealmIdResponse
from src.resource.proto._generated.identity.project_app_service_pb2_grpc import ProjectAppServiceStub


class IdentityAndAccessAdapterImpl(IdentityAndAccessAdapter):
    def __init__(self):
        self._server = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE", "")
        self._port = os.getenv("CAFM_IDENTITY_GRPC_SERVER_SERVICE_PORT", "")

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

    def projectsByRealmId(self, tokenData: TokenData = None, realmId: str = None) -> dict:
        with grpc.insecure_channel(f"{self._server}:{self._port}") as channel:
            stub = ProjectAppServiceStub(channel)
            try:
                request = ProjectAppService_projectsByRealmIdRequest(
                    orders=[], result_from=0, result_size=999999, realm_id=realmId
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