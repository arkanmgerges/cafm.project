"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import time
from typing import Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.EquipmentApplicationService import EquipmentApplicationService
from src.domain_model.project.equipment.Equipment import Equipment
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.domain_model.resource.exception.EquipmentDoesNotExistException import EquipmentDoesNotExistException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.equipment_app_service_pb2 import EquipmentAppService_equipmentsResponse, \
    EquipmentAppService_equipmentByIdResponse, EquipmentAppService_newIdResponse
from src.resource.proto._generated.equipment_app_service_pb2_grpc import EquipmentAppServiceServicer


class EquipmentAppServiceListener(EquipmentAppServiceServicer):
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
                f'[{EquipmentAppServiceListener.newId.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
                    token: {token}')
            appService: EquipmentApplicationService = AppDi.instance.get(EquipmentApplicationService)
            return EquipmentAppService_newIdResponse(id=appService.newId())
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return EquipmentAppService_newIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipments(self, request, context):
        try:
            token = self._token(context)
            metadata = context.invocation_metadata()
            resultSize = request.resultSize if request.resultSize >= 0 else 10
            claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
            logger.debug(
                f'[{EquipmentAppServiceListener.equipments.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}')
            equipmentAppService: EquipmentApplicationService = AppDi.instance.get(EquipmentApplicationService)

            orderData = [{"orderBy": o.orderBy, "direction": o.direction} for o in request.order]
            result: dict = equipmentAppService.equipments(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData)
            response = EquipmentAppService_equipmentsResponse()
            for item in result['items']:
                response.equipments.add(id=item.id(),
                                           name=item.name(),
                                           projectId=item.projectId(),
                                           equipmentProjectCategoryId=item.equipmentProjectCategoryId(),
                                           equipmentCategoryId=item.equipmentCategoryId(),
                                           equipmentCategoryGroupId=item.equipmentCategoryGroupId(),
                                           buildingId=item.buildingId(),
                                           buildingLevelId=item.buildingLevelId(),
                                           buildingLevelRoomId=item.buildingLevelRoomId(),
                                           manufacturerId=item.manufacturerId(),
                                           equipmentModelId=item.equipmentModelId(),
                                           quantity=item.quantity(),
                                           )
            response.itemCount = result['itemCount']
            logger.debug(f'[{EquipmentAppServiceListener.equipments.__qualname__}] - response: {response}')
            return EquipmentAppService_equipmentsResponse(equipments=response.equipments,
                                                                itemCount=response.itemCount)
        except EquipmentDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('No equipments found')
            return EquipmentAppService_equipmentsResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return EquipmentAppService_equipmentsResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipmentById(self, request, context):
        try:
            token = self._token(context)
            appService: EquipmentApplicationService = AppDi.instance.get(EquipmentApplicationService)
            obj: Equipment = appService.equipmentById(id=request.id, token=token)
            logger.debug(f'[{EquipmentAppServiceListener.equipmentById.__qualname__}] - response: {obj}')
            response = EquipmentAppService_equipmentByIdResponse()
            self._addObjectToResponse(obj=obj, response=response)
            return response
        except EquipmentDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('equipment does not exist')
            return EquipmentAppService_equipmentByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return EquipmentAppService_equipmentByIdResponse()

    @debugLogger
    def _addObjectToResponse(self, obj: Equipment, response: Any):
        response.equipment.id = obj.id()
        response.equipment.name=obj.name()
        response.equipment.projectId=obj.projectId()
        response.equipment.equipmentProjectCategoryId=obj.equipmentProjectCategoryId()
        response.equipment.equipmentCategoryId=obj.equipmentCategoryId()
        response.equipment.equipmentCategoryGroupId=obj.equipmentCategoryGroupId()
        response.equipment.buildingId=obj.buildingId()
        response.equipment.buildingLevelId=obj.buildingLevelId()
        response.equipment.buildingLevelRoomId=obj.buildingLevelRoomId()
        response.equipment.manufacturerId=obj.manufacturerId()
        response.equipment.equipmentModelId=obj.equipmentModelId()
        response.equipment.quantity=obj.quantity()

    @debugLogger
    def _token(self, context) -> str:
        metadata = context.invocation_metadata()
        if 'token' in metadata[0]:
            return metadata[0].value
        return ''
