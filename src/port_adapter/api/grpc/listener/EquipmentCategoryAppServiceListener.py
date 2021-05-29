"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import time
from typing import Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.EquipmentCategoryApplicationService import (
    EquipmentCategoryApplicationService,
)
from src.domain_model.project.equipment.category.EquipmentCategory import (
    EquipmentCategory,
)
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.domain_model.resource.exception.EquipmentCategoryDoesNotExistException import (
    EquipmentCategoryDoesNotExistException,
)
from src.domain_model.token.TokenService import TokenService
from src.port_adapter.api.grpc.listener.BaseListener import BaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.equipment_category_app_service_pb2 import (
    EquipmentCategoryAppService_equipmentCategoriesResponse,
    EquipmentCategoryAppService_equipmentCategoryByIdResponse,
    EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse,
    EquipmentCategoryAppService_newIdResponse,
)
from src.resource.proto._generated.equipment_category_app_service_pb2_grpc import (
    EquipmentCategoryAppServiceServicer,
)


class EquipmentCategoryAppServiceListener(EquipmentCategoryAppServiceServicer, BaseListener):
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
                f"[{EquipmentCategoryAppServiceListener.newId.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
                    token: {token}"
            )
            appService: EquipmentCategoryApplicationService = AppDi.instance.get(
                EquipmentCategoryApplicationService
            )
            return EquipmentCategoryAppService_newIdResponse(id=appService.newId())
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return EquipmentCategoryAppService_newIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipmentCategories(self, request, context):
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
                f"[{EquipmentCategoryAppServiceListener.equipmentCategories.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            equipmentCategoryAppService: EquipmentCategoryApplicationService = (
                AppDi.instance.get(EquipmentCategoryApplicationService)
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = equipmentCategoryAppService.equipmentCategories(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
            )
            response = EquipmentCategoryAppService_equipmentCategoriesResponse()
            for item in result["items"]:
                response.equipmentCategories.add(
                    id=item.id(),
                    name=item.name(),
                )
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{EquipmentCategoryAppServiceListener.equipmentCategories.__qualname__}] - response: {response}"
            )
            return EquipmentCategoryAppService_equipmentCategoriesResponse(
                equipmentCategories=response.equipmentCategories,
                totalItemCount=response.totalItemCount,
            )
        except EquipmentCategoryDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No equipmentCategories found")
            return EquipmentCategoryAppService_equipmentCategoriesResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return EquipmentCategoryAppService_equipmentCategoriesResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipmentCategoryById(self, request, context):
        try:
            token = self._token(context)
            appService: EquipmentCategoryApplicationService = AppDi.instance.get(
                EquipmentCategoryApplicationService
            )
            obj: EquipmentCategory = appService.equipmentCategoryById(
                id=request.id, token=token
            )
            logger.debug(
                f"[{EquipmentCategoryAppServiceListener.equipmentCategoryById.__qualname__}] - response: {obj}"
            )
            response = EquipmentCategoryAppService_equipmentCategoryByIdResponse()
            self._addObjectToResponse(obj=obj, response=response)
            return response
        except EquipmentCategoryDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("equipment category does not exist")
            return EquipmentCategoryAppService_equipmentCategoryByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return EquipmentCategoryAppService_equipmentCategoryByIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipmentCategoryGroupsByCategoryId(self, request, context):
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
                f"[{EquipmentCategoryAppServiceListener.equipmentCategoryGroupsByCategoryId.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
        resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            appService: EquipmentCategoryApplicationService = AppDi.instance.get(
                EquipmentCategoryApplicationService
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = appService.equipmentCategoryGroupsByCategoryId(
                id=request.id,
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
            )
            response = (
                EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse()
            )
            for item in result["items"]:
                response.equipmentCategoryGroups.add(
                    id=item.id(),
                    name=item.name(),
                    equipmentCategoryId=item.equipmentCategoryId(),
                )
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{EquipmentCategoryAppServiceListener.equipmentCategoryGroupsByCategoryId.__qualname__}] - response: {response}"
            )
            return (
                EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse(
                    equipmentCategoryGroups=response.equipmentCategoryGroups,
                    totalItemCount=response.totalItemCount,
                )
            )
        except EquipmentCategoryDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No equipmentCategory found")
            return (
                EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse()
            )
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return (
                EquipmentCategoryAppService_equipmentCategoryGroupsByCategoryIdResponse()
            )

    @debugLogger
    def _addObjectToResponse(self, obj: EquipmentCategory, response: Any):
        response.equipmentCategory.id = obj.id()
        response.equipmentCategory.name = obj.name()

    @debugLogger
    def _token(self, context) -> str:
        return super()._token(context=context)
