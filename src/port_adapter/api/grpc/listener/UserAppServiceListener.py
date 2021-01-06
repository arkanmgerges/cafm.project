"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import time

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.UserApplicationService import UserApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.domain_model.resource.exception.UserDoesNotExistException import UserDoesNotExistException
from src.domain_model.token.TokenService import TokenService
from src.domain_model.user.User import User
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.user_app_service_pb2 import UserAppService_userByEmailResponse, \
    UserAppService_usersResponse, UserAppService_userByIdResponse
from src.resource.proto._generated.user_app_service_pb2_grpc import UserAppServiceServicer


class UserAppServiceListener(UserAppServiceServicer):
    """The listener function implements the rpc call as described in the .proto file"""

    def __init__(self):
        self.counter = 0
        self.last_print_time = time.time()
        self._tokenService = TokenService()

    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def userByEmail(self, request, context):
        try:
            token = self._token(context)
            userAppService: UserApplicationService = AppDi.instance.get(UserApplicationService)
            user: User = userAppService.userByEmail(email=request.email, token=token)
            response = UserAppService_userByEmailResponse()
            response.user.id = user.id()
            response.user.email = user.email()
            response.user.firstName = user.firstName()
            response.user.lastName = user.lastName()
            response.user.addressOne = user.addressOne()
            response.user.addressTwo = user.addressTwo()
            response.user.postalCode = user.postalCode()
            response.user.avatarImage = user.avatarImage()
            return response
        except UserDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User does not exist')
            return UserAppService_userByEmailResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return UserAppService_userByEmailResponse()
        # except Exception as e:
        #     context.set_code(grpc.StatusCode.UNKNOWN)
        #     context.set_details(f'{e}')
        #     return identity_pb2.UserResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def users(self, request, context):
        try:
            token = self._token(context)
            metadata = context.invocation_metadata()
            resultSize = request.resultSize if request.resultSize > 0 else 10
            claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
            logger.debug(
                f'[{UserAppServiceListener.users.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}')
            userAppService: UserApplicationService = AppDi.instance.get(UserApplicationService)

            orderData = [{"orderBy": o.orderBy, "direction": o.direction} for o in request.order]
            result: dict = userAppService.users(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData)
            response = UserAppService_usersResponse()
            for user in result['items']:
                response.users.add(id=user.id(), email=user.email(), firstName=user.firstName(),
                                   lastName=user.lastName(), addressOne=user.addressOne(),
                                   addressTwo=user.addressTwo(), postalCode=user.postalCode(),
                                   avatarImage=user.avatarImage())
            response.itemCount = result['itemCount']
            logger.debug(f'[{UserAppServiceListener.users.__qualname__}] - response: {response}')
            return UserAppService_usersResponse(users=response.users, itemCount=response.itemCount)
        except UserDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('No users found')
            return UserAppService_usersResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return UserAppService_usersResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def userById(self, request, context):
        try:
            token = self._token(context)
            userAppService: UserApplicationService = AppDi.instance.get(UserApplicationService)
            user: User = userAppService.userById(id=request.id, token=token)
            logger.debug(f'[{UserAppServiceListener.userById.__qualname__}] - response: {user}')
            response = UserAppService_userByIdResponse()
            response.user.id = user.id()
            response.user.email = user.email()
            response.user.firstName = user.firstName()
            response.user.lastName = user.lastName()
            response.user.addressOne = user.addressOne()
            response.user.addressTwo = user.addressTwo()
            response.user.postalCode = user.postalCode()
            response.user.avatarImage = user.avatarImage()
            return response
        except UserDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User does not exist')
            return UserAppService_userByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return UserAppService_userByIdResponse()

    @debugLogger
    def _token(self, context) -> str:
        metadata = context.invocation_metadata()
        if 'token' in metadata[0]:
            return metadata[0].value
        return ''
