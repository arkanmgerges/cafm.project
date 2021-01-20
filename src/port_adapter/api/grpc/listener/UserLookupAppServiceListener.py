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
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.domain_model.resource.exception.UserDoesNotExistException import UserDoesNotExistException
from src.domain_model.role.Role import Role
from src.domain_model.token.TokenService import TokenService
from src.domain_model.user.User import User
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.user_lookup_app_service_pb2 import UserLookupAppService_userLookupByUserIdResponse
from src.resource.proto._generated.user_lookup_app_service_pb2_grpc import UserLookupAppServiceServicer


class UserLookupAppServiceListener(UserLookupAppServiceServicer):
    """The listener function implements the rpc call as described in the .proto file"""

    def __init__(self):
        self.counter = 0
        self.last_print_time = time.time()
        self._tokenService = TokenService()

    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def userLookupByUserEmail(self, request, context):
        pass
        # try:
        #     token = self._token(context)
        #     userAppService: UserApplicationService = AppDi.instance.get(UserApplicationService)
        #     user: User = userAppService.userByEmail(email=request.email, token=token)
        #     response = UserLookupAppService_userLookupByUserEmailResponse()
        #     self._addObjectToResponse(obj=user, response=response)
        #     return response
        # except UserDoesNotExistException:
        #     context.set_code(grpc.StatusCode.NOT_FOUND)
        #     context.set_details('User does not exist')
        #     return UserLookupAppService_userLookupByUserEmailResponse()
        # except UnAuthorizedException:
        #     context.set_code(grpc.StatusCode.PERMISSION_DENIED)
        #     context.set_details('Un Authorized')
        #     return UserLookupAppService_userLookupByUserEmailResponse()
        # # except Exception as e:
        # #     context.set_code(grpc.StatusCode.UNKNOWN)
        # #     context.set_details(f'{e}')
        # #     return identity_pb2.UserResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def userLookups(self, request, context):
        pass

    #         try:
    #             token = self._token(context)
    #             metadata = context.invocation_metadata()
    #             resultSize = request.resultSize if request.resultSize >= 0 else 10
    #             claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
    #             logger.debug(
    #                 f'[{UserLookupAppServiceListener.userLookups.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
    # resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}')
    #             userAppService: UserApplicationService = AppDi.instance.get(UserApplicationService)
    #
    #             orderData = [{"orderBy": o.orderBy, "direction": o.direction} for o in request.order]
    #             result: dict = userAppService.users(
    #                 resultFrom=request.resultFrom,
    #                 resultSize=resultSize,
    #                 token=token,
    #                 order=orderData)
    #             response = UserLookupAppService_userLookupsResponse()
    #             for user in result['items']:
    #                 response.users.add(id=user.id(),
    #                                    email=user.email(),
    #                                    firstName=user.firstName(),
    #                                    lastName=user.lastName(),
    #                                    addressOne=user.addressOne(),
    #                                    addressTwo=user.addressTwo(),
    #                                    postalCode=user.postalCode(),
    #                                    phoneNumber=user.phoneNumber(),
    #                                    avatarImage=user.avatarImage(),
    #                                    countryId=user.countryId(),
    #                                    cityId=user.cityId(),
    #                                    countryStateName=user.countryStateName(),
    #                                    startDate=user.startDate()
    #                                    )
    #             response.itemCount = result['itemCount']
    #             logger.debug(f'[{UserLookupAppServiceListener.userLookups.__qualname__}] - response: {response}')
    #             return UserLookupAppService_userLookupsResponse(users=response.users, itemCount=response.itemCount)
    #         except UserDoesNotExistException:
    #             context.set_code(grpc.StatusCode.NOT_FOUND)
    #             context.set_details('No users found')
    #             return UserLookupAppService_userLookupsResponse()
    #         except UnAuthorizedException:
    #             context.set_code(grpc.StatusCode.PERMISSION_DENIED)
    #             context.set_details('Un Authorized')
    #             return UserLookupAppService_userLookupsResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def userLookupByUserId(self, request, context):
        try:
            token = self._token(context)
            userLookupAppService: UserLookupApplicationService = AppDi.instance.get(UserLookupApplicationService)
            userLookup: UserLookup = userLookupAppService.userLookupByUserId(id=request.id, token=token)

            logger.debug(f'[{UserLookupAppServiceListener.userLookupByUserId.__qualname__}] - response: {userLookup}')
            response = UserLookupAppService_userLookupByUserIdResponse()
            self._addObjectToResponse(userLookup=userLookup, response=response.userLookup)
            return response
        except UserDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('User does not exist')
            return UserLookupAppService_userLookupByUserIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return UserLookupAppService_userLookupByUserIdResponse()

    @debugLogger
    def _addObjectToResponse(self, userLookup: UserLookup, response: Any):
        self._addUserObjectToResponse(obj=userLookup.user(), response=response.user)
        for role in userLookup.roles():
            self._addRoleObjectToRolesResponse(obj=role, response=response)

        for org in userLookup.organizations():
            self._addOrganizationObjectToOrganizationsResponse(obj=org, response=response)

    def _addRoleObjectToRolesResponse(self, obj: Role, response: Any):
        response.roles.add(id=obj.id(), name=obj.name())

    def _addOrganizationObjectToOrganizationsResponse(self, obj: Organization, response: Any):
        response.organizations.add(
            id=obj.id(),
            name=obj.name(),
            websiteUrl=obj.websiteUrl(),
            organizationType=obj.organizationType(),
            addressOne=obj.addressOne(),
            addressTwo=obj.addressTwo(),
            postalCode=obj.postalCode(),
            countryId=obj.countryId(),
            cityId=obj.cityId(),
            countryStateName=obj.countryStateName(),
            managerFirstName=obj.managerFirstName(),
            managerLastName=obj.managerLastName(),
            managerEmail=obj.managerEmail(),
            managerPhoneNumber=obj.managerPhoneNumber(),
            managerAvatar=obj.managerAvatar()
        )

    def _addUserObjectToResponse(self, obj: User, response: Any):
        response.id = obj.id()
        response.email = obj.email()
        response.firstName = obj.firstName()
        response.lastName = obj.lastName()
        response.addressOne = obj.addressOne()
        response.addressTwo = obj.addressTwo()
        response.postalCode = obj.postalCode()
        response.phoneNumber = obj.phoneNumber()
        response.avatarImage = obj.avatarImage()
        response.countryId = obj.countryId()
        response.cityId = obj.cityId()
        response.countryStateName = obj.countryStateName()
        response.startDate = obj.startDate() if obj.startDate() is not None else 0.0

    @debugLogger
    def _token(self, context) -> str:
        metadata = context.invocation_metadata()
        if 'token' in metadata[0]:
            return metadata[0].value
        return ''
