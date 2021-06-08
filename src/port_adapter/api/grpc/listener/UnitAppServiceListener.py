"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import grpc

from src.application.UnitApplicationService import UnitApplicationService
from src.domain_model.project.unit.Unit import Unit
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.domain_model.resource.exception.UnitDoesNotExistException import UnitDoesNotExistException
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.unit_app_service_pb2 import (
    UnitAppService_unitsResponse,
    UnitAppService_unitByIdResponse,
    UnitAppService_newIdResponse,
)
from src.resource.proto._generated.unit_app_service_pb2_grpc import (
    UnitAppServiceServicer,
)


class UnitAppServiceListener(
    CommonBaseListener, UnitAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):
        import src.port_adapter.AppDi as AppDi
        self._appService: UnitApplicationService = AppDi.instance.get(
            UnitApplicationService
        )
        super().__init__()


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(request=request, context=context, response=UnitAppService_newIdResponse)


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def units(self, request, context):
        response = UnitAppService_unitsResponse
        try:
            import src.port_adapter.AppDi as AppDi
            unitAppService: UnitApplicationService = (
                AppDi.instance.get(UnitApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=unitAppService.units,
                                     responseAttribute='units'
                                     )

        except UnitDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No units found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def unit_by_id(self, request, context):
        response = UnitAppService_unitByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            unitAppService: UnitApplicationService = (
                AppDi.instance.get(UnitApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=unitAppService.unitById,
                                     responseAttribute='unit',
                                     appServiceParams={'id': request.id}
                                     )
        except UnitDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    def _addObjectToGrpcResponse(self, obj: Unit, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "name": obj.name(),
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
