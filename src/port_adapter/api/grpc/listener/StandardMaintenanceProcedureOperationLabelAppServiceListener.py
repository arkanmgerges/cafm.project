"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import grpc

from src.application.StandardMaintenanceProcedureOperationLabelApplicationService import StandardMaintenanceProcedureOperationLabelApplicationService
from src.domain_model.standard_maintenance.procedure.operation.label.StandardMaintenanceProcedureOperationLabel import StandardMaintenanceProcedureOperationLabel
from src.domain_model.resource.exception.StandardMaintenanceProcedureOperationLabelDoesNotExistException import StandardMaintenanceProcedureOperationLabelDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.standard_maintenance_procedure_operation_label_app_service_pb2 import (
    StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse,
    StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse,
    StandardMaintenanceProcedureOperationLabelAppService_newIdResponse,
)
from src.resource.proto._generated.standard_maintenance_procedure_operation_label_app_service_pb2_grpc import (
    StandardMaintenanceProcedureOperationLabelAppServiceServicer,
)

class StandardMaintenanceProcedureOperationLabelAppServiceListener(
    CommonBaseListener, StandardMaintenanceProcedureOperationLabelAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):
        super().__init__()
        import src.port_adapter.AppDi as AppDi
        self._appService: StandardMaintenanceProcedureOperationLabelApplicationService = AppDi.instance.get(
            StandardMaintenanceProcedureOperationLabelApplicationService
        )
        


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(request=request, context=context, response=StandardMaintenanceProcedureOperationLabelAppService_newIdResponse)


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def standard_maintenance_procedure_operation_labels(self, request, context):
        response = StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelsResponse
        try:
            import src.port_adapter.AppDi as AppDi
            standardMaintenanceProcedureOperationLabelAppService: StandardMaintenanceProcedureOperationLabelApplicationService = (
                AppDi.instance.get(StandardMaintenanceProcedureOperationLabelApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=standardMaintenanceProcedureOperationLabelAppService.standardMaintenanceProcedureOperationLabels,
                                     responseAttribute='standard_maintenance_procedure_operation_labels'
                                     )

        except StandardMaintenanceProcedureOperationLabelDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No standardMaintenanceProcedureOperationLabels found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def standard_maintenance_procedure_operation_label_by_id(self, request, context):
        response = StandardMaintenanceProcedureOperationLabelAppService_standardMaintenanceProcedureOperationLabelByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            standardMaintenanceProcedureOperationLabelAppService: StandardMaintenanceProcedureOperationLabelApplicationService = (
                AppDi.instance.get(StandardMaintenanceProcedureOperationLabelApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=standardMaintenanceProcedureOperationLabelAppService.standardMaintenanceProcedureOperationLabelById,
                                     responseAttribute='standard_maintenance_procedure_operation_label',
                                     appServiceParams={'id': request.id}
                                     )
        except StandardMaintenanceProcedureOperationLabelDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    def _addObjectToGrpcResponse(self, obj: StandardMaintenanceProcedureOperationLabel, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "label": obj.label() if obj.label() is not None else '',
            "generate_alert": obj.generateAlert() if obj.generateAlert() is not None else 0,
            "standard_maintenance_procedure_operation_id": obj.standardMaintenanceProcedureOperationId() if obj.standardMaintenanceProcedureOperationId() is not None else '',
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
