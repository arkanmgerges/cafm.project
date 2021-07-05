"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import grpc

from src.application.MaintenanceProcedureApplicationService import MaintenanceProcedureApplicationService
from src.domain_model.project.maintenance.procedure.MaintenanceProcedure import MaintenanceProcedure
from src.domain_model.resource.exception.MaintenanceProcedureDoesNotExistException import MaintenanceProcedureDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.maintenance_procedure_app_service_pb2 import (
    MaintenanceProcedureAppService_maintenanceProceduresResponse,
    MaintenanceProcedureAppService_maintenanceProcedureByIdResponse,
    MaintenanceProcedureAppService_newIdResponse,
    MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdResponse)

from src.resource.proto._generated.project.maintenance_procedure_app_service_pb2_grpc import \
    MaintenanceProcedureAppServiceServicer


class MaintenanceProcedureAppServiceListener(
    CommonBaseListener, MaintenanceProcedureAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):
        super().__init__()
        import src.port_adapter.AppDi as AppDi
        self._appService: MaintenanceProcedureApplicationService = AppDi.instance.get(
            MaintenanceProcedureApplicationService
        )


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(request=request, context=context, response=MaintenanceProcedureAppService_newIdResponse)


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def maintenance_procedures(self, request, context):
        response = MaintenanceProcedureAppService_maintenanceProceduresResponse
        try:
            import src.port_adapter.AppDi as AppDi
            maintenanceProcedureAppService: MaintenanceProcedureApplicationService = (
                AppDi.instance.get(MaintenanceProcedureApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=maintenanceProcedureAppService.maintenanceProcedures,
                                     responseAttribute='maintenance_procedures'
                                     )

        except MaintenanceProcedureDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No maintenanceProcedures found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def maintenance_procedures_by_equipment_id(self, request, context):
        response = MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            maintenanceProcedureAppService: MaintenanceProcedureApplicationService = (
                AppDi.instance.get(MaintenanceProcedureApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                  appServiceMethod=maintenanceProcedureAppService.maintenanceProceduresByEquipmentId,
                                  responseAttribute='maintenance_procedures',
                                  appServiceParams={"equipmentId": request.equipment_id}
                                  )

        except MaintenanceProcedureDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No maintenanceProcedures found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def maintenance_procedure_by_id(self, request, context):
        response = MaintenanceProcedureAppService_maintenanceProcedureByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            maintenanceProcedureAppService: MaintenanceProcedureApplicationService = (
                AppDi.instance.get(MaintenanceProcedureApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=maintenanceProcedureAppService.maintenanceProcedureById,
                                     responseAttribute='maintenance_procedure',
                                     appServiceParams={'id': request.id}
                                     )
        except MaintenanceProcedureDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    def _addObjectToGrpcResponse(self, obj: MaintenanceProcedure, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "name": obj.name() if obj.name() is not None else '',
            "type": obj.type() if obj.type() is not None else '',
            "frequency": obj.frequency() if obj.frequency() is not None else '',
            "start_date": obj.startDate() if obj.startDate() is not None else 0,
            "subcontractor_id": obj.subcontractorId() if obj.subcontractorId() is not None else '',
            "equipment_id": obj.equipmentId() if obj.equipmentId() is not None else '',
            "sub_type": obj.subType() if obj.subType() is not None else '',
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
