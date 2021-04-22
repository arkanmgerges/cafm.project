"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import time
from typing import Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.StandardMaintenanceProcedureApplicationService import (
    StandardMaintenanceProcedureApplicationService,
)
from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedure import (
    StandardMaintenanceProcedure,
)
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.domain_model.resource.exception.StandardMaintenanceProcedureDoesNotExistException import (
    StandardMaintenanceProcedureDoesNotExistException,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.standard_maintenance_procedure_app_service_pb2 import (
    StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse,
    StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse,
    StandardMaintenanceProcedureAppService_newIdResponse,
)
from src.resource.proto._generated.standard_maintenance_procedure_app_service_pb2_grpc import (
    StandardMaintenanceProcedureAppServiceServicer,
)


class StandardMaintenanceProcedureAppServiceListener(
    StandardMaintenanceProcedureAppServiceServicer
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
            metadata = context.invocation_metadata()
            claims = (
                self._tokenService.claimsFromToken(token=metadata[0].value)
                if "token" in metadata[0]
                else None
            )
            logger.debug(
                f"[{StandardMaintenanceProcedureAppServiceListener.newId.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
                    token: {token}"
            )
            appService: StandardMaintenanceProcedureApplicationService = (
                AppDi.instance.get(StandardMaintenanceProcedureApplicationService)
            )
            return StandardMaintenanceProcedureAppService_newIdResponse(
                id=appService.newId()
            )
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return StandardMaintenanceProcedureAppService_newIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def standardMaintenanceProcedures(self, request, context):
        try:
            token = self._token(context)
            metadata = context.invocation_metadata()
            resultSize = request.resultSize if request.resultSize >= 0 else 10
            claims = (
                self._tokenService.claimsFromToken(token=metadata[0].value)
                if "token" in metadata[0]
                else None
            )
            logger.debug(
                f"[{StandardMaintenanceProcedureAppServiceListener.standardMaintenanceProcedures.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            standardMaintenanceProcedureAppService: StandardMaintenanceProcedureApplicationService = AppDi.instance.get(
                StandardMaintenanceProcedureApplicationService
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = (
                standardMaintenanceProcedureAppService.standardMaintenanceProcedures(
                    resultFrom=request.resultFrom,
                    resultSize=resultSize,
                    token=token,
                    order=orderData,
                )
            )
            response = (
                StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse()
            )
            for item in result["items"]:
                response.standardMaintenanceProcedures.add(
                    id=item.id(),
                    name=item.name(),
                    type=item.type(),
                    subtype=item.subtype(),
                    frequency=item.frequency(),
                    startDate=item.startDate(),
                    organizationId=item.organizationId(),
                    standardEquipmentCategoryGroupId=item.standardEquipmentCategoryGroupId(),
                )
            response.itemCount = result["itemCount"]
            logger.debug(
                f"[{StandardMaintenanceProcedureAppServiceListener.standardMaintenanceProcedures.__qualname__}] - response: {response}"
            )
            return StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse(
                standardMaintenanceProcedures=response.standardMaintenanceProcedures,
                itemCount=response.itemCount,
            )
        except StandardMaintenanceProcedureDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No standardMaintenanceProcedures found")
            return (
                StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse()
            )
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return (
                StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse()
            )

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def standardMaintenanceProcedureById(self, request, context):
        try:
            token = self._token(context)
            appService: StandardMaintenanceProcedureApplicationService = (
                AppDi.instance.get(StandardMaintenanceProcedureApplicationService)
            )
            obj: StandardMaintenanceProcedure = (
                appService.standardMaintenanceProcedureById(id=request.id, token=token)
            )
            logger.debug(
                f"[{StandardMaintenanceProcedureAppServiceListener.standardMaintenanceProcedureById.__qualname__}] - response: {obj}"
            )
            response = (
                StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse()
            )
            self._addObjectToResponse(obj=obj, response=response)
            return response
        except StandardMaintenanceProcedureDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("standard maintenance procedure does not exist")
            return (
                StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse()
            )
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return (
                StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse()
            )

    @debugLogger
    def _addObjectToResponse(self, obj: StandardMaintenanceProcedure, response: Any):
        response.standardMaintenanceProcedure.id = obj.id()
        response.standardMaintenanceProcedure.name = obj.name()
        response.standardMaintenanceProcedure.type = obj.type()
        response.standardMaintenanceProcedure.subtype = obj.subtype()
        response.standardMaintenanceProcedure.frequency = obj.frequency()
        response.standardMaintenanceProcedure.startDate = obj.startDate()
        response.standardMaintenanceProcedure.organizationId = obj.organizationId()
        response.standardMaintenanceProcedure.standardEquipmentCategoryGroupId = (
            obj.standardEquipmentCategoryGroupId()
        )

    @debugLogger
    def _token(self, context) -> str:
        metadata = context.invocation_metadata()
        if "token" in metadata[0]:
            return metadata[0].value
        return ""
