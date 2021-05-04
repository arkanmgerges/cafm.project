"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import time
from typing import Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.EquipmentProjectCategoryApplicationService import (
    EquipmentProjectCategoryApplicationService,
)
from src.domain_model.project.equipment.project_category.EquipmentProjectCategory import (
    EquipmentProjectCategory,
)
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.domain_model.resource.exception.EquipmentProjectCategoryDoesNotExistException import (
    EquipmentProjectCategoryDoesNotExistException,
)
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.equipment_project_category_app_service_pb2 import (
    EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse,
    EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse,
    EquipmentProjectCategoryAppService_equipmentCategoryGroupsByProjectCategoryIdResponse,
    EquipmentProjectCategoryAppService_newIdResponse,
)
from src.resource.proto._generated.equipment_project_category_app_service_pb2_grpc import (
    EquipmentProjectCategoryAppServiceServicer,
)


class EquipmentProjectCategoryAppServiceListener(
    EquipmentProjectCategoryAppServiceServicer
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
                f"[{EquipmentProjectCategoryAppServiceListener.newId.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
                    token: {token}"
            )
            appService: EquipmentProjectCategoryApplicationService = AppDi.instance.get(
                EquipmentProjectCategoryApplicationService
            )
            return EquipmentProjectCategoryAppService_newIdResponse(
                id=appService.newId()
            )
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return EquipmentProjectCategoryAppService_newIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipmentProjectCategories(self, request, context):
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
                f"[{EquipmentProjectCategoryAppServiceListener.equipmentProjectCategories.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            equipmentProjectCategoryAppService: EquipmentProjectCategoryApplicationService = AppDi.instance.get(
                EquipmentProjectCategoryApplicationService
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = (
                equipmentProjectCategoryAppService.equipmentProjectCategories(
                    resultFrom=request.resultFrom,
                    resultSize=resultSize,
                    token=token,
                    order=orderData,
                )
            )
            response = (
                EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse()
            )
            for item in result["items"]:
                response.equipmentProjectCategories.add(
                    id=item.id(),
                    name=item.name(),
                )
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{EquipmentProjectCategoryAppServiceListener.equipmentProjectCategories.__qualname__}] - response: {response}"
            )
            return (
                EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse(
                    equipmentProjectCategories=response.equipmentProjectCategories,
                    totalItemCount=response.totalItemCount,
                )
            )
        except EquipmentProjectCategoryDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No equipmentProjectCategories found")
            return (
                EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse()
            )
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return (
                EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse()
            )

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipmentProjectCategoryById(self, request, context):
        try:
            token = self._token(context)
            appService: EquipmentProjectCategoryApplicationService = AppDi.instance.get(
                EquipmentProjectCategoryApplicationService
            )
            obj: EquipmentProjectCategory = appService.equipmentProjectCategoryById(
                id=request.id, token=token
            )
            logger.debug(
                f"[{EquipmentProjectCategoryAppServiceListener.equipmentProjectCategoryById.__qualname__}] - response: {obj}"
            )
            response = (
                EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse()
            )
            self._addObjectToResponse(obj=obj, response=response)
            return response
        except EquipmentProjectCategoryDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("equipment project category does not exist")
            return (
                EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse()
            )
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return (
                EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse()
            )

    def equipmentCategoryGroupsByProjectCategoryId(self, request, context):
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
                f"[{EquipmentProjectCategoryAppServiceListener.equipmentCategoryGroupsByProjectCategoryId.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
        resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            equipmentProjectCategoryAppService: EquipmentProjectCategoryApplicationService = AppDi.instance.get(
                EquipmentProjectCategoryApplicationService
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = equipmentProjectCategoryAppService.equipmentCategoryGroupsByProjectCategoryId(
                id=request.id,
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
            )
            response = (
                EquipmentProjectCategoryAppService_equipmentCategoryGroupsByProjectCategoryIdResponse()
            )
            for item in result["items"]:
                response.equipmentCategoryGroups.add(
                    id=item.id(),
                    name=item.name(),
                    equipmentCategoryId=item.equipmentCategoryId(),
                )
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{EquipmentProjectCategoryAppServiceListener.equipmentCategoryGroupsByProjectCategoryId.__qualname__}] - response: {response}"
            )
            return EquipmentProjectCategoryAppService_equipmentCategoryGroupsByProjectCategoryIdResponse(
                equipmentCategoryGroups=response.equipmentCategoryGroups,
                totalItemCount=response.totalItemCount,
            )
        except EquipmentProjectCategoryDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No equipmentProjectCategories found")
            return (
                EquipmentProjectCategoryAppService_equipmentCategoryGroupsByProjectCategoryIdResponse()
            )
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return (
                EquipmentProjectCategoryAppService_equipmentCategoryGroupsByProjectCategoryIdResponse()
            )

    @debugLogger
    def _addObjectToResponse(self, obj: EquipmentProjectCategory, response: Any):
        response.equipmentProjectCategory.id = obj.id()
        response.equipmentProjectCategory.name = obj.name()

    @debugLogger
    def _token(self, context) -> str:
        metadata = context.invocation_metadata()
        if "token" in metadata[0]:
            return metadata[0].value
        return ""
