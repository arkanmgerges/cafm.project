"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import grpc

from src.application.RoleApplicationService import RoleApplicationService
from src.domain_model.resource.exception.RoleDoesNotExistException import RoleDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.domain_model.role.Role import Role
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.role_app_service_pb2 import (
    RoleAppService_rolesResponse,
    RoleAppService_roleByIdResponse,
    RoleAppService_newIdResponse, RoleAppService_rolesByOrganizationTypeResponse, RoleAppService_roleByNameResponse,
)
from src.resource.proto._generated.role_app_service_pb2_grpc import (
    RoleAppServiceServicer,
)


class RoleAppServiceListener(
    CommonBaseListener, RoleAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):
        super().__init__()
        import src.port_adapter.AppDi as AppDi
        self._appService: RoleApplicationService = AppDi.instance.get(
            RoleApplicationService
        )


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(request=request, context=context, response=RoleAppService_newIdResponse)


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def roles(self, request, context):
        response = RoleAppService_rolesResponse
        try:
            import src.port_adapter.AppDi as AppDi
            roleAppService: RoleApplicationService = (
                AppDi.instance.get(RoleApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=roleAppService.roles,
                                     responseAttribute='roles'
                                     )

        except RoleDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No roles found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def roles_by_organization_type(self, request, context):
        response = RoleAppService_rolesByOrganizationTypeResponse
        try:
            import src.port_adapter.AppDi as AppDi
            roleAppService: RoleApplicationService = (
                AppDi.instance.get(RoleApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                  appServiceMethod=roleAppService.rolesByOrganizationType,
                                  responseAttribute='roles',
                                  appServiceParams={"organizationType": request.organization_type}
                                  )

        except RoleDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No roles found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def role_by_id(self, request, context):
        response = RoleAppService_roleByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            roleAppService: RoleApplicationService = (
                AppDi.instance.get(RoleApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=roleAppService.roleById,
                                     responseAttribute='role',
                                     appServiceParams={'id': request.id}
                                     )
        except RoleDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def role_by_name(self, request, context):
        response = RoleAppService_roleByNameResponse
        try:
            import src.port_adapter.AppDi as AppDi
            roleAppService: RoleApplicationService = (
                AppDi.instance.get(RoleApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=roleAppService.roleByName,
                                     responseAttribute='role',
                                     appServiceParams={'name': request.name}
                                     )
        except RoleDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    def _addObjectToGrpcResponse(self, obj: Role, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "name": obj.name() if obj.name() is not None else '',
            "title": obj.title() if obj.title() is not None else '',
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
