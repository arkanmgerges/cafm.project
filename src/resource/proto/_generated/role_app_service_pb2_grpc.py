# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import role_app_service_pb2 as role__app__service__pb2


class RoleAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.rolesByOrganizationType = channel.unary_unary(
            "/cafm.project.role.RoleAppService/rolesByOrganizationType",
            request_serializer=role__app__service__pb2.RoleAppService_rolesByOrganizationTypeRequest.SerializeToString,
            response_deserializer=role__app__service__pb2.RoleAppService_rolesByOrganizationTypeResponse.FromString,
        )
        self.roleByName = channel.unary_unary(
            "/cafm.project.role.RoleAppService/roleByName",
            request_serializer=role__app__service__pb2.RoleAppService_roleByNameRequest.SerializeToString,
            response_deserializer=role__app__service__pb2.RoleAppService_roleByNameResponse.FromString,
        )
        self.roleById = channel.unary_unary(
            "/cafm.project.role.RoleAppService/roleById",
            request_serializer=role__app__service__pb2.RoleAppService_roleByIdRequest.SerializeToString,
            response_deserializer=role__app__service__pb2.RoleAppService_roleByIdResponse.FromString,
        )
        self.roles = channel.unary_unary(
            "/cafm.project.role.RoleAppService/roles",
            request_serializer=role__app__service__pb2.RoleAppService_rolesRequest.SerializeToString,
            response_deserializer=role__app__service__pb2.RoleAppService_rolesResponse.FromString,
        )
        self.newId = channel.unary_unary(
            "/cafm.project.role.RoleAppService/newId",
            request_serializer=role__app__service__pb2.RoleAppService_newIdRequest.SerializeToString,
            response_deserializer=role__app__service__pb2.RoleAppService_newIdResponse.FromString,
        )


class RoleAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def rolesByOrganizationType(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def roleByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def roleById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def roles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def newId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_RoleAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "rolesByOrganizationType": grpc.unary_unary_rpc_method_handler(
            servicer.rolesByOrganizationType,
            request_deserializer=role__app__service__pb2.RoleAppService_rolesByOrganizationTypeRequest.FromString,
            response_serializer=role__app__service__pb2.RoleAppService_rolesByOrganizationTypeResponse.SerializeToString,
        ),
        "roleByName": grpc.unary_unary_rpc_method_handler(
            servicer.roleByName,
            request_deserializer=role__app__service__pb2.RoleAppService_roleByNameRequest.FromString,
            response_serializer=role__app__service__pb2.RoleAppService_roleByNameResponse.SerializeToString,
        ),
        "roleById": grpc.unary_unary_rpc_method_handler(
            servicer.roleById,
            request_deserializer=role__app__service__pb2.RoleAppService_roleByIdRequest.FromString,
            response_serializer=role__app__service__pb2.RoleAppService_roleByIdResponse.SerializeToString,
        ),
        "roles": grpc.unary_unary_rpc_method_handler(
            servicer.roles,
            request_deserializer=role__app__service__pb2.RoleAppService_rolesRequest.FromString,
            response_serializer=role__app__service__pb2.RoleAppService_rolesResponse.SerializeToString,
        ),
        "newId": grpc.unary_unary_rpc_method_handler(
            servicer.newId,
            request_deserializer=role__app__service__pb2.RoleAppService_newIdRequest.FromString,
            response_serializer=role__app__service__pb2.RoleAppService_newIdResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "cafm.project.role.RoleAppService", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class RoleAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def rolesByOrganizationType(
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
            "/cafm.project.role.RoleAppService/rolesByOrganizationType",
            role__app__service__pb2.RoleAppService_rolesByOrganizationTypeRequest.SerializeToString,
            role__app__service__pb2.RoleAppService_rolesByOrganizationTypeResponse.FromString,
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
    def roleByName(
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
            "/cafm.project.role.RoleAppService/roleByName",
            role__app__service__pb2.RoleAppService_roleByNameRequest.SerializeToString,
            role__app__service__pb2.RoleAppService_roleByNameResponse.FromString,
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
    def roleById(
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
            "/cafm.project.role.RoleAppService/roleById",
            role__app__service__pb2.RoleAppService_roleByIdRequest.SerializeToString,
            role__app__service__pb2.RoleAppService_roleByIdResponse.FromString,
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
    def roles(
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
            "/cafm.project.role.RoleAppService/roles",
            role__app__service__pb2.RoleAppService_rolesRequest.SerializeToString,
            role__app__service__pb2.RoleAppService_rolesResponse.FromString,
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
            "/cafm.project.role.RoleAppService/newId",
            role__app__service__pb2.RoleAppService_newIdRequest.SerializeToString,
            role__app__service__pb2.RoleAppService_newIdResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
