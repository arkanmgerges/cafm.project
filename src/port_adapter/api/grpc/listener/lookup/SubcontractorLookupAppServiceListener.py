"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import time

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.lookup.subcontractor.SubcontractorLookup import SubcontractorLookup
from src.application.lookup.subcontractor.SubcontractorLookupApplicationService import SubcontractorLookupApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)

from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.subcontractor_lookup_app_service_pb2 import \
    SubcontractorLookupAppService_lookupResponse
from src.resource.proto._generated.subcontractor_lookup_app_service_pb2_grpc import \
    SubcontractorLookupAppServiceServicer


class SubcontractorLookupAppServiceListener(SubcontractorLookupAppServiceServicer):
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
                f"[{SubcontractorLookupAppServiceListener.lookup.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, orders: {request.orders}, filters: {request.filters}, token: {token}"
            )
            appService: SubcontractorLookupApplicationService = AppDi.instance.get(
                SubcontractorLookupApplicationService
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

            response = SubcontractorLookupAppService_lookupResponse()
            for item in result["items"]:
                response.subcontractorLookups.add(**self._kwargsByObject(item))
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{SubcontractorLookupAppServiceListener.lookup.__qualname__}] - response: {response}"
            )
            return SubcontractorLookupAppService_lookupResponse(
                subcontractorLookups=response.subcontractorLookups, totalItemCount=response.totalItemCount
            )
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Not Authorized")
            return SubcontractorLookupAppService_lookupResponse()

    def _kwargsByObject(self, instance: SubcontractorLookup) -> dict:
        return dict(map(lambda attribute: (attribute, getattr(instance, attribute, None)), SubcontractorLookup.attributes()))


    @debugLogger
    def _token(self, context) -> str:
        metadata = context.invocation_metadata()
        if "token" in metadata[0]:
            return metadata[0].value
        return ""
