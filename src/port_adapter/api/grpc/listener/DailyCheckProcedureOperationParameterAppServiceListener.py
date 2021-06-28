"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import grpc

from src.application.DailyCheckProcedureOperationParameterApplicationService import DailyCheckProcedureOperationParameterApplicationService
from src.domain_model.project.daily_check.procedure.operation.parameter.DailyCheckProcedureOperationParameter import DailyCheckProcedureOperationParameter
from src.domain_model.resource.exception.DailyCheckProcedureOperationParameterDoesNotExistException import DailyCheckProcedureOperationParameterDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.daily_check_procedure_operation_parameter_app_service_pb2 import \
    DailyCheckProcedureOperationParameterAppService_newIdResponse, \
    DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse, \
    DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdResponse, \
    DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse
from src.resource.proto._generated.project.daily_check_procedure_operation_parameter_app_service_pb2_grpc import \
    DailyCheckProcedureOperationParameterAppServiceServicer


class DailyCheckProcedureOperationParameterAppServiceListener(
    CommonBaseListener, DailyCheckProcedureOperationParameterAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):
        super().__init__()
        import src.port_adapter.AppDi as AppDi
        self._appService: DailyCheckProcedureOperationParameterApplicationService = AppDi.instance.get(
            DailyCheckProcedureOperationParameterApplicationService
        )


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(request=request, context=context, response=DailyCheckProcedureOperationParameterAppService_newIdResponse)


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def daily_check_procedure_operation_parameters(self, request, context):
        response = DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse
        try:
            import src.port_adapter.AppDi as AppDi
            dailyCheckProcedureOperationParameterAppService: DailyCheckProcedureOperationParameterApplicationService = (
                AppDi.instance.get(DailyCheckProcedureOperationParameterApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=dailyCheckProcedureOperationParameterAppService.dailyCheckProcedureOperationParameters,
                                     responseAttribute='daily_check_procedure_operation_parameters'
                                     )

        except DailyCheckProcedureOperationParameterDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No dailyCheckProcedureOperationParameters found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def daily_check_procedure_operation_parameters_by_daily_check_procedure_operation_id(
            self, request, context
    ):
        response = DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            dailyCheckProcedureOperationParameterAppService: DailyCheckProcedureOperationParameterApplicationService = (
                AppDi.instance.get(DailyCheckProcedureOperationParameterApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                  appServiceMethod=dailyCheckProcedureOperationParameterAppService.dailyCheckProcedureOperationParametersByDailyCheckProcedureOperationId,
                                  responseAttribute='daily_check_procedure_operation_parameters',
                                  appServiceParams={"dailyCheckProcedureOperationId": request.daily_check_procedure_operation_id}
                                  )

        except DailyCheckProcedureOperationParameterDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No dailyCheckProcedureOperationParameters found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def daily_check_procedure_operation_parameter_by_id(self, request, context):
        response = DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            dailyCheckProcedureOperationParameterAppService: DailyCheckProcedureOperationParameterApplicationService = (
                AppDi.instance.get(DailyCheckProcedureOperationParameterApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=dailyCheckProcedureOperationParameterAppService.dailyCheckProcedureOperationParameterById,
                                     responseAttribute='daily_check_procedure_operation_parameter',
                                     appServiceParams={'id': request.id}
                                     )
        except DailyCheckProcedureOperationParameterDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    def _addObjectToGrpcResponse(self, obj: DailyCheckProcedureOperationParameter, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "name": obj.name() if obj.name() is not None else '',
            "unit_id": obj.unitId() if obj.unitId() is not None else '',
            "daily_check_procedure_operation_id": obj.dailyCheckProcedureOperationId() if obj.dailyCheckProcedureOperationId() is not None else '',
            "min_value": str(obj.minValue()) if obj.minValue() is not None else "0.0",
            "max_value": str(obj.maxValue()) if obj.maxValue() is not None else "0.0",
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
