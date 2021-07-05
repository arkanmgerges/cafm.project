"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import grpc

from src.application.OrganizationApplicationService import OrganizationApplicationService
from src.domain_model.organization.Organization import Organization
from src.domain_model.resource.exception.OrganizationDoesNotExistException import OrganizationDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.organization_app_service_pb2 import (
    OrganizationAppService_organizationsResponse,
    OrganizationAppService_organizationByIdResponse,
    OrganizationAppService_newIdResponse, OrganizationAppService_organizationsByTypeResponse,
)
from src.resource.proto._generated.project.organization_app_service_pb2_grpc import OrganizationAppServiceServicer


class OrganizationAppServiceListener(
    CommonBaseListener, OrganizationAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):
        super().__init__()
        import src.port_adapter.AppDi as AppDi
        self._appService: OrganizationApplicationService = AppDi.instance.get(
            OrganizationApplicationService
        )


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(request=request, context=context, response=OrganizationAppService_newIdResponse)


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def organizations(self, request, context):
        response = OrganizationAppService_organizationsResponse
        try:
            import src.port_adapter.AppDi as AppDi
            organizationAppService: OrganizationApplicationService = (
                AppDi.instance.get(OrganizationApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=organizationAppService.organizations,
                                     responseAttribute='organizations'
                                     )

        except OrganizationDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No organizations found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def organizations_by_type(self, request, context):
        response = OrganizationAppService_organizationsByTypeResponse
        try:
            import src.port_adapter.AppDi as AppDi
            organizationAppService: OrganizationApplicationService = (
                AppDi.instance.get(OrganizationApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                  appServiceMethod=organizationAppService.organizationsByType,
                                  responseAttribute='organizations',
                                  appServiceParams={"type": request.type}
                                  )

        except OrganizationDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No organizations found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def organization_by_id(self, request, context):
        response = OrganizationAppService_organizationByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            organizationAppService: OrganizationApplicationService = (
                AppDi.instance.get(OrganizationApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=organizationAppService.organizationById,
                                     responseAttribute='organization',
                                     appServiceParams={'id': request.id}
                                     )
        except OrganizationDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    def _addObjectToGrpcResponse(self, obj: Organization, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "name": obj.name() if obj.name() is not None else '',
            "website_url": obj.websiteUrl() if obj.websiteUrl() is not None else '',
            "organization_type": obj.organizationType() if obj.organizationType() is not None else '',
            "address_one": obj.addressOne() if obj.addressOne() is not None else '',
            "address_two": obj.addressTwo() if obj.addressTwo() is not None else '',
            "postal_code": obj.postalCode() if obj.postalCode() is not None else '',
            "country_id": obj.countryId() if obj.countryId() is not None else 0,
            "city_id": obj.cityId() if obj.cityId() is not None else 0,
            "country_state_name": obj.countryStateName() if obj.countryStateName() is not None else '',
            "country_state_iso_code": obj.countryStateIsoCode() if obj.countryStateIsoCode() is not None else '',
            "manager_first_name": obj.managerFirstName() if obj.managerFirstName() is not None else '',
            "manager_last_name": obj.managerLastName() if obj.managerLastName() is not None else '',
            "manager_email": obj.managerEmail() if obj.managerEmail() is not None else '',
            "manager_phone_number": obj.managerPhoneNumber() if obj.managerPhoneNumber() is not None else '',
            "manager_avatar": obj.managerAvatar() if obj.managerAvatar() is not None else '',
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
