"""
@author: Mohammad S. moso<moso@develoop.run>
"""
import time
from typing import Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.SubcontractorApplicationService import SubcontractorApplicationService
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.resource.exception.SubcontractorDoesNotExistException import SubcontractorDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.domain_model.resource.exception.UserDoesNotExistException import UserDoesNotExistException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.subcontractor_app_service_pb2 import SubcontractorAppService_subcontractorsResponse, \
    SubcontractorppService_subcontractorByIdResponse, SubcontractorAppService_newIdResponse
from src.resource.proto._generated.subcontractor_app_service_pb2_grpc import SubcontractorAppServiceServicer


class SubcontractorAppServiceListener(SubcontractorAppServiceServicer):
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
                f'[{SubcontractorAppServiceListener.newId.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
                    token: {token}')
            appService: SubcontractorApplicationService = AppDi.instance.get(SubcontractorApplicationService)
            return SubcontractorAppService_newIdResponse(id=appService.newId())
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return SubcontractorAppService_newIdResponse()

    """
    c4model|cb|project:Component(identity__grpc__SubcontractorAppServiceListener__subcontractors, "Get subcontractors", "grpc listener", "Get all subcontractors")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def subcontractors(self, request, context):
        try:
            token = self._token(context)
            metadata = context.invocation_metadata()
            resultSize = request.resultSize if request.resultSize >= 0 else 10
            claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
            logger.debug(
                f'[{SubcontractorAppServiceListener.subcontractors.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
        resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}')
            appService: SubcontractorApplicationService = AppDi.instance.get(SubcontractorApplicationService)

            orderData = [{"orderBy": o.orderBy, "direction": o.direction} for o in request.order]
            result: dict = appService.subcontractors(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData)
            response = SubcontractorAppService_subcontractorsResponse()
            for subcontractor in result['items']:
                response.subcontractors.add(id=subcontractor.id(),
                                            companyName=subcontractor.companyName(),
                                            websiteUrl=subcontractor.websiteUrl(),
                                            contactPerson=subcontractor.contactPerson(),
                                            email=subcontractor.email(),
                                            phoneNumber=subcontractor.phoneNumber(),
                                            addressOne=subcontractor.addressOne(),
                                            addressTwo=subcontractor.addressTwo())
            response.itemCount = result['itemCount']
            logger.debug(f'[{SubcontractorAppServiceListener.subcontractors.__qualname__}] - response: {response}')
            return SubcontractorAppService_subcontractorsResponse(subcontractors=response.subcontractors,
                                                                  itemCount=response.itemCount)
        except UserDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('No subcontractors found')
            return SubcontractorAppService_subcontractorsResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return SubcontractorAppService_subcontractorsResponse()

    """
    c4model|cb|project:Component(identity__grpc__SubcontractorAppServiceListener__subcontractorById, "Get subcontractor by id", "grpc listener", "Get a subcontractor by id")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def subcontractorById(self, request, context):
        try:
            token = self._token(context)
            appService: SubcontractorApplicationService = AppDi.instance.get(SubcontractorApplicationService)
            obj: Subcontractor = appService.subcontractorById(id=request.id, token=token)
            logger.debug(f'[{SubcontractorAppServiceListener.subcontractorById.__qualname__}] - response: {obj}')
            response = SubcontractorppService_subcontractorByIdResponse()
            self._addObjectToResponse(obj=obj, response=response)
            return response
        except SubcontractorDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('subcontractor does not exist')
            return SubcontractorppService_subcontractorByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return SubcontractorppService_subcontractorByIdResponse()

    @debugLogger
    def _addObjectToResponse(self, obj: Subcontractor, response: Any):
        response.subcontractor.id = obj.id()
        response.subcontractor.companyName = obj.companyName()
        response.subcontractor.websiteUrl = obj.websiteUrl()
        response.subcontractor.contactPerson = obj.contactPerson()
        response.subcontractor.email = obj.email()
        response.subcontractor.phoneNumber = obj.phoneNumber()
        response.subcontractor.addressOne = obj.addressOne()
        response.subcontractor.addressTwo = obj.addressTwo()

    @debugLogger
    def _token(self, context) -> str:
        metadata = context.invocation_metadata()
        if 'token' in metadata[0]:
            return metadata[0].value
        return ''
