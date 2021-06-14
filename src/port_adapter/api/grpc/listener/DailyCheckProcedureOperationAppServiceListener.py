"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import time
from typing import Any

import grpc

from src.application.DailyCheckProcedureOperationApplicationService import DailyCheckProcedureOperationApplicationService
from src.domain_model.project.daily_check.procedure.operation.DailyCheckProcedureOperation import DailyCheckProcedureOperation
from src.domain_model.resource.exception.DailyCheckProcedureOperationDoesNotExistException import DailyCheckProcedureOperationDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.daily_check_procedure_operation_app_service_pb2 import (
    DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsResponse,
    DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdResponse,
    DailyCheckProcedureOperationAppService_newIdResponse,
    DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdResponse,
)
from src.resource.proto._generated.daily_check_procedure_operation_app_service_pb2_grpc import (
    DailyCheckProcedureOperationAppServiceServicer,
)

class DailyCheckProcedureOperationAppServiceListener(
    CommonBaseListener, DailyCheckProcedureOperationAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):
        super().__init__()
        import src.port_adapter.AppDi as AppDi
        self._appService: DailyCheckProcedureOperationApplicationService = AppDi.instance.get(
            DailyCheckProcedureOperationApplicationService
        )


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(request=request, context=context, response=DailyCheckProcedureOperationAppService_newIdResponse)


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def daily_check_procedure_operations(self, request, context):
        response = DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsResponse
        try:
            import src.port_adapter.AppDi as AppDi
            dailyCheckProcedureOperationAppService: DailyCheckProcedureOperationApplicationService = (
                AppDi.instance.get(DailyCheckProcedureOperationApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=dailyCheckProcedureOperationAppService.dailyCheckProcedureOperations,
                                     responseAttribute='daily_check_procedure_operations'
                                     )

        except DailyCheckProcedureOperationDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No dailyCheckProcedureOperations found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def daily_check_procedure_operation_by_id(self, request, context):
        response = DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            dailyCheckProcedureOperationAppService: DailyCheckProcedureOperationApplicationService = (
                AppDi.instance.get(DailyCheckProcedureOperationApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=dailyCheckProcedureOperationAppService.dailyCheckProcedureOperationById,
                                     responseAttribute='daily_check_procedure_operation',
                                     appServiceParams={'id': request.id}
                                     )
        except DailyCheckProcedureOperationDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def daily_check_procedure_operations_by_daily_check_procedure_id(self, request, context):
        response = DailyCheckProcedureOperationAppService_dailyCheckProcedureOperationsByDailyCheckProcedureIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            dailyCheckProcedureOperationAppService: DailyCheckProcedureOperationApplicationService = (
                AppDi.instance.get(DailyCheckProcedureOperationApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                  appServiceMethod=dailyCheckProcedureOperationAppService.dailyCheckProcedureOperationsByDailyCheckProcedureId,
                                  responseAttribute='daily_check_procedure_operations',
                                  appServiceParams={'dailyCheckProcedureId': request.daily_check_procedure_id}
                                  )

        except DailyCheckProcedureOperationDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No dailyCheckProcedureOperations found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    def _addObjectToGrpcResponse(self, obj: DailyCheckProcedureOperation, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "name": obj.name() if obj.name() is not None else '',
            "description": obj.description() if obj.description() is not None else '',
            "type": obj.type() if obj.type() is not None else '',
            "daily_check_procedure_id": obj.dailyCheckProcedureId() if obj.dailyCheckProcedureId() is not None else '',
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
