"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import time
from typing import Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.EquipmentInputApplicationService import EquipmentInputApplicationService
from src.domain_model.project.equipment.input.EquipmentInput import EquipmentInput
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.domain_model.resource.exception.EquipmentInputDoesNotExistException import EquipmentInputDoesNotExistException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.equipment_input_app_service_pb2 import \
    EquipmentInputAppService_equipmentInputsResponse, \
    EquipmentInputAppService_equipmentInputByIdResponse, EquipmentInputAppService_newIdResponse, \
    EquipmentInputAppService_equipmentInputsByEquipmentIdResponse
from src.resource.proto._generated.equipment_input_app_service_pb2_grpc import EquipmentInputAppServiceServicer


class EquipmentInputAppServiceListener(EquipmentInputAppServiceServicer):
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
            claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
            logger.debug(
                f'[{EquipmentInputAppServiceListener.newId.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
                    token: {token}')
            appService: EquipmentInputApplicationService = AppDi.instance.get(EquipmentInputApplicationService)
            return EquipmentInputAppService_newIdResponse(id=appService.newId())
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return EquipmentInputAppService_newIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipmentInputs(self, request, context):
        try:
            token = self._token(context)
            metadata = context.invocation_metadata()
            resultSize = request.resultSize if request.resultSize >= 0 else 10
            claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
            logger.debug(
                f'[{EquipmentInputAppServiceListener.equipmentInputs.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}')
            equipmentInputAppService: EquipmentInputApplicationService = AppDi.instance.get(EquipmentInputApplicationService)

            orderData = [{"orderBy": o.orderBy, "direction": o.direction} for o in request.order]
            result: dict = equipmentInputAppService.equipmentInputs(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData)
            response = EquipmentInputAppService_equipmentInputsResponse()
            for item in result['items']:
                response.equipmentInputs.add(id=item.id(),
                                           name=item.name(),
                                           value=item.value(),
                                           unitId=item.unitId(),
                                           equipmentId=item.equipmentId(),
                                           )
            response.itemCount = result['itemCount']
            logger.debug(f'[{EquipmentInputAppServiceListener.equipmentInputs.__qualname__}] - response: {response}')
            return EquipmentInputAppService_equipmentInputsResponse(equipmentInputs=response.equipmentInputs,
                                                                itemCount=response.itemCount)
        except EquipmentInputDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('No equipmentInputs found')
            return EquipmentInputAppService_equipmentInputsResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return EquipmentInputAppService_equipmentInputsResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipmentInputsByEquipmentId(self, request, context):
        try:
            token = self._token(context)
            metadata = context.invocation_metadata()
            resultSize = request.resultSize if request.resultSize >= 0 else 10
            claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
            logger.debug(
                f'[{EquipmentInputAppServiceListener.equipmentInputsByEquipmentId.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}')
            equipmentInputAppService: EquipmentInputApplicationService = AppDi.instance.get(EquipmentInputApplicationService)

            orderData = [{"orderBy": o.orderBy, "direction": o.direction} for o in request.order]
            result: dict = equipmentInputAppService.equipmentInputsByEquipmentId(
                equipmentId=request.equipmentId,
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData)
            response = EquipmentInputAppService_equipmentInputsByEquipmentIdResponse()
            for item in result['items']:
                response.equipmentInputs.add(id=item.id(),
                                           name=item.name(),
                                           value=item.value(),
                                           unitId=item.unitId(),
                                           equipmentId=item.equipmentId(),
                                           )
            response.itemCount = result['itemCount']
            logger.debug(f'[{EquipmentInputAppServiceListener.equipmentInputsByEquipmentId.__qualname__}] - response: {response}')
            return EquipmentInputAppService_equipmentInputsByEquipmentIdResponse(equipmentInputs=response.equipmentInputs,
                                                                itemCount=response.itemCount)
        except EquipmentInputDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('No equipmentInputs found')
            return EquipmentInputAppService_equipmentInputsByEquipmentIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return EquipmentInputAppService_equipmentInputsByEquipmentIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipmentInputById(self, request, context):
        try:
            token = self._token(context)
            appService: EquipmentInputApplicationService = AppDi.instance.get(EquipmentInputApplicationService)
            obj: EquipmentInput = appService.equipmentInputById(id=request.id, token=token)
            logger.debug(f'[{EquipmentInputAppServiceListener.equipmentInputById.__qualname__}] - response: {obj}')
            response = EquipmentInputAppService_equipmentInputByIdResponse()
            self._addObjectToResponse(obj=obj, response=response)
            return response
        except EquipmentInputDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('equipment input does not exist')
            return EquipmentInputAppService_equipmentInputByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return EquipmentInputAppService_equipmentInputByIdResponse()

    @debugLogger
    def _addObjectToResponse(self, obj: EquipmentInput, response: Any):
        response.equipmentInput.id = obj.id()
        response.equipmentInput.name = obj.name()
        response.equipmentInput.value = obj.value()
        response.equipmentInput.unitId = obj.unitId()
        response.equipmentInput.equipmentId = obj.equipmentId()

    @debugLogger
    def _token(self, context) -> str:
        metadata = context.invocation_metadata()
        if 'token' in metadata[0]:
            return metadata[0].value
        return ''
