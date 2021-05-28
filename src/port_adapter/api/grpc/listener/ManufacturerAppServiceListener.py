"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import time
from typing import Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.ManufacturerApplicationService import (
    ManufacturerApplicationService,
)
from src.domain_model.manufacturer.Manufacturer import Manufacturer
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.domain_model.resource.exception.ManufacturerDoesNotExistException import (
    ManufacturerDoesNotExistException,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.manufacturer_app_service_pb2 import (
    ManufacturerAppService_manufacturersResponse,
    ManufacturerAppService_manufacturerByIdResponse,
    ManufacturerAppService_newIdResponse,
)
from src.resource.proto._generated.manufacturer_app_service_pb2_grpc import (
    ManufacturerAppServiceServicer,
)


class ManufacturerAppServiceListener(ManufacturerAppServiceServicer):
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
                f"[{ManufacturerAppServiceListener.newId.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
                    token: {token}"
            )
            appService: ManufacturerApplicationService = AppDi.instance.get(
                ManufacturerApplicationService
            )
            return ManufacturerAppService_newIdResponse(id=appService.newId())
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return ManufacturerAppService_newIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def manufacturers(self, request, context):
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
                f"[{ManufacturerAppServiceListener.manufacturers.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            manufacturerAppService: ManufacturerApplicationService = AppDi.instance.get(
                ManufacturerApplicationService
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = manufacturerAppService.manufacturers(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
            )
            response = ManufacturerAppService_manufacturersResponse()
            for item in result["items"]:
                response.manufacturers.add(
                    id=item.id(),
                    name=item.name(),
                )
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{ManufacturerAppServiceListener.manufacturers.__qualname__}] - response: {response}"
            )
            return ManufacturerAppService_manufacturersResponse(
                manufacturers=response.manufacturers, totalItemCount=response.totalItemCount
            )
        except ManufacturerDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No manufacturers found")
            return ManufacturerAppService_manufacturersResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return ManufacturerAppService_manufacturersResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def manufacturerById(self, request, context):
        try:
            token = self._token(context)
            appService: ManufacturerApplicationService = AppDi.instance.get(
                ManufacturerApplicationService
            )
            obj: Manufacturer = appService.manufacturerById(id=request.id, token=token)
            logger.debug(
                f"[{ManufacturerAppServiceListener.manufacturerById.__qualname__}] - response: {obj}"
            )
            response = ManufacturerAppService_manufacturerByIdResponse()
            self._addObjectToResponse(obj=obj, response=response)
            return response
        except ManufacturerDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("manufacturer does not exist")
            return ManufacturerAppService_manufacturerByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return ManufacturerAppService_manufacturerByIdResponse()

    @debugLogger
    def _addObjectToResponse(self, obj: Manufacturer, response: Any):
        response.manufacturer.id = obj.id()
        response.manufacturer.name = obj.name()

    @debugLogger
    def _token(self, context) -> str:
        metadata = context.invocation_metadata()
        if "token" in metadata[0]:
            return metadata[0].value
        return ""