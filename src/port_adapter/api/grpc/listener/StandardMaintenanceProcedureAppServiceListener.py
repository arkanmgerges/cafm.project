"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import grpc

from src.application.StandardMaintenanceProcedureApplicationService import StandardMaintenanceProcedureApplicationService
from src.domain_model.standard_maintenance_procedure.StandardMaintenanceProcedure import StandardMaintenanceProcedure
from src.domain_model.resource.exception.StandardMaintenanceProcedureDoesNotExistException import StandardMaintenanceProcedureDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.standard_maintenance_procedure_app_service_pb2 import (
    StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse,
    StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse,
    StandardMaintenanceProcedureAppService_newIdResponse,
)
from src.resource.proto._generated.standard_maintenance_procedure_app_service_pb2_grpc import (
    StandardMaintenanceProcedureAppServiceServicer,
)

class StandardMaintenanceProcedureAppServiceListener(
    CommonBaseListener, StandardMaintenanceProcedureAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):
        import src.port_adapter.AppDi as AppDi
        self._appService: StandardMaintenanceProcedureApplicationService = AppDi.instance.get(
            StandardMaintenanceProcedureApplicationService
        )
        super().__init__()


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(request=request, context=context, response=StandardMaintenanceProcedureAppService_newIdResponse)


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def standard_maintenance_procedures(self, request, context):
        response = StandardMaintenanceProcedureAppService_standardMaintenanceProceduresResponse
        try:
            import src.port_adapter.AppDi as AppDi
            standardMaintenanceProcedureAppService: StandardMaintenanceProcedureApplicationService = (
                AppDi.instance.get(StandardMaintenanceProcedureApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=standardMaintenanceProcedureAppService.standardMaintenanceProcedures,
                                     responseAttribute='standard_maintenance_procedures'
                                     )

        except StandardMaintenanceProcedureDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No standardMaintenanceProcedures found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def standard_maintenance_procedure_by_id(self, request, context):
        response = StandardMaintenanceProcedureAppService_standardMaintenanceProcedureByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            standardMaintenanceProcedureAppService: StandardMaintenanceProcedureApplicationService = (
                AppDi.instance.get(StandardMaintenanceProcedureApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=standardMaintenanceProcedureAppService.standardMaintenanceProcedureById,
                                     responseAttribute='standard_maintenance_procedure',
                                     appServiceParams={'id': request.id}
                                     )
        except StandardMaintenanceProcedureDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    def _addObjectToGrpcResponse(self, obj: StandardMaintenanceProcedure, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "name": obj.name() if obj.name() is not None else '',
            "type": obj.type() if obj.type() is not None else '',
            "sub_type": obj.subtype() if obj.subtype() is not None else '',
            "frequency": obj.frequency() if obj.frequency() is not None else '',
            "start_date": obj.startDate() if obj.startDate() is not None else 0,
            "organization_id": obj.organizationId() if obj.organizationId() is not None else '',
            "standard_equipment_category_group_id": obj.standardEquipmentCategoryGroupId() if obj.standardEquipmentCategoryGroupId() is not None else '',
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
