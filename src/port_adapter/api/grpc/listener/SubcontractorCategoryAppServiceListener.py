"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import grpc

from src.application.SubcontractorCategoryApplicationService import SubcontractorCategoryApplicationService
from src.domain_model.resource.exception.SubcontractorCategoryDoesNotExistException import \
    SubcontractorCategoryDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.domain_model.subcontractor.category.SubcontractorCategory import SubcontractorCategory
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.subcontractor_category_app_service_pb2 import (
    SubcontractorCategoryAppService_subcontractorCategoriesResponse,
    SubcontractorCategoryAppService_subcontractorCategoryByIdResponse,
    SubcontractorCategoryAppService_newIdResponse,
)
from src.resource.proto._generated.subcontractor_category_app_service_pb2_grpc import (
    SubcontractorCategoryAppServiceServicer,
)


class SubcontractorCategoryAppServiceListener(
    CommonBaseListener, SubcontractorCategoryAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):
        import src.port_adapter.AppDi as AppDi
        self._appService: SubcontractorCategoryApplicationService = AppDi.instance.get(
            SubcontractorCategoryApplicationService
        )
        super().__init__()


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(request=request, context=context, response=SubcontractorCategoryAppService_newIdResponse)


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def subcontractor_categories(self, request, context):
        response = SubcontractorCategoryAppService_subcontractorCategoriesResponse
        try:
            import src.port_adapter.AppDi as AppDi
            subcontractorCategoryAppService: SubcontractorCategoryApplicationService = (
                AppDi.instance.get(SubcontractorCategoryApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=subcontractorCategoryAppService.subcontractorCategories,
                                     responseAttribute='subcontractor_categories'
                                     )

        except SubcontractorCategoryDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No subcontractorCategories found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def subcontractor_category_by_id(self, request, context):
        response = SubcontractorCategoryAppService_subcontractorCategoryByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            subcontractorCategoryAppService: SubcontractorCategoryApplicationService = (
                AppDi.instance.get(SubcontractorCategoryApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=subcontractorCategoryAppService.subcontractorCategoryById,
                                     responseAttribute='subcontractor_category',
                                     appServiceParams={'id': request.id}
                                     )
        except SubcontractorCategoryDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    def _addObjectToGrpcResponse(self, obj: SubcontractorCategory, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "name": obj.name() if obj.name() is not None else '',
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
