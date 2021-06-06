"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import time

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.lookup.daily_check_procedure.EquipmentCategoryGroup import EquipmentCategoryGroup
from src.application.lookup.daily_check_procedure.DailyCheckProcedureOperation import DailyCheckProcedureOperation
from src.application.lookup.daily_check_procedure.DailyCheckProcedure import DailyCheckProcedure
from src.application.lookup.daily_check_procedure.DailyCheckProcedureApplicationService import DailyCheckProcedureApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)

from src.domain_model.token.TokenService import TokenService
from src.port_adapter.api.grpc.listener.BaseListener import BaseListener
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.lookup.daily_check_procedure.daily_check_procedure_app_service_pb2 import \
    DailyCheckProcedureAppService_lookupResponse
from src.resource.proto._generated.lookup.daily_check_procedure.daily_check_procedure_app_service_pb2_grpc import \
    DailyCheckProcedureAppServiceServicer
from src.resource.proto._generated.lookup.daily_check_procedure.equipment_category_group_pb2 import EquipmentCategoryGroup as ProtoEquipmentCategoryGroup
from src.resource.proto._generated.lookup.daily_check_procedure.daily_check_procedure_operation_pb2 import DailyCheckProcedureOperation as ProtoDailyCheckProcedureOperation

class DailyCheckProcedureAppServiceListener(DailyCheckProcedureAppServiceServicer, BaseListener):
    """The listener function implements the rpc call as described in the .proto file"""

    def __init__(self):
        self.counter = 0
        self.last_print_time = time.time()
        self._tokenService = TokenService()

    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def lookup(self, request, context):
        try:
            token = self._token(context)
            metadata = context.invocation_metadata()
            resultFrom = request.resultFrom if request.resultFrom >= 0 else 0
            resultSize = request.resultSize if request.resultSize >= 0 else 10
            claims = (
                self._tokenService.claimsFromToken(token=metadata[0].value)
                if "token" in metadata[0]
                else None
            )
            logger.debug(
                f"[{DailyCheckProcedureAppServiceListener.lookup.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, orders: {request.orders}, filters: {request.filters}, token: {token}"
            )
            appService: DailyCheckProcedureApplicationService = AppDi.instance.get(
                DailyCheckProcedureApplicationService
            )
            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.orders
            ]
            filterData = [
                {"key": o.key, "value": o.value} for o in request.filters
            ]
            result: dict = appService.lookup(
                resultFrom=resultFrom,
                resultSize=resultSize,
                token=token,
                orders=orderData,
                filters=filterData,
            )

            response = DailyCheckProcedureAppService_lookupResponse()
            for item in result["items"]:
                response.daily_check_procedures.add(**self._kwargsByObject(item))
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{DailyCheckProcedureAppServiceListener.lookup.__qualname__}] - response: {response}"
            )
            return response
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Not Authorized")
            return DailyCheckProcedureAppService_lookupResponse()

    def _kwargsByObject(self, instance: DailyCheckProcedure) -> dict:
        kwargs = {}
        for modelAttributeKey, lookupModelAttribute in DailyCheckProcedure.attributes().items():
            modelAttributeParameter = Util.snakeCaseToLowerCameCaseString(modelAttributeKey)
            modelValue = getattr(instance, modelAttributeParameter, None)
            if lookupModelAttribute.isClass:
                lowerCamelCaseAttributes = {}
                if modelValue is not None:
                    lowerCamelCaseAttributes = dict((Util.snakeCaseToLowerCameCaseString(key), value) for key, value in
                                                    modelValue.toMap().items())
                kwargs[modelAttributeParameter] = self._lookupModelDataTypeToGrpcType(lookupModelAttribute.dataType)(
                    **lowerCamelCaseAttributes)
            else:
                kwargs[modelAttributeParameter] = modelValue
        return kwargs

    def _lookupModelDataTypeToGrpcType(self, modelDataType):
        mapping = {
            EquipmentCategoryGroup: ProtoEquipmentCategoryGroup,
            DailyCheckProcedureOperation: ProtoDailyCheckProcedureOperation,
        }

        return mapping[modelDataType] if modelDataType in mapping else None

    @debugLogger
    def _token(self, context) -> str:
        return super()._token(context=context)
