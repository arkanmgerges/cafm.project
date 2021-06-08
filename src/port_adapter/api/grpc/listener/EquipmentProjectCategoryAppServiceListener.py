"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import grpc

from src.application.EquipmentProjectCategoryApplicationService import EquipmentProjectCategoryApplicationService
from src.domain_model.project.equipment.project_category.EquipmentProjectCategory import EquipmentProjectCategory
from src.domain_model.resource.exception.EquipmentProjectCategoryDoesNotExistException import \
    EquipmentProjectCategoryDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.equipment_project_category_app_service_pb2 import (
    EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse,
    EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse,
    EquipmentProjectCategoryAppService_newIdResponse,
    EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse,
)
from src.resource.proto._generated.equipment_project_category_app_service_pb2_grpc import (
    EquipmentProjectCategoryAppServiceServicer,
)


class EquipmentProjectCategoryAppServiceListener(
    CommonBaseListener, EquipmentProjectCategoryAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):
        import src.port_adapter.AppDi as AppDi
        self._appService: EquipmentProjectCategoryApplicationService = AppDi.instance.get(
            EquipmentProjectCategoryApplicationService
        )
        super().__init__()


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(request=request, context=context, response=EquipmentProjectCategoryAppService_newIdResponse)


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipment_project_categories(self, request, context):
        response = EquipmentProjectCategoryAppService_equipmentProjectCategoriesResponse
        try:
            import src.port_adapter.AppDi as AppDi
            equipmentProjectCategoryAppService: EquipmentProjectCategoryApplicationService = (
                AppDi.instance.get(EquipmentProjectCategoryApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=equipmentProjectCategoryAppService.equipmentProjectCategories,
                                     responseAttribute='equipment_project_categories'
                                     )

        except EquipmentProjectCategoryDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No equipmentProjectCategories found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipment_category_groups_by_equipment_project_category_id(self, request, context):
        response = EquipmentProjectCategoryAppService_equipmentCategoryGroupsByEquipmentProjectCategoryIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            equipmentProjectCategoryAppService: EquipmentProjectCategoryApplicationService = (
                AppDi.instance.get(EquipmentProjectCategoryApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=equipmentProjectCategoryAppService.equipmentCategoryGroupsByEquipmentProjectCategoryId,
                                     responseAttribute='equipment_category_groups',
                                     appServiceParams={"id": request.id}
                                     )

        except EquipmentProjectCategoryDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No equipmentProjectCategories found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def equipment_project_category_by_id(self, request, context):
        response = EquipmentProjectCategoryAppService_equipmentProjectCategoryByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            equipmentProjectCategoryAppService: EquipmentProjectCategoryApplicationService = (
                AppDi.instance.get(EquipmentProjectCategoryApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=equipmentProjectCategoryAppService.equipmentProjectCategoryById,
                                     responseAttribute='equipment_project_category',
                                     appServiceParams={'id': request.id}
                                     )
        except EquipmentProjectCategoryDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    def _addObjectToGrpcResponse(self, obj: EquipmentProjectCategory, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "name": obj.name(),
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
