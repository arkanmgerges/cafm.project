# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from project import subcontractor_category_app_service_pb2 as project_dot_subcontractor__category__app__service__pb2


class SubcontractorCategoryAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.subcontractor_category_by_id = channel.unary_unary(
                '/cafm.project.subcontractor_category.SubcontractorCategoryAppService/subcontractor_category_by_id',
                request_serializer=project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_subcontractorCategoryByIdRequest.SerializeToString,
                response_deserializer=project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_subcontractorCategoryByIdResponse.FromString,
                )
        self.subcontractor_categories = channel.unary_unary(
                '/cafm.project.subcontractor_category.SubcontractorCategoryAppService/subcontractor_categories',
                request_serializer=project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_subcontractorCategoriesRequest.SerializeToString,
                response_deserializer=project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_subcontractorCategoriesResponse.FromString,
                )
        self.new_id = channel.unary_unary(
                '/cafm.project.subcontractor_category.SubcontractorCategoryAppService/new_id',
                request_serializer=project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_newIdRequest.SerializeToString,
                response_deserializer=project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_newIdResponse.FromString,
                )


class SubcontractorCategoryAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def subcontractor_category_by_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def subcontractor_categories(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def new_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SubcontractorCategoryAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'subcontractor_category_by_id': grpc.unary_unary_rpc_method_handler(
                    servicer.subcontractor_category_by_id,
                    request_deserializer=project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_subcontractorCategoryByIdRequest.FromString,
                    response_serializer=project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_subcontractorCategoryByIdResponse.SerializeToString,
            ),
            'subcontractor_categories': grpc.unary_unary_rpc_method_handler(
                    servicer.subcontractor_categories,
                    request_deserializer=project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_subcontractorCategoriesRequest.FromString,
                    response_serializer=project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_subcontractorCategoriesResponse.SerializeToString,
            ),
            'new_id': grpc.unary_unary_rpc_method_handler(
                    servicer.new_id,
                    request_deserializer=project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_newIdRequest.FromString,
                    response_serializer=project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_newIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.subcontractor_category.SubcontractorCategoryAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SubcontractorCategoryAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def subcontractor_category_by_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.subcontractor_category.SubcontractorCategoryAppService/subcontractor_category_by_id',
            project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_subcontractorCategoryByIdRequest.SerializeToString,
            project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_subcontractorCategoryByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def subcontractor_categories(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.subcontractor_category.SubcontractorCategoryAppService/subcontractor_categories',
            project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_subcontractorCategoriesRequest.SerializeToString,
            project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_subcontractorCategoriesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def new_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.subcontractor_category.SubcontractorCategoryAppService/new_id',
            project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_newIdRequest.SerializeToString,
            project_dot_subcontractor__category__app__service__pb2.SubcontractorCategoryAppService_newIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)