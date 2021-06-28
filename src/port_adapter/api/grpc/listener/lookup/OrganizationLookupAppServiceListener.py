"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import time
from typing import Any, List

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.lookup.organization.OrganizationLookupApplicationService import OrganizationLookupApplicationService
from src.application.lookup.organization.OrganizationLookup import OrganizationLookup
from src.domain_model.common.HasToMap import HasToMap
from src.domain_model.organization.Organization import Organization
from src.domain_model.project.Project import Project
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
from src.resource.proto._generated.project.lookup.organization.organization_lookup_app_service_pb2 import \
    OrganizationLookupAppService_organizationLookupsResponse
from src.resource.proto._generated.project.lookup.organization.organization_lookup_app_service_pb2_grpc import \
    OrganizationLookupAppServiceServicer


class OrganizationLookupAppServiceListener(OrganizationLookupAppServiceServicer, BaseListener):
    """The listener function implements the rpc call as described in the .proto file"""

    def __init__(self):
        self.counter = 0
        self.last_print_time = time.time()
        self._tokenService = TokenService()

    def __str__(self):
        return self.__class__.__name__


    """
    c4model|cb|project:Component(identity__grpc__OrganizationLookupAppServiceListener__projectLookups, "Get a user lookups", "grpc listener", "Get user lookups")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def lookup(self, request, context):
        response = OrganizationLookupAppService_organizationLookupsResponse
        try:
            token = self._token(context)
            appService: OrganizationLookupApplicationService = AppDi.instance.get(
                OrganizationLookupApplicationService
            )

            resultFrom = request.result_from if request.result_from >= 0 else 0
            resultSize = request.result_size if request.result_size >= 0 else 10
            logger.debug(
                f"[{OrganizationLookupAppServiceListener.lookup.__qualname__}] - result_from: {request.result_from}, result_size: {request.result_size}"
            )

            orderData = [
                {"orderBy": o.order_by, "direction": o.direction} for o in request.orders
            ]

            filterData = [
                {"key": o.key, "value": o.value} for o in request.filters
            ]

            lookupsDict: dict = appService.lookup(
                resultFrom=resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
                filter=filterData
            )
            response = response()

            response.total_item_count = lookupsDict["totalItemCount"]
            for lookupItem in lookupsDict["items"]:
                responseItem = response.organization_lookups.add()
                self._addObjectToResponse(lookupObject=lookupItem, response=responseItem)
            return response
        except UserDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("User does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    def _addObjectToResponse(self, lookupObject: OrganizationLookup, response: Any):
        self._addOrganizationObjectToResponse(obj=lookupObject.organization(), response=response.organization)
        for role in lookupObject.roles():
            self._addRoleObjectToRolesResponse(obj=role, response=response)

        for project in lookupObject.projects():
            self._addProjectObjectToProjectsResponse(
                obj=project, response=response
            )
        
        for user in lookupObject.users():
            self._addUserObjectToUsersResponse(
                obj=user, response=response
            )

    def _addRoleObjectToRolesResponse(self, obj: Role, response: Any):
        response.roles.add(id=obj.id(), name=obj.name(), title=obj.title())

    def _addOrganizationObjectToResponse(
        self, obj: Organization, response: Any
    ):
        for attribute, value in self._constructKwargs(obj=obj,
                                                      intAttributes=['city_id', 'country_id', ],
                                                      mapping={'organization_id': 'id'}).items():
            setattr(response, attribute, value)

    def _addProjectObjectToProjectsResponse(
        self, obj: Project, response: Any
    ):
        response.projects.add(**(self._constructKwargs(obj=obj, intAttributes=['city_id', 'country_id', 'start_date', 'developer_city_id', 'developer_country_id'], mapping={'project_id': 'id'})))


    def _addUserObjectToUsersResponse(self, obj: User, response: Any):
        response.users.add(**(self._constructKwargs(obj=obj, intAttributes=['city_id', 'country_id', 'start_date', ], mapping={'user_id': 'id'})))


    def _constructKwargs(self, obj: HasToMap, intAttributes: List[str]=None, mapping=None):
        kwargs = {}
        mapping = mapping if mapping is not None else {}
        intAttributes = intAttributes if intAttributes is not None else []
        for attribute, value in obj.toMap().items():
            if attribute in mapping:
                attribute = mapping[attribute]
            if attribute in intAttributes and value is None:
                value = 0
            elif value is None:
                value = ''
            kwargs[attribute] = value
        return kwargs

    @debugLogger
    def _token(self, context) -> str:
        return super()._token(context=context)
