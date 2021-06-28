"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



import grpc

from src.application.TagApplicationService import TagApplicationService
from src.domain_model.tag.Tag import Tag
from src.domain_model.resource.exception.TagDoesNotExistException import TagDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project.tag_app_service_pb2 import (
    TagAppService_tagsResponse,
    TagAppService_tagByIdResponse,
    TagAppService_newIdResponse,
)
from src.resource.proto._generated.project.tag_app_service_pb2_grpc import TagAppServiceServicer


class TagAppServiceListener(
    CommonBaseListener, TagAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):
        super().__init__()
        import src.port_adapter.AppDi as AppDi
        self._appService: TagApplicationService = AppDi.instance.get(
            TagApplicationService
        )
        


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        return super().newId(request=request, context=context, response=TagAppService_newIdResponse)


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def tags(self, request, context):
        response = TagAppService_tagsResponse
        try:
            import src.port_adapter.AppDi as AppDi
            tagAppService: TagApplicationService = (
                AppDi.instance.get(TagApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=tagAppService.tags,
                                     responseAttribute='tags'
                                     )

        except TagDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No tags found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def tag_by_id(self, request, context):
        response = TagAppService_tagByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            tagAppService: TagApplicationService = (
                AppDi.instance.get(TagApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=tagAppService.tagById,
                                     responseAttribute='tag',
                                     appServiceParams={'id': request.id}
                                     )
        except TagDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    def _addObjectToGrpcResponse(self, obj: Tag, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "name": obj.name() if obj.name() is not None else '',
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
