"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import grpc

from src.application.lookup.model_data.BaseLookupModel import BaseLookupModel
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.domain_model.token.TokenService import TokenService
from src.port_adapter.api.grpc.listener.BaseListener import BaseListener
from src.resource.common.Util import Util
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry


class BaseLookupListener(BaseListener):
    @debugLogger
    def __init__(self):
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
                if lookupModelAttributeData.isArray and type(modelValue) is list:
                    kwargs[snakeCaseLookupModelAttributeKey] = []
                    if modelValue is not None:
                        kwargs[snakeCaseLookupModelAttributeKey] = [self._kwargsByObject(x) for x in modelValue]
                else:
                    snakeCaseAttributes = {}
                    if modelValue is not None:
                        snakeCaseAttributes = dict(
                            (Util.camelCaseToLowerSnakeCase(key), value) for key, value in
                            modelValue.toMap().items())
                    kwargs[snakeCaseLookupModelAttributeKey] = self._lookupModelDataTypeToGrpcType(
                        lookupModelAttributeData.dataType)(
                        **snakeCaseAttributes)
            else:
                kwargs[snakeCaseLookupModelAttributeKey] = modelValue
        return kwargs