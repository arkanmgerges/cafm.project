# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import user_app_service_pb2 as user__app__service__pb2


class UserAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.userByEmail = channel.unary_unary(
            "/cafm.project.user.UserAppService/userByEmail",
            request_serializer=user__app__service__pb2.UserAppService_userByEmailRequest.SerializeToString,
            response_deserializer=user__app__service__pb2.UserAppService_userByEmailResponse.FromString,
        )
        self.userById = channel.unary_unary(
            "/cafm.project.user.UserAppService/userById",
            request_serializer=user__app__service__pb2.UserAppService_userByIdRequest.SerializeToString,
            response_deserializer=user__app__service__pb2.UserAppService_userByIdResponse.FromString,
        )
        self.users = channel.unary_unary(
            "/cafm.project.user.UserAppService/users",
            request_serializer=user__app__service__pb2.UserAppService_usersRequest.SerializeToString,
            response_deserializer=user__app__service__pb2.UserAppService_usersResponse.FromString,
        )
        self.newId = channel.unary_unary(
            "/cafm.project.user.UserAppService/newId",
            request_serializer=user__app__service__pb2.UserAppService_newIdRequest.SerializeToString,
            response_deserializer=user__app__service__pb2.UserAppService_newIdResponse.FromString,
        )


class UserAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def userByEmail(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def userById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def users(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def newId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_UserAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "userByEmail": grpc.unary_unary_rpc_method_handler(
            servicer.userByEmail,
            request_deserializer=user__app__service__pb2.UserAppService_userByEmailRequest.FromString,
            response_serializer=user__app__service__pb2.UserAppService_userByEmailResponse.SerializeToString,
        ),
        "userById": grpc.unary_unary_rpc_method_handler(
            servicer.userById,
            request_deserializer=user__app__service__pb2.UserAppService_userByIdRequest.FromString,
            response_serializer=user__app__service__pb2.UserAppService_userByIdResponse.SerializeToString,
        ),
        "users": grpc.unary_unary_rpc_method_handler(
            servicer.users,
            request_deserializer=user__app__service__pb2.UserAppService_usersRequest.FromString,
            response_serializer=user__app__service__pb2.UserAppService_usersResponse.SerializeToString,
        ),
        "newId": grpc.unary_unary_rpc_method_handler(
            servicer.newId,
            request_deserializer=user__app__service__pb2.UserAppService_newIdRequest.FromString,
            response_serializer=user__app__service__pb2.UserAppService_newIdResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "cafm.project.user.UserAppService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class UserAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def userByEmail(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/cafm.project.user.UserAppService/userByEmail",
            user__app__service__pb2.UserAppService_userByEmailRequest.SerializeToString,
            user__app__service__pb2.UserAppService_userByEmailResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def userById(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/cafm.project.user.UserAppService/userById",
            user__app__service__pb2.UserAppService_userByIdRequest.SerializeToString,
            user__app__service__pb2.UserAppService_userByIdResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def users(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/cafm.project.user.UserAppService/users",
            user__app__service__pb2.UserAppService_usersRequest.SerializeToString,
            user__app__service__pb2.UserAppService_usersResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def newId(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/cafm.project.user.UserAppService/newId",
            user__app__service__pb2.UserAppService_newIdRequest.SerializeToString,
            user__app__service__pb2.UserAppService_newIdResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
