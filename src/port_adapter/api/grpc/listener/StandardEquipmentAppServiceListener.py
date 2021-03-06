"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import grpc

from src.application.StandardEquipmentApplicationService import StandardEquipmentApplicationService
from src.domain_model.project.standard_equipment.StandardEquipment import StandardEquipment
from src.domain_model.resource.exception.StandardEquipmentDoesNotExistException import StandardEquipmentDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.standard_equipment_app_service_pb2 import (
    StandardEquipmentAppService_standardEquipmentsResponse,
    StandardEquipmentAppService_standardEquipmentByIdResponse,
    StandardEquipmentAppService_newIdResponse,
)
from src.resource.proto._generated.project.standard_equipment_app_service_pb2_grpc import \
    StandardEquipmentAppServiceServicer


class StandardEquipmentAppServiceListener(
    CommonBaseListener, StandardEquipmentAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):
        super().__init__()
        import src.port_adapter.AppDi as AppDi
        self._appService: StandardEquipmentApplicationService = AppDi.instance.get(
            StandardEquipmentApplicationService
        )


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(request=request, context=context, response=StandardEquipmentAppService_newIdResponse)


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def standard_equipments(self, request, context):
        response = StandardEquipmentAppService_standardEquipmentsResponse
        try:
            import src.port_adapter.AppDi as AppDi
            standardEquipmentAppService: StandardEquipmentApplicationService = (
                AppDi.instance.get(StandardEquipmentApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=standardEquipmentAppService.standardEquipments,
                                     responseAttribute='standard_equipments'
                                     )

        except StandardEquipmentDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No standardEquipments found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def standard_equipment_by_id(self, request, context):
        response = StandardEquipmentAppService_standardEquipmentByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            standardEquipmentAppService: StandardEquipmentApplicationService = (
                AppDi.instance.get(StandardEquipmentApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=standardEquipmentAppService.standardEquipmentById,
                                     responseAttribute='standard_equipment',
                                     appServiceParams={'id': request.id}
                                     )
        except StandardEquipmentDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    def _addObjectToGrpcResponse(self, obj: StandardEquipment, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "name": obj.name() if obj.name() is not None else '',
            "standard_equipment_category_id": obj.standardEquipmentCategoryId() if obj.standardEquipmentCategoryId() is not None else '',
            "standard_equipment_category_group_id": obj.standardEquipmentCategoryGroupId() if obj.standardEquipmentCategoryGroupId() is not None else '',
            "manufacturer_id": obj.manufacturerId() if obj.manufacturerId() is not None else '',
            "equipment_model_id": obj.equipmentModelId() if obj.equipmentModelId() is not None else '',
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
