"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import grpc

from src.application.StandardEquipmentProjectCategoryApplicationService import (
    StandardEquipmentProjectCategoryApplicationService,
)
from src.domain_model.project.standard_equipment.standard_project.standard_category.StandardEquipmentProjectCategory import (
    StandardEquipmentProjectCategory,
)
from src.domain_model.resource.exception.StandardEquipmentProjectCategoryDoesNotExistException import (
    StandardEquipmentProjectCategoryDoesNotExistException,
)
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.standard_equipment_project_category_app_service_pb2 import (
    StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoriesResponse,
    StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoryByIdResponse,
    StandardEquipmentProjectCategoryAppService_newIdResponse,
)
from src.resource.proto._generated.project.standard_equipment_project_category_app_service_pb2_grpc import (
    StandardEquipmentProjectCategoryAppServiceServicer,
)
from src.resource.proto._generated.project.standard_equipment_project_category_app_service_pb2 import (
    StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoriesByOrganizationIdResponse,
)
from src.resource.logging.logger import logger


class StandardEquipmentProjectCategoryAppServiceListener(
    CommonBaseListener, StandardEquipmentProjectCategoryAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""

    def __init__(self):
        super().__init__()
        import src.port_adapter.AppDi as AppDi

        self._appService: StandardEquipmentProjectCategoryApplicationService = (
            AppDi.instance.get(StandardEquipmentProjectCategoryApplicationService)
        )

    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(
            request=request,
            context=context,
            response=StandardEquipmentProjectCategoryAppService_newIdResponse,
        )

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def standard_equipment_project_categories(self, request, context):
        response = StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoriesResponse
        try:
            import src.port_adapter.AppDi as AppDi

            standardEquipmentProjectCategoryAppService: StandardEquipmentProjectCategoryApplicationService = AppDi.instance.get(
                StandardEquipmentProjectCategoryApplicationService
            )
            return super().models(
                request=request,
                context=context,
                response=response,
                appServiceMethod=standardEquipmentProjectCategoryAppService.standardEquipmentProjectCategories,
                responseAttribute="standard_equipment_project_categories",
            )

        except StandardEquipmentProjectCategoryDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No standardEquipmentProjectCategories found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def standard_equipment_project_categories_by_organization_id(
        self, request, context
    ):
        response = StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoriesByOrganizationIdResponse
        try:
            import src.port_adapter.AppDi as AppDi

            standardEquipmentProjectCategoryAppService: StandardEquipmentProjectCategoryApplicationService = AppDi.instance.get(
                StandardEquipmentProjectCategoryApplicationService
            )
            return super().models(
                request=request,
                context=context,
                response=response,
                appServiceMethod=standardEquipmentProjectCategoryAppService.standardEquipmentProjectCategoriesByOrganizationId,
                responseAttribute="standard_equipment_project_categories",
                appServiceParams={"organizationId": request.organization_id},
            )

        except StandardEquipmentProjectCategoryDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No standardEquipmentProjectCategories found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()
        except Exception as e:
            logger.debug(e)
            raise e

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def standard_equipment_project_category_by_id(self, request, context):
        response = StandardEquipmentProjectCategoryAppService_standardEquipmentProjectCategoryByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi

            standardEquipmentProjectCategoryAppService: StandardEquipmentProjectCategoryApplicationService = AppDi.instance.get(
                StandardEquipmentProjectCategoryApplicationService
            )
            return super().oneModel(
                request=request,
                context=context,
                response=response,
                appServiceMethod=standardEquipmentProjectCategoryAppService.standardEquipmentProjectCategoryById,
                responseAttribute="standard_equipment_project_category",
                appServiceParams={"id": request.id},
            )
        except StandardEquipmentProjectCategoryDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("standard equipment project category does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Unauthorized")
            return response()

    def _addObjectToGrpcResponse(
        self, obj: StandardEquipmentProjectCategory, grpcResponseObject
    ):
        kwargs = {
            "id": obj.id(),
            "name": obj.name() if obj.name() is not None else "",
            "organization_id": obj.organizationId()
            if obj.organizationId() is not None
            else "",
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
