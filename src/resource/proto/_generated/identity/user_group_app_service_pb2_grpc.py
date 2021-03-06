# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from identity import user_group_app_service_pb2 as identity_dot_user__group__app__service__pb2


class UserGroupAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.user_group_by_name = channel.unary_unary(
                '/cafm.identity.user_group.UserGroupAppService/user_group_by_name',
                request_serializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByNameRequest.SerializeToString,
                response_deserializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByNameResponse.FromString,
                )
        self.user_group_by_id = channel.unary_unary(
                '/cafm.identity.user_group.UserGroupAppService/user_group_by_id',
                request_serializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByIdRequest.SerializeToString,
                response_deserializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByIdResponse.FromString,
                )
        self.user_groups = channel.unary_unary(
                '/cafm.identity.user_group.UserGroupAppService/user_groups',
                request_serializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupsRequest.SerializeToString,
                response_deserializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupsResponse.FromString,
                )
        self.new_id = channel.unary_unary(
                '/cafm.identity.user_group.UserGroupAppService/new_id',
                request_serializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_newIdRequest.SerializeToString,
                response_deserializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_newIdResponse.FromString,
                )


class UserGroupAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def user_group_by_name(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def user_group_by_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def user_groups(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def new_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserGroupAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'user_group_by_name': grpc.unary_unary_rpc_method_handler(
                    servicer.user_group_by_name,
                    request_deserializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByNameRequest.FromString,
                    response_serializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByNameResponse.SerializeToString,
            ),
            'user_group_by_id': grpc.unary_unary_rpc_method_handler(
                    servicer.user_group_by_id,
                    request_deserializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByIdRequest.FromString,
                    response_serializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByIdResponse.SerializeToString,
            ),
            'user_groups': grpc.unary_unary_rpc_method_handler(
                    servicer.user_groups,
                    request_deserializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupsRequest.FromString,
                    response_serializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupsResponse.SerializeToString,
            ),
            'new_id': grpc.unary_unary_rpc_method_handler(
                    servicer.new_id,
                    request_deserializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_newIdRequest.FromString,
                    response_serializer=identity_dot_user__group__app__service__pb2.UserGroupAppService_newIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.identity.user_group.UserGroupAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserGroupAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def user_group_by_name(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.identity.user_group.UserGroupAppService/user_group_by_name',
            identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByNameRequest.SerializeToString,
            identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def user_group_by_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.identity.user_group.UserGroupAppService/user_group_by_id',
            identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByIdRequest.SerializeToString,
            identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def user_groups(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.identity.user_group.UserGroupAppService/user_groups',
            identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupsRequest.SerializeToString,
            identity_dot_user__group__app__service__pb2.UserGroupAppService_userGroupsResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/cafm.identity.user_group.UserGroupAppService/new_id',
            identity_dot_user__group__app__service__pb2.UserGroupAppService_newIdRequest.SerializeToString,
            identity_dot_user__group__app__service__pb2.UserGroupAppService_newIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
