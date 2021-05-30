"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import time
from typing import Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.UserApplicationService import UserApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.domain_model.resource.exception.UserDoesNotExistException import (
    UserDoesNotExistException,
)
from src.domain_model.token.TokenService import TokenService
from src.port_adapter.api.grpc.listener.BaseListener import BaseListener
from src.domain_model.user.User import User
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.user_app_service_pb2 import (
    UserAppService_userByEmailResponse,
    UserAppService_usersResponse,
    UserAppService_userByIdResponse,
    UserAppService_newIdResponse,
)
from src.resource.proto._generated.user_app_service_pb2_grpc import (
    UserAppServiceServicer,
)


class UserAppServiceListener(UserAppServiceServicer, BaseListener):
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
                f"[{UserAppServiceListener.newId.__qualname__}] - claims: {claims}\n\t \
                    token: {token}"
            )
            appService: UserApplicationService = AppDi.instance.get(
                UserApplicationService
            )
            return UserAppService_newIdResponse(id=appService.newId())
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return UserAppService_newIdResponse()

    """
    c4model|cb|project:Component(identity__grpc__UserAppServiceListener__userByEmail, "Get a user by email", "grpc listener", "Get a user by email")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def userByEmail(self, request, context):
        try:
            token = self._token(context)
            userAppService: UserApplicationService = AppDi.instance.get(
                UserApplicationService
            )
            user: User = userAppService.userByEmail(email=request.email, token=token)
            response = UserAppService_userByEmailResponse()
            self._addObjectToResponse(obj=user, response=response)
            return response
        except UserDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User does not exist")
            return UserAppService_userByEmailResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return UserAppService_userByEmailResponse()
        # except Exception as e:
        #     context.set_code(grpc.StatusCode.UNKNOWN)
        #     context.set_details(f'{e}')
        #     return identity_pb2.UserResponse()

    """
    c4model|cb|project:Component(identity__grpc__UserAppServiceListener__users, "Get all users", "grpc listener", "Get users")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def users(self, request, context):
        try:
            token = self._token(context)

            resultSize = request.resultSize if request.resultSize >= 0 else 10
            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{UserAppServiceListener.users.__qualname__}] - claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            userAppService: UserApplicationService = AppDi.instance.get(
                UserApplicationService
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = userAppService.users(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
            )
            response = UserAppService_usersResponse()
            for user in result["items"]:
                response.users.add(
                    id=user.id(),
                    email=user.email(),
                    firstName=user.firstName(),
                    lastName=user.lastName(),
                    addressOne=user.addressOne(),
                    addressTwo=user.addressTwo(),
                    postalCode=user.postalCode(),
                    phoneNumber=user.phoneNumber(),
                    avatarImage=user.avatarImage(),
                    countryId=user.countryId(),
                    cityId=user.cityId(),
                    stateId=user.stateId(),
                    countryStateName=user.countryStateName(),
                    startDate=user.startDate() if user.startDate() is not None else 0,
                )
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{UserAppServiceListener.users.__qualname__}] - response: {response}"
            )
            return UserAppService_usersResponse(
                users=response.users, totalItemCount=response.totalItemCount
            )
        except UserDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No users found")
            return UserAppService_usersResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return UserAppService_usersResponse()

    """
    c4model|cb|project:Component(identity__grpc__UserAppServiceListener__userById, "Get a user by id", "grpc listener", "Get a user by id")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def userById(self, request, context):
        try:
            token = self._token(context)
            userAppService: UserApplicationService = AppDi.instance.get(
                UserApplicationService
            )
            user: User = userAppService.userById(id=request.id, token=token)
            logger.debug(
                f"[{UserAppServiceListener.userById.__qualname__}] - response: {user}"
            )
            response = UserAppService_userByIdResponse()
            self._addObjectToResponse(obj=user, response=response)
            return response
        except UserDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User does not exist")
            return UserAppService_userByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return UserAppService_userByIdResponse()

    @debugLogger
    def _addObjectToResponse(self, obj: User, response: Any):
        response.user.id = obj.id()
        response.user.email = obj.email() if obj.email() is not None else ""
        response.user.firstName = obj.firstName() if obj.firstName() is not None else ""
        response.user.lastName = obj.lastName() if obj.lastName() is not None else ""
        response.user.addressOne = (
            obj.addressOne() if obj.addressOne() is not None else ""
        )
        response.user.addressTwo = (
            obj.addressTwo() if obj.addressTwo() is not None else ""
        )
        response.user.postalCode = (
            obj.postalCode() if obj.postalCode() is not None else ""
        )
        response.user.phoneNumber = (
            obj.phoneNumber() if obj.phoneNumber() is not None else ""
        )
        response.user.avatarImage = (
            obj.avatarImage() if obj.avatarImage() is not None else ""
        )
        response.user.countryId = obj.countryId()
        response.user.cityId = obj.cityId()
        response.user.stateId = obj.stateId() if obj.stateId() is not None else ""
        response.user.countryStateName = (
            obj.countryStateName() if obj.countryStateName() is not None else ""
        )
        response.user.startDate = obj.startDate() if obj.startDate() is not None else 0

    @debugLogger
    def _token(self, context) -> str:
        return super()._token(context=context)
