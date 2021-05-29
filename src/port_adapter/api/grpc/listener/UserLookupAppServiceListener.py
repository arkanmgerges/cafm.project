"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import time
from typing import Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.UserLookupApplicationService import UserLookupApplicationService
from src.application.user_lookup.UserLookup import UserLookup
from src.domain_model.organization.Organization import Organization
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.domain_model.resource.exception.UserDoesNotExistException import (
    UserDoesNotExistException,
)
from src.domain_model.role.Role import Role
from src.domain_model.token.TokenService import TokenService
from src.port_adapter.api.grpc.listener.BaseListener import BaseListener
from src.domain_model.user.User import User
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.user_lookup_app_service_pb2 import (
    UserLookupAppService_userLookupByUserIdResponse,
    UserLookupAppService_userLookupsResponse,
)
from src.resource.proto._generated.user_lookup_app_service_pb2_grpc import (
    UserLookupAppServiceServicer,
)


class UserLookupAppServiceListener(UserLookupAppServiceServicer, BaseListener):
    """The listener function implements the rpc call as described in the .proto file"""

    def __init__(self):
        self.counter = 0
        self.last_print_time = time.time()
        self._tokenService = TokenService()

    def __str__(self):
        return self.__class__.__name__

    """
    c4model|cb|project:Component(identity__grpc__UserLookupAppServiceListener__userLookupByUserEmail, "Get a user lookup by email", "grpc listener", "Get a user lookup by email")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def userLookupByUserEmail(self, request, context):
        try:
            token = self._token(context)
            userLookupAppService: UserLookupApplicationService = AppDi.instance.get(
                UserLookupApplicationService
            )
            userLookup: UserLookup = userLookupAppService.userLookupByUserEmail(
                email=request.email, token=token
            )

            logger.debug(
                f"[{UserLookupAppServiceListener.userLookupByUserId.__qualname__}] - response: {userLookup}"
            )
            response = UserLookupAppService_userLookupByUserIdResponse()
            self._addObjectToResponse(
                userLookup=userLookup, response=response.userLookup
            )
            return response
        except UserDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User does not exist")
            return UserLookupAppService_userLookupByUserIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return UserLookupAppService_userLookupByUserIdResponse()

    """
    c4model|cb|project:Component(identity__grpc__UserLookupAppServiceListener__userLookupByUserId, "Get a user lookup by id", "grpc listener", "Get a user lookup by id")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def userLookupByUserId(self, request, context):
        try:
            token = self._token(context)
            userLookupAppService: UserLookupApplicationService = AppDi.instance.get(
                UserLookupApplicationService
            )
            userLookup: UserLookup = userLookupAppService.userLookupByUserId(
                id=request.id, token=token
            )

            logger.debug(
                f"[{UserLookupAppServiceListener.userLookupByUserId.__qualname__}] - response: {userLookup}"
            )
            response = UserLookupAppService_userLookupByUserIdResponse()
            self._addObjectToResponse(
                userLookup=userLookup, response=response.userLookup
            )
            return response
        except UserDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User does not exist")
            return UserLookupAppService_userLookupByUserIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return UserLookupAppService_userLookupByUserIdResponse()

    """
    c4model|cb|project:Component(identity__grpc__UserLookupAppServiceListener__userLookups, "Get a user lookups", "grpc listener", "Get user lookups")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def userLookups(self, request, context):
        try:
            token = self._token(context)
            userLookupAppService: UserLookupApplicationService = AppDi.instance.get(
                UserLookupApplicationService
            )

            resultSize = request.resultSize if request.resultSize >= 0 else 10
            logger.debug(
                f"[{UserLookupAppServiceListener.userLookupByUserId.__qualname__}] - resultFrom: {request.resultFrom}, resultSize: {resultSize}"
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            userLookupsDict: dict = userLookupAppService.userLookups(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
            )
            response = UserLookupAppService_userLookupsResponse()

            response.totalItemCount = userLookupsDict["totalItemCount"]
            for userLookup in userLookupsDict["items"]:
                responseItem = response.userLookups.add()
                self._addObjectToResponse(userLookup=userLookup, response=responseItem)
            return response
        except UserDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User does not exist")
            return UserLookupAppService_userLookupByUserIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return UserLookupAppService_userLookupByUserIdResponse()

    @debugLogger
    def _addObjectToResponse(self, userLookup: UserLookup, response: Any):
        self._addUserObjectToResponse(obj=userLookup.user(), response=response.user)
        for role in userLookup.roles():
            self._addRoleObjectToRolesResponse(obj=role, response=response)

        for org in userLookup.organizations():
            self._addOrganizationObjectToOrganizationsResponse(
                obj=org, response=response
            )

    def _addRoleObjectToRolesResponse(self, obj: Role, response: Any):
        response.roles.add(id=obj.id(), name=obj.name())

    def _addOrganizationObjectToOrganizationsResponse(
        self, obj: Organization, response: Any
    ):
        response.organizations.add(
            id=obj.id(),
            name=obj.name() if obj.name() is not None else "",
            websiteUrl=obj.websiteUrl() if obj.websiteUrl() is not None else "",
            organizationType=obj.organizationType()
            if obj.organizationType() is not None
            else "",
            addressOne=obj.addressOne() if obj.addressOne() is not None else "",
            addressTwo=obj.addressTwo() if obj.addressTwo() is not None else "",
            postalCode=obj.postalCode() if obj.postalCode() is not None else "",
            countryId=obj.countryId() if obj.countryId() is not None else 0,
            cityId=obj.cityId() if obj.cityId() is not None else 0,
            countryStateName=obj.countryStateName()
            if obj.countryStateName() is not None
            else "",
            managerFirstName=obj.managerFirstName()
            if obj.managerFirstName() is not None
            else "",
            managerLastName=obj.managerLastName()
            if obj.managerLastName() is not None
            else "",
            managerEmail=obj.managerEmail() if obj.managerEmail() is not None else "",
            managerPhoneNumber=obj.managerPhoneNumber()
            if obj.managerPhoneNumber() is not None
            else "",
            managerAvatar=obj.managerAvatar()
            if obj.managerAvatar() is not None
            else "",
        )

    def _addUserObjectToResponse(self, obj: User, response: Any):
        response.id = obj.id()
        response.email = obj.email() if obj.email() is not None else ""
        response.firstName = obj.firstName() if obj.firstName() is not None else ""
        response.lastName = obj.lastName() if obj.lastName() is not None else ""
        response.addressOne = obj.addressOne() if obj.addressOne() is not None else ""
        response.addressTwo = obj.addressTwo() if obj.addressTwo() is not None else ""
        response.postalCode = obj.postalCode() if obj.postalCode() is not None else ""
        response.phoneNumber = (
            obj.phoneNumber() if obj.phoneNumber() is not None else ""
        )
        response.avatarImage = (
            obj.avatarImage() if obj.avatarImage() is not None else ""
        )
        response.countryId = obj.countryId() if obj.countryId() is not None else 0
        response.cityId = obj.cityId() if obj.cityId() is not None else 0
        response.stateId = obj.stateId() if obj.stateId() is not None else ""
        response.countryStateName = (
            obj.countryStateName() if obj.countryStateName() is not None else ""
        )
        response.startDate = obj.startDate() if obj.startDate() is not None else 0

    @debugLogger
    def _token(self, context) -> str:
        return super()._token(context=context)
