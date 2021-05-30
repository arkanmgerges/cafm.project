"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import time
from typing import Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.OrganizationApplicationService import (
    OrganizationApplicationService,
)
from src.domain_model.organization.Organization import Organization
from src.domain_model.resource.exception.OrganizationDoesNotExistException import (
    OrganizationDoesNotExistException,
)
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.domain_model.resource.exception.UserDoesNotExistException import (
    UserDoesNotExistException,
)
from src.domain_model.token.TokenService import TokenService
from src.port_adapter.api.grpc.listener.BaseListener import BaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.organization_app_service_pb2 import (
    OrganizationAppService_organizationsResponse,
    OrganizationAppService_organizationByIdResponse,
    OrganizationAppService_newIdResponse,
)
from src.resource.proto._generated.organization_app_service_pb2_grpc import (
    OrganizationAppServiceServicer,
)


class OrganizationAppServiceListener(OrganizationAppServiceServicer, BaseListener):
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

            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{OrganizationAppServiceListener.newId.__qualname__}] - claims: {claims}\n\t \
                    token: {token}"
            )
            appService: OrganizationApplicationService = AppDi.instance.get(
                OrganizationApplicationService
            )
            return OrganizationAppService_newIdResponse(id=appService.newId())
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return OrganizationAppService_newIdResponse()

    """
    c4model|cb|project:Component(identity__grpc__OrganizationAppServiceListener__organizations, "Get organizations", "grpc listener", "Get all organizations")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def organizations(self, request, context):
        try:
            token = self._token(context)

            resultSize = request.resultSize if request.resultSize >= 0 else 10
            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{OrganizationAppServiceListener.organizations.__qualname__}] - claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            appService: OrganizationApplicationService = AppDi.instance.get(
                OrganizationApplicationService
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = appService.organizations(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
            )
            response = OrganizationAppService_organizationsResponse()
            for organization in result["items"]:
                response.organizations.add(
                    id=organization.id(),
                    name=organization.name(),
                    websiteUrl=organization.websiteUrl(),
                    organizationType=organization.organizationType(),
                    addressOne=organization.addressOne(),
                    addressTwo=organization.addressTwo(),
                    postalCode=organization.postalCode(),
                    countryId=organization.countryId(),
                    cityId=organization.cityId(),
                    countryStateName=organization.countryStateName(),
                    managerFirstName=organization.managerFirstName(),
                    managerLastName=organization.managerLastName(),
                    managerEmail=organization.managerEmail(),
                    managerPhoneNumber=organization.managerPhoneNumber(),
                    managerAvatar=organization.managerAvatar(),
                )
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{OrganizationAppServiceListener.organizations.__qualname__}] - response: {response}"
            )
            return response
        except UserDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No organizations found")
            return OrganizationAppService_organizationsResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return OrganizationAppService_organizationsResponse()

    """
    c4model|cb|project:Component(identity__grpc__OrganizationAppServiceListener__organizationById, "Get organization by id", "grpc listener", "Get a organization by id")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def organizationById(self, request, context):
        try:
            token = self._token(context)
            appService: OrganizationApplicationService = AppDi.instance.get(
                OrganizationApplicationService
            )
            obj: Organization = appService.organizationById(id=request.id, token=token)
            logger.debug(
                f"[{OrganizationAppServiceListener.organizationById.__qualname__}] - response: {obj}"
            )
            response = OrganizationAppService_organizationByIdResponse()
            self._addObjectToResponse(obj=obj, response=response)
            return response
        except OrganizationDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Organization does not exist")
            return OrganizationAppService_organizationByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return OrganizationAppService_organizationByIdResponse()

    @debugLogger
    def _addObjectToResponse(self, obj: Organization, response: Any):
        response.organization.id = obj.id()
        response.organization.name = obj.name() if obj.name() is not None else ""
        response.organization.websiteUrl = obj.websiteUrl() if obj.websiteUrl() is not None else ""
        response.organization.organizationType = obj.organizationType() if obj.organizationType() is not None else ""
        response.organization.addressOne = obj.addressOne() if obj.addressOne() is not None else ""
        response.organization.addressTwo = obj.addressTwo() if obj.addressTwo() is not None else ""
        response.organization.postalCode = obj.postalCode() if obj.postalCode() is not None else ""
        response.organization.countryId = obj.countryId()
        response.organization.cityId = obj.cityId()
        response.organization.countryStateName = obj.countryStateName() if obj.countryStateName() is not None else ""
        response.organization.managerFirstName = obj.managerFirstName() if obj.managerFirstName() is not None else ""
        response.organization.managerLastName = obj.managerLastName()  if obj.managerLastName() is not None else ""
        response.organization.managerEmail = obj.managerEmail()  if obj.managerEmail() is not None else ""
        response.organization.managerPhoneNumber = obj.managerPhoneNumber() if obj.managerPhoneNumber() is not None else ""
        response.organization.managerAvatar = obj.managerAvatar() if obj.managerAvatar() is not None else ""

    @debugLogger
    def _token(self, context) -> str:
        return super()._token(context=context)
