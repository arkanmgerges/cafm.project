"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import time
from typing import Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.EquipmentModelApplicationService import (
    EquipmentModelApplicationService,
)
from src.domain_model.project.equipment.model.EquipmentModel import EquipmentModel
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.domain_model.resource.exception.EquipmentModelDoesNotExistException import (
    EquipmentModelDoesNotExistException,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.equipment_model_app_service_pb2 import (
    EquipmentModelAppService_equipmentModelsResponse,
    EquipmentModelAppService_equipmentModelByIdResponse,
    EquipmentModelAppService_newIdResponse,
)
from src.resource.proto._generated.equipment_model_app_service_pb2_grpc import (
    EquipmentModelAppServiceServicer,
)


class EquipmentModelAppServiceListener(EquipmentModelAppServiceServicer):
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
                f"[{EquipmentModelAppServiceListener.newId.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
                    token: {token}"
            )
            appService: EquipmentModelApplicationService = AppDi.instance.get(
                EquipmentModelApplicationService
            )
            return EquipmentModelAppService_newIdResponse(id=appService.newId())
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return EquipmentModelAppService_newIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipmentModels(self, request, context):
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
                f"[{EquipmentModelAppServiceListener.equipmentModels.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            equipmentModelAppService: EquipmentModelApplicationService = (
                AppDi.instance.get(EquipmentModelApplicationService)
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = equipmentModelAppService.equipmentModels(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
            )
            response = EquipmentModelAppService_equipmentModelsResponse()
            for item in result["items"]:
                response.equipmentModels.add(
                    id=item.id(),
                    name=item.name(),
                )
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{EquipmentModelAppServiceListener.equipmentModels.__qualname__}] - response: {response}"
            )
            return EquipmentModelAppService_equipmentModelsResponse(
                equipmentModels=response.equipmentModels, totalItemCount=response.totalItemCount
            )
        except EquipmentModelDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No equipmentModels found")
            return EquipmentModelAppService_equipmentModelsResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return EquipmentModelAppService_equipmentModelsResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipmentModelById(self, request, context):
        try:
            token = self._token(context)
            appService: EquipmentModelApplicationService = AppDi.instance.get(
                EquipmentModelApplicationService
            )
            obj: EquipmentModel = appService.equipmentModelById(
                id=request.id, token=token
            )
            logger.debug(
                f"[{EquipmentModelAppServiceListener.equipmentModelById.__qualname__}] - response: {obj}"
            )
            response = EquipmentModelAppService_equipmentModelByIdResponse()
            self._addObjectToResponse(obj=obj, response=response)
            return response
        except EquipmentModelDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("equipment model does not exist")
            return EquipmentModelAppService_equipmentModelByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return EquipmentModelAppService_equipmentModelByIdResponse()

    @debugLogger
    def _addObjectToResponse(self, obj: EquipmentModel, response: Any):
        response.equipmentModel.id = obj.id()
        response.equipmentModel.name = obj.name()

    @debugLogger
    def _token(self, context) -> str:
        metadata = context.invocation_metadata()
        if "token" in metadata[0]:
            return metadata[0].value
        return ""
