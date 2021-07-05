"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import grpc

from src.application.MaintenanceProcedureOperationParameterApplicationService import MaintenanceProcedureOperationParameterApplicationService
from src.domain_model.project.maintenance.procedure.operation.parameter.MaintenanceProcedureOperationParameter import MaintenanceProcedureOperationParameter
from src.domain_model.resource.exception.MaintenanceProcedureOperationParameterDoesNotExistException import MaintenanceProcedureOperationParameterDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.maintenance_procedure_operation_parameter_app_service_pb2 import (
    MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse,
    MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse,
    MaintenanceProcedureOperationParameterAppService_newIdResponse,
    MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse,

)
from src.resource.proto._generated.project.maintenance_procedure_operation_parameter_app_service_pb2_grpc import \
    MaintenanceProcedureOperationParameterAppServiceServicer


class MaintenanceProcedureOperationParameterAppServiceListener(
    CommonBaseListener, MaintenanceProcedureOperationParameterAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):
        super().__init__()
        import src.port_adapter.AppDi as AppDi
        self._appService: MaintenanceProcedureOperationParameterApplicationService = AppDi.instance.get(
            MaintenanceProcedureOperationParameterApplicationService
        )


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(request=request, context=context, response=MaintenanceProcedureOperationParameterAppService_newIdResponse)


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def maintenance_procedure_operation_parameters(self, request, context):
        response = MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersResponse
        try:
            import src.port_adapter.AppDi as AppDi
            maintenanceProcedureOperationParameterAppService: MaintenanceProcedureOperationParameterApplicationService = (
                AppDi.instance.get(MaintenanceProcedureOperationParameterApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=maintenanceProcedureOperationParameterAppService.maintenanceProcedureOperationParameters,
                                     responseAttribute='maintenance_procedure_operation_parameters'
                                     )

        except MaintenanceProcedureOperationParameterDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No maintenanceProcedureOperationParameters found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def maintenance_procedure_operation_parameters_by_maintenance_procedure_operation_id(self, request, context):
        response = MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParametersByMaintenanceProcedureOperationIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            maintenanceProcedureOperationParameterAppService: MaintenanceProcedureOperationParameterApplicationService = (
                AppDi.instance.get(MaintenanceProcedureOperationParameterApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                  appServiceMethod=maintenanceProcedureOperationParameterAppService.maintenanceProcedureOperationParametersByMaintenanceProcedureOperationId,
                                  responseAttribute='maintenance_procedure_operation_parameters',
                                  appServiceParams={"maintenanceProcedureOperationId": request.maintenance_procedure_operation_id},
                                  )

        except MaintenanceProcedureOperationParameterDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No maintenanceProcedureOperationParameters found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def maintenance_procedure_operation_parameter_by_id(self, request, context):
        response = MaintenanceProcedureOperationParameterAppService_maintenanceProcedureOperationParameterByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            maintenanceProcedureOperationParameterAppService: MaintenanceProcedureOperationParameterApplicationService = (
                AppDi.instance.get(MaintenanceProcedureOperationParameterApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=maintenanceProcedureOperationParameterAppService.maintenanceProcedureOperationParameterById,
                                     responseAttribute='maintenance_procedure_operation_parameter',
                                     appServiceParams={'id': request.id}
                                     )
        except MaintenanceProcedureOperationParameterDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    def _addObjectToGrpcResponse(self, obj: MaintenanceProcedureOperationParameter, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "name": obj.name() if obj.name() is not None else '',
            "unit_id": obj.unitId() if obj.unitId() is not None else '',
            "maintenance_procedure_operation_id": obj.maintenanceProcedureOperationId() if obj.maintenanceProcedureOperationId() is not None else '',
            "min_value": str(obj.minValue()) if obj.minValue() is not None else '0.0',
            "max_value": str(obj.maxValue()) if obj.maxValue() is not None else '0.0',
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
