"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import time
from typing import Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.RoleApplicationService import RoleApplicationService
from src.domain_model.role.Role import Role
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.domain_model.resource.exception.RoleDoesNotExistException import (
    RoleDoesNotExistException,
)
from src.domain_model.token.TokenService import TokenService
from src.port_adapter.api.grpc.listener.BaseListener import BaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.role_app_service_pb2 import (
    RoleAppService_rolesByOrganizationTypeResponse,
    RoleAppService_rolesResponse,
    RoleAppService_roleByIdResponse,
    RoleAppService_newIdResponse,
)
from src.resource.proto._generated.role_app_service_pb2_grpc import (
    RoleAppServiceServicer,
)


class RoleAppServiceListener(RoleAppServiceServicer, BaseListener):
    """The listener function implements the rpc call as described in the .proto file"""

    def __init__(self):
        self.counter = 0
        self.last_print_time = time.time()
        self._tokenService = TokenService()

    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def newId(self, request, context):
        try:
            token = self._token(context)

            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{RoleAppServiceListener.newId.__qualname__}] - claims: {claims}\n\t \
                    token: {token}"
            )
            roleAppService: RoleApplicationService = AppDi.instance.get(
                RoleApplicationService
            )
            return RoleAppService_newIdResponse(id=roleAppService.newId())
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return RoleAppService_newIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def roles(self, request, context):
        try:
            token = self._token(context)

            resultSize = request.resultSize if request.resultSize >= 0 else 10
            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{RoleAppServiceListener.roles.__qualname__}] - claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            roleAppService: RoleApplicationService = AppDi.instance.get(
                RoleApplicationService
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = roleAppService.roles(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
            )
            response = RoleAppService_rolesResponse()
            for item in result["items"]:
                response.roles.add(
                    id=item.id(),
                    name=item.name(),
                    title=item.title(),
                )
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{RoleAppServiceListener.roles.__qualname__}] - response: {response}"
            )
            return RoleAppService_rolesResponse(
                roles=response.roles, totalItemCount=response.totalItemCount
            )
        except RoleDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No roles found")
            return RoleAppService_rolesResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return RoleAppService_rolesResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def rolesByOrganizationType(self, request, context):
        try:
            token = self._token(context)

            resultSize = request.resultSize if request.resultSize >= 0 else 10
            resultFrom = request.resultFrom
            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{RoleAppServiceListener.rolesByOrganizationType.__qualname__}] - claims: {claims}\n\t \
resultFrom: {resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            roleAppService: RoleApplicationService = AppDi.instance.get(
                RoleApplicationService
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = roleAppService.rolesByOrganizationType(
                organizationType=request.organizationType,
                resultFrom=resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
            )
            response = RoleAppService_rolesByOrganizationTypeResponse()
            for item in result["items"]:
                response.roles.add(
                    id=item.id(),
                    name=item.name(),
                    title=item.title(),
                )
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{RoleAppServiceListener.rolesByOrganizationType.__qualname__}] - response: {response}"
            )
            return RoleAppService_rolesByOrganizationTypeResponse(
                roles=response.roles, totalItemCount=response.totalItemCount
            )
        except RoleDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No roles found")
            return RoleAppService_rolesByOrganizationTypeResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return RoleAppService_rolesByOrganizationTypeResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def roleById(self, request, context):
        try:
            token = self._token(context)
            roleAppService: RoleApplicationService = AppDi.instance.get(
                RoleApplicationService
            )
            obj: Role = roleAppService.roleById(id=request.id, token=token)
            logger.debug(
                f"[{RoleAppServiceListener.roleById.__qualname__}] - response: {obj}"
            )
            response = RoleAppService_roleByIdResponse()
            self._addObjectToResponse(obj=obj, response=response)
            return response
        except RoleDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("role does not exist")
            return RoleAppService_roleByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return RoleAppService_roleByIdResponse()

    @debugLogger
    def _addObjectToResponse(self, obj: Role, response: Any):
        response.role.id = obj.id()
        response.role.name = obj.name()
        response.role.title = obj.title()

    @debugLogger
    def _token(self, context) -> str:
        return super()._token(context=context)
