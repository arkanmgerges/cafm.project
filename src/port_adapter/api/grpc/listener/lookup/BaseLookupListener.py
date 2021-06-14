"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import abstractmethod
from datetime import datetime

import grpc

from src.application.lookup.model_data.BaseLookupModel import BaseLookupModel
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.domain_model.token.TokenService import TokenService
from src.port_adapter.api.grpc.listener.BaseListener import BaseListener
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry


class BaseLookupListener(BaseListener):
    @debugLogger
    def __init__(self):
        # This field is overwritten by the derived class
        self._responseAttribute = None
        self._appService = None
        self._tokenService = TokenService()
        super().__init__()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def lookup(self, request, context):
        try:
            token = self._token(context)

            resultFrom = request.result_from if request.result_from >= 0 else 0
            resultSize = request.result_size if request.result_size >= 0 else 10
            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{BaseLookupListener.__qualname__}] - claims: {claims}\n\t \
    result_from: {request.result_from}, result_size: {request.result_size}, orders: {request.orders}, filters: {request.filters}, token: {token}"
            )

            orderData = [
                {"orderBy": o.order_by, "direction": o.direction} for o in request.orders
            ]
            filterData = [
                {"key": o.key, "value": o.value} for o in request.filters
            ]

            result: dict = self._appService.lookup(
                resultFrom=resultFrom,
                resultSize=resultSize,
                token=token,
                orders=orderData,
                filters=filterData,
            )

            response = self._lookupResponse()
            for item in result["items"]:
                obj = getattr(response, self._responseAttribute, None)
                obj.add(**self._kwargsByObject(item))
            response.total_item_count = result["totalItemCount"]
            logger.debug(
                f"[{BaseLookupListener.__qualname__}] - response: {response}"
            )
            return response
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Not Authorized")
            return self._lookupResponse()

    def _kwargsByObject(self, instance: BaseLookupModel) -> dict:
        kwargs = {}
        for lookupModelAttributeKey, lookupModelAttributeData in instance.attributes().items():
            snakeCaseLookupModelAttributeKey = Util.camelCaseToLowerSnakeCase(lookupModelAttributeKey)
            modelValue = getattr(instance, lookupModelAttributeKey, None)
            if lookupModelAttributeData.isClass:
                if lookupModelAttributeData.isArray and isinstance(modelValue, list):
                    # Here modelValue is a list of type, lookup model
                    kwargs[snakeCaseLookupModelAttributeKey] = []
                    if modelValue is not None:
                        kwargs[snakeCaseLookupModelAttributeKey] = [self._kwargsByObject(x) for x in modelValue]
                else:
                    snakeCaseAttributes = {}
                    if modelValue is not None:
                        # Here modelValue is a lookup model object
                        snakeCaseAttributes = dict(
                            (Util.camelCaseToLowerSnakeCase(key), self._convertValueDataType(value, lookupModelAttributeData)) for key, value in
                            modelValue.toMap().items())
                    kwargs[snakeCaseLookupModelAttributeKey] = self._lookupModelDataTypeToGrpcType(
                        lookupModelAttributeData.dataType)(
                        **snakeCaseAttributes)
            else:
                kwargs[snakeCaseLookupModelAttributeKey] = self._convertValueDataType(modelValue, lookupModelAttributeData)
        return kwargs

    def _convertValueDataType(self, value, lookupModelAttributeData):
        if lookupModelAttributeData.dataType is not lookupModelAttributeData.protoDataType:
            if lookupModelAttributeData.dataType is str:
                if lookupModelAttributeData.protoDataType is float:
                    return float(value) if value is not None else 0.0
                elif lookupModelAttributeData.protoDataType is int:
                    return int(value) if value is not None else 0
            elif lookupModelAttributeData.dataType is float:
                if lookupModelAttributeData.protoDataType is str:
                    return str(value) if value is not None else "0.0"
                else:
                    return "0.0"
            elif lookupModelAttributeData.dataType is datetime:
                if lookupModelAttributeData.protoDataType is str:
                    return DateTimeHelper.datetimeToInt(value)
                else:
                    return "0"
            else:
                return value

    @abstractmethod
    def _lookupResponse(self):
        pass

    @abstractmethod
    def _lookupModelDataTypeToGrpcType(self, dataType):
        pass