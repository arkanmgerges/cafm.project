"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import time
from typing import Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.MaintenanceProcedureApplicationService import (
    MaintenanceProcedureApplicationService,
)
from src.domain_model.project.maintenance.procedure.MaintenanceProcedure import (
    MaintenanceProcedure,
)
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.domain_model.resource.exception.MaintenanceProcedureDoesNotExistException import (
    MaintenanceProcedureDoesNotExistException,
)
from src.domain_model.token.TokenService import TokenService
from src.port_adapter.api.grpc.listener.BaseListener import BaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.maintenance_procedure_app_service_pb2 import (
    MaintenanceProcedureAppService_maintenanceProceduresResponse,
    MaintenanceProcedureAppService_maintenanceProcedureByIdResponse,
    MaintenanceProcedureAppService_newIdResponse,
)
from src.resource.proto._generated.maintenance_procedure_app_service_pb2_grpc import (
    MaintenanceProcedureAppServiceServicer,
)
from src.resource.proto._generated.maintenance_procedure_app_service_pb2 import (
    MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdResponse,
)


class MaintenanceProcedureAppServiceListener(MaintenanceProcedureAppServiceServicer, BaseListener):
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
                f"[{MaintenanceProcedureAppServiceListener.newId.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
                    token: {token}"
            )
            appService: MaintenanceProcedureApplicationService = AppDi.instance.get(
                MaintenanceProcedureApplicationService
            )
            return MaintenanceProcedureAppService_newIdResponse(id=appService.newId())
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return MaintenanceProcedureAppService_newIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def maintenanceProcedures(self, request, context):
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
                f"[{MaintenanceProcedureAppServiceListener.maintenanceProcedures.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            maintenanceProcedureAppService: MaintenanceProcedureApplicationService = (
                AppDi.instance.get(MaintenanceProcedureApplicationService)
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = maintenanceProcedureAppService.maintenanceProcedures(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
            )
            response = MaintenanceProcedureAppService_maintenanceProceduresResponse()
            for item in result["items"]:
                response.maintenanceProcedures.add(
                    id=item.id(),
                    name=item.name(),
                    type=item.type(),
                    subType=item.subType(),
                    frequency=item.frequency(),
                    startDate=item.startDate() if item.startDate is not None else 0,
                    subcontractorId=item.subcontractorId(),
                    equipmentId=item.equipmentId(),
                )
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{MaintenanceProcedureAppServiceListener.maintenanceProcedures.__qualname__}] - response: {response}"
            )
            return MaintenanceProcedureAppService_maintenanceProceduresResponse(
                maintenanceProcedures=response.maintenanceProcedures,
                totalItemCount=response.totalItemCount,
            )
        except MaintenanceProcedureDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No maintenanceProcedures found")
            return MaintenanceProcedureAppService_maintenanceProceduresResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return MaintenanceProcedureAppService_maintenanceProceduresResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def maintenanceProcedureById(self, request, context):
        try:
            token = self._token(context)
            appService: MaintenanceProcedureApplicationService = AppDi.instance.get(
                MaintenanceProcedureApplicationService
            )
            obj: MaintenanceProcedure = appService.maintenanceProcedureById(
                id=request.id, token=token
            )
            logger.debug(
                f"[{MaintenanceProcedureAppServiceListener.maintenanceProcedureById.__qualname__}] - response: {obj}"
            )
            response = MaintenanceProcedureAppService_maintenanceProcedureByIdResponse()
            self._addObjectToResponse(obj=obj, response=response)
            return response
        except MaintenanceProcedureDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("maintenance procedure does not exist")
            return MaintenanceProcedureAppService_maintenanceProcedureByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return MaintenanceProcedureAppService_maintenanceProcedureByIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def maintenanceProceduresByEquipmentId(self, request, context):
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
                f"[{MaintenanceProcedureAppServiceListener.maintenanceProceduresByEquipmentId.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            maintenanceProcedureAppService: MaintenanceProcedureApplicationService = (
                AppDi.instance.get(MaintenanceProcedureApplicationService)
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = (
                maintenanceProcedureAppService.maintenanceProceduresByEquipmentId(
                    equipmentId=request.equipmentId,
                    resultFrom=request.resultFrom,
                    resultSize=resultSize,
                    token=token,
                    order=orderData,
                )
            )
            response = (
                MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdResponse()
            )
            for item in result["items"]:
                response.maintenanceProcedures.add(
                    id=item.id(),
                    name=item.name(),
                    type=item.type(),
                    subType=item.subType(),
                    frequency=item.frequency(),
                    startDate=item.startDate() if item.startDate is not None else 0,
                    subcontractorId=item.subcontractorId(),
                    equipmentId=item.equipmentId(),
                )
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{MaintenanceProcedureAppServiceListener.maintenanceProceduresByEquipmentId.__qualname__}] - response: {response}"
            )
            return MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdResponse(
                maintenanceProcedures=response.maintenanceProcedures,
                totalItemCount=response.totalItemCount,
            )
        except MaintenanceProcedureDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No maintenanceProcedures found")
            return (
                MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdResponse()
            )
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return (
                MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdResponse()
            )

    @debugLogger
    def _addObjectToResponse(self, obj: MaintenanceProcedure, response: Any):
        response.maintenanceProcedure.id = obj.id()
        response.maintenanceProcedure.name = obj.name()
        response.maintenanceProcedure.type = obj.type()
        response.maintenanceProcedure.subType = obj.subType() if obj.subType() is not None else ""
        response.maintenanceProcedure.frequency = obj.frequency()
        response.maintenanceProcedure.startDate = obj.startDate() if obj.startDate() is not None else 0
        response.maintenanceProcedure.subcontractorId = obj.subcontractorId()
        response.maintenanceProcedure.equipmentId = obj.equipmentId()

    @debugLogger
    def _token(self, context) -> str:
        return super()._token(context=context)
