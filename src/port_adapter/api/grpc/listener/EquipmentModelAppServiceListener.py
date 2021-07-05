"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import grpc

from src.application.EquipmentModelApplicationService import EquipmentModelApplicationService
from src.domain_model.project.equipment.model.EquipmentModel import EquipmentModel
from src.domain_model.resource.exception.EquipmentModelDoesNotExistException import EquipmentModelDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.equipment_model_app_service_pb2 import \
    EquipmentModelAppService_newIdResponse, EquipmentModelAppService_equipmentModelsResponse, \
    EquipmentModelAppService_equipmentModelByIdResponse
from src.resource.proto._generated.project.equipment_model_app_service_pb2_grpc import EquipmentModelAppServiceServicer


class EquipmentModelAppServiceListener(
    CommonBaseListener, EquipmentModelAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):
        super().__init__()
        import src.port_adapter.AppDi as AppDi
        self._appService: EquipmentModelApplicationService = AppDi.instance.get(
            EquipmentModelApplicationService
        )


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(request=request, context=context, response=EquipmentModelAppService_newIdResponse)


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipment_models(self, request, context):
        response = EquipmentModelAppService_equipmentModelsResponse
        try:
            import src.port_adapter.AppDi as AppDi
            equipmentModelAppService: EquipmentModelApplicationService = (
                AppDi.instance.get(EquipmentModelApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=equipmentModelAppService.equipmentModels,
                                     responseAttribute='equipment_models'
                                     )

        except EquipmentModelDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No equipmentModels found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipment_model_by_id(self, request, context):
        response = EquipmentModelAppService_equipmentModelByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            equipmentModelAppService: EquipmentModelApplicationService = (
                AppDi.instance.get(EquipmentModelApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=equipmentModelAppService.equipmentModelById,
                                     responseAttribute='equipment_model',
                                     appServiceParams={'id': request.id}
                                     )
        except EquipmentModelDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    def _addObjectToGrpcResponse(self, obj: EquipmentModel, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "name": obj.name() if obj.name() is not None else '',
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
