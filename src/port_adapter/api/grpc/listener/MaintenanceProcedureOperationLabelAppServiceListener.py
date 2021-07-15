"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import grpc

from src.application.MaintenanceProcedureOperationLabelApplicationService import MaintenanceProcedureOperationLabelApplicationService
from src.domain_model.project.maintenance.procedure.operation.label.MaintenanceProcedureOperationLabel import MaintenanceProcedureOperationLabel
from src.domain_model.resource.exception.MaintenanceProcedureOperationLabelDoesNotExistException import MaintenanceProcedureOperationLabelDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.maintenance_procedure_operation_label_app_service_pb2 import (
    MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsResponse,
    MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdResponse,
    MaintenanceProcedureOperationLabelAppService_newIdResponse,
)
from src.resource.proto._generated.maintenance_procedure_operation_label_app_service_pb2_grpc import (
    MaintenanceProcedureOperationLabelAppServiceServicer,
)

class MaintenanceProcedureOperationLabelAppServiceListener(
    CommonBaseListener, MaintenanceProcedureOperationLabelAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):
        super().__init__()
        import src.port_adapter.AppDi as AppDi
        self._appService: MaintenanceProcedureOperationLabelApplicationService = AppDi.instance.get(
            MaintenanceProcedureOperationLabelApplicationService
        )
        


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(request=request, context=context, response=MaintenanceProcedureOperationLabelAppService_newIdResponse)


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def maintenance_procedure_operation_labels(self, request, context):
        response = MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelsResponse
        try:
            import src.port_adapter.AppDi as AppDi
            maintenanceProcedureOperationLabelAppService: MaintenanceProcedureOperationLabelApplicationService = (
                AppDi.instance.get(MaintenanceProcedureOperationLabelApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=maintenanceProcedureOperationLabelAppService.maintenanceProcedureOperationLabels,
                                     responseAttribute='maintenance_procedure_operation_labels'
                                     )

        except MaintenanceProcedureOperationLabelDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No maintenanceProcedureOperationLabels found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def maintenance_procedure_operation_label_by_id(self, request, context):
        response = MaintenanceProcedureOperationLabelAppService_maintenanceProcedureOperationLabelByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            maintenanceProcedureOperationLabelAppService: MaintenanceProcedureOperationLabelApplicationService = (
                AppDi.instance.get(MaintenanceProcedureOperationLabelApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=maintenanceProcedureOperationLabelAppService.maintenanceProcedureOperationLabelById,
                                     responseAttribute='maintenance_procedure_operation_label',
                                     appServiceParams={'id': request.id}
                                     )
        except MaintenanceProcedureOperationLabelDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    def _addObjectToGrpcResponse(self, obj: MaintenanceProcedureOperationLabel, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "label": obj.label() if obj.label() is not None else '',
            "generate_alert": obj.generateAlert() if obj.generateAlert() is not None else 0,
            "maintenance_procedure_operation_id": obj.maintenanceProcedureOperationId() if obj.maintenanceProcedureOperationId() is not None else '',
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
