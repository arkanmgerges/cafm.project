"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import time
from typing import Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.MaintenanceProcedureOperationParameterApplicationService import (
    MaintenanceProcedureOperationParameterApplicationService,
)
from src.domain_model.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameter import (
    MaintenanceProcedureOperationParameter,
)
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.domain_model.resource.exception.MaintenanceProcedureOperationParameterDoesNotExistException import (
    MaintenanceProcedureOperationParameterDoesNotExistException,
)
from src.domain_model.token.TokenService import TokenService
from src.port_adapter.api.grpc.listener.BaseListener import BaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.maintenance_procedure_operation_parameter_app_service_pb2 import (
    MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse,
    MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse,
    MaintenanceProcedureOperationParameterAppService_newIdResponse,
)
from src.resource.proto._generated.maintenance_procedure_operation_parameter_app_service_pb2_grpc import (
    MaintenanceProcedureOperationParameterAppServiceServicer,
)
from src.resource.proto._generated.maintenance_procedure_operation_parameter_app_service_pb2 import (
    MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse,
)


class MaintenanceProcedureOperationParameterAppServiceListener(
    MaintenanceProcedureOperationParameterAppServiceServicer, BaseListener
):
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
                f"[{MaintenanceProcedureOperationParameterAppServiceListener.newId.__qualname__}] - claims: {claims}\n\t \
                    token: {token}"
            )
            appService: MaintenanceProcedureOperationParameterApplicationService = (
                AppDi.instance.get(
                    MaintenanceProcedureOperationParameterApplicationService
                )
            )
            return MaintenanceProcedureOperationParameterAppService_newIdResponse(
                id=appService.newId()
            )
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return MaintenanceProcedureOperationParameterAppService_newIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def maintenanceProcedureOperationParameters(self, request, context):
        try:
            token = self._token(context)

            resultSize = request.resultSize if request.resultSize >= 0 else 10
            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{MaintenanceProcedureOperationParameterAppServiceListener.maintenanceProcedureOperationParameters.__qualname__}] - claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            maintenanceProcedureOperationParameterAppService: MaintenanceProcedureOperationParameterApplicationService = AppDi.instance.get(
                MaintenanceProcedureOperationParameterApplicationService
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = maintenanceProcedureOperationParameterAppService.maintenanceProcedureOperationParameters(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
            )
            response = (
                MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse()
            )
            for item in result["items"]:
                response.maintenanceProcedureOperationParameters.add(
                    id=item.id(),
                    name=item.name(),
                    unitId=item.unitId(),
                    maintenanceProcedureOperationId=item.maintenanceProcedureOperationId(),
                    minValue=str(item.minValue())
                    if item.minValue is not None
                    else str(0),
                    maxValue=str(item.maxValue())
                    if item.maxValue is not None
                    else str(0),
                )
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{MaintenanceProcedureOperationParameterAppServiceListener.maintenanceProcedureOperationParameters.__qualname__}] - response: {response}"
            )
            return MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse(
                maintenanceProcedureOperationParameters=response.maintenanceProcedureOperationParameters,
                totalItemCount=response.totalItemCount,
            )
        except MaintenanceProcedureOperationParameterDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No maintenanceProcedureOperationParameters found")
            return (
                MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse()
            )
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return (
                MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse()
            )

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def maintenanceProcedureOperationParameterById(self, request, context):
        try:
            token = self._token(context)
            appService: MaintenanceProcedureOperationParameterApplicationService = (
                AppDi.instance.get(
                    MaintenanceProcedureOperationParameterApplicationService
                )
            )
            obj: MaintenanceProcedureOperationParameter = (
                appService.maintenanceProcedureOperationParameterById(
                    id=request.id, token=token
                )
            )
            logger.debug(
                f"[{MaintenanceProcedureOperationParameterAppServiceListener.maintenanceProcedureOperationParameterById.__qualname__}] - response: {obj}"
            )
            response = (
                MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse()
            )
            self._addObjectToResponse(obj=obj, response=response)
            return response
        except MaintenanceProcedureOperationParameterDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(
                "maintenance procedure operation parameter does not exist"
            )
            return (
                MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse()
            )
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return (
                MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse()
            )

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def maintenanceProcedureOperationParametersByMaintenanceProcedureOperationId(
        self, request, context
    ):
        try:
            token = self._token(context)

            resultSize = request.resultSize if request.resultSize >= 0 else 10
            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{MaintenanceProcedureOperationParameterAppServiceListener.maintenanceProcedureOperationParametersByMaintenanceProcedureOperationId.__qualname__}] - claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            maintenanceProcedureOperationParameterAppService: MaintenanceProcedureOperationParameterApplicationService = AppDi.instance.get(
                MaintenanceProcedureOperationParameterApplicationService
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = maintenanceProcedureOperationParameterAppService.maintenanceProcedureOperationParametersByMaintenanceProcedureOperationId(
                maintenanceProcedureOperationId=request.maintenanceProcedureOperationId,
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
            )
            response = (
                MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse()
            )
            for item in result["items"]:
                response.maintenanceProcedureOperationParameters.add(
                    id=item.id(),
                    name=item.name(),
                    unitId=item.unitId(),
                    maintenanceProcedureOperationId=item.maintenanceProcedureOperationId(),
                    minValue=str(item.minValue())
                    if item.minValue is not None
                    else str(0),
                    maxValue=str(item.maxValue())
                    if item.maxValue is not None
                    else str(0),
                )
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{MaintenanceProcedureOperationParameterAppServiceListener.maintenanceProcedureOperationParametersByMaintenanceProcedureOperationId.__qualname__}] - response: {response}"
            )
            return MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse(
                maintenanceProcedureOperationParameters=response.maintenanceProcedureOperationParameters,
                totalItemCount=response.totalItemCount,
            )
        except MaintenanceProcedureOperationParameterDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No maintenanceProcedureOperationParameters found")
            return (
                MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse()
            )
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return (
                MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse()
            )

    @debugLogger
    def _addObjectToResponse(
        self, obj: MaintenanceProcedureOperationParameter, response: Any
    ):
        response.maintenanceProcedureOperationParameter.id = obj.id()
        response.maintenanceProcedureOperationParameter.name = obj.name()
        response.maintenanceProcedureOperationParameter.unitId = obj.unitId()
        response.maintenanceProcedureOperationParameter.maintenanceProcedureOperationId = (
            obj.maintenanceProcedureOperationId()
        )
        response.maintenanceProcedureOperationParameter.minValue = (
            str(obj.minValue()) if obj.minValue() is not None else str(0)
        )
        response.maintenanceProcedureOperationParameter.maxValue = (
            str(obj.maxValue()) if obj.maxValue() is not None else str(0)
        )

    @debugLogger
    def _token(self, context) -> str:
        return super()._token(context=context)
