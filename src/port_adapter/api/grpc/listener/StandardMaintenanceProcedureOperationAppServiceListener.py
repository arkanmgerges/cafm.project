"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import grpc

from src.application.StandardMaintenanceProcedureOperationApplicationService import StandardMaintenanceProcedureOperationApplicationService
from src.domain_model.standard_maintenance.procedure.operation.StandardMaintenanceProcedureOperation import StandardMaintenanceProcedureOperation
from src.domain_model.resource.exception.StandardMaintenanceProcedureOperationDoesNotExistException import StandardMaintenanceProcedureOperationDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.standard_maintenance_procedure_operation_app_service_pb2 import (
    StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsResponse,
    StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdResponse,
    StandardMaintenanceProcedureOperationAppService_newIdResponse,
    StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdResponse,
)
from src.resource.proto._generated.standard_maintenance_procedure_operation_app_service_pb2_grpc import (
    StandardMaintenanceProcedureOperationAppServiceServicer,
)

class StandardMaintenanceProcedureOperationAppServiceListener(
    CommonBaseListener, StandardMaintenanceProcedureOperationAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):
        super().__init__()
        import src.port_adapter.AppDi as AppDi
        self._appService: StandardMaintenanceProcedureOperationApplicationService = AppDi.instance.get(
            StandardMaintenanceProcedureOperationApplicationService
        )


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(request=request, context=context, response=StandardMaintenanceProcedureOperationAppService_newIdResponse)


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def standard_maintenance_procedure_operations(self, request, context):
        response = StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsResponse
        try:
            import src.port_adapter.AppDi as AppDi
            standardMaintenanceProcedureOperationAppService: StandardMaintenanceProcedureOperationApplicationService = (
                AppDi.instance.get(StandardMaintenanceProcedureOperationApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=standardMaintenanceProcedureOperationAppService.standardMaintenanceProcedureOperations,
                                     responseAttribute='standard_maintenance_procedure_operations'
                                     )

        except StandardMaintenanceProcedureOperationDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No standard maintenance procedure operations found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def standard_maintenance_procedure_operations_by_standard_maintenance_procedure_id(self, request, context):
        response = StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            standardMaintenanceProcedureOperationAppService: StandardMaintenanceProcedureOperationApplicationService = (
                AppDi.instance.get(StandardMaintenanceProcedureOperationApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                  appServiceMethod=standardMaintenanceProcedureOperationAppService.standardMaintenanceProcedureOperationsByStandardMaintenanceProcedureId,
                                  responseAttribute='standard_maintenance_procedure_operations',
                                  appServiceParams={'standard_maintenanceProcedureId': request.standard_maintenance_procedure_id}
                                  )

        except StandardMaintenanceProcedureOperationDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No standard maintenance procedure operations found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def standard_maintenance_procedure_operation_by_id(self, request, context):
        response = StandardMaintenanceProcedureOperationAppService_standardMaintenanceProcedureOperationByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            standardMaintenanceProcedureOperationAppService: StandardMaintenanceProcedureOperationApplicationService = (
                AppDi.instance.get(StandardMaintenanceProcedureOperationApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=standardMaintenanceProcedureOperationAppService.standardMaintenanceProcedureOperationById,
                                     responseAttribute='standard_maintenance_procedure_operation',
                                     appServiceParams={'id': request.id}
                                     )
        except StandardMaintenanceProcedureOperationDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("standard maintenance procedure operation does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    def _addObjectToGrpcResponse(self, obj: StandardMaintenanceProcedureOperation, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "name": obj.name() if obj.name() is not None else '',
            "description": obj.description() if obj.description() is not None else '',
            "type": obj.type() if obj.type() is not None else '',
            "standard_maintenance_procedure_id": obj.standardMaintenanceProcedureId() if obj.standardMaintenanceProcedureId() is not None else '',
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
