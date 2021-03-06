# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from identity import policy_app_service_pb2 as identity_dot_policy__app__service__pb2


class PolicyAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.users_include_access_roles = channel.unary_unary(
                '/cafm.identity.policy.PolicyAppService/users_include_access_roles',
                request_serializer=identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeAccessRolesRequest.SerializeToString,
                response_deserializer=identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeAccessRolesResponse.FromString,
                )
        self.users_include_roles = channel.unary_unary(
                '/cafm.identity.policy.PolicyAppService/users_include_roles',
                request_serializer=identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeRolesRequest.SerializeToString,
                response_deserializer=identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeRolesResponse.FromString,
                )
        self.users_include_realms_and_roles = channel.unary_unary(
                '/cafm.identity.policy.PolicyAppService/users_include_realms_and_roles',
                request_serializer=identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeRealmsAndRolesRequest.SerializeToString,
                response_deserializer=identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeRealmsAndRolesResponse.FromString,
                )
        self.realms_include_users_include_roles = channel.unary_unary(
                '/cafm.identity.policy.PolicyAppService/realms_include_users_include_roles',
                request_serializer=identity_dot_policy__app__service__pb2.PolicyAppService_realmsIncludeUsersIncludeRolesRequest.SerializeToString,
                response_deserializer=identity_dot_policy__app__service__pb2.PolicyAppService_realmsIncludeUsersIncludeRolesResponse.FromString,
                )
        self.projects_include_realms_include_users_include_roles = channel.unary_unary(
                '/cafm.identity.policy.PolicyAppService/projects_include_realms_include_users_include_roles',
                request_serializer=identity_dot_policy__app__service__pb2.PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesRequest.SerializeToString,
                response_deserializer=identity_dot_policy__app__service__pb2.PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesResponse.FromString,
                )


class PolicyAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def users_include_access_roles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def users_include_roles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def users_include_realms_and_roles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def realms_include_users_include_roles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def projects_include_realms_include_users_include_roles(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PolicyAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'users_include_access_roles': grpc.unary_unary_rpc_method_handler(
                    servicer.users_include_access_roles,
                    request_deserializer=identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeAccessRolesRequest.FromString,
                    response_serializer=identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeAccessRolesResponse.SerializeToString,
            ),
            'users_include_roles': grpc.unary_unary_rpc_method_handler(
                    servicer.users_include_roles,
                    request_deserializer=identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeRolesRequest.FromString,
                    response_serializer=identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeRolesResponse.SerializeToString,
            ),
            'users_include_realms_and_roles': grpc.unary_unary_rpc_method_handler(
                    servicer.users_include_realms_and_roles,
                    request_deserializer=identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeRealmsAndRolesRequest.FromString,
                    response_serializer=identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeRealmsAndRolesResponse.SerializeToString,
            ),
            'realms_include_users_include_roles': grpc.unary_unary_rpc_method_handler(
                    servicer.realms_include_users_include_roles,
                    request_deserializer=identity_dot_policy__app__service__pb2.PolicyAppService_realmsIncludeUsersIncludeRolesRequest.FromString,
                    response_serializer=identity_dot_policy__app__service__pb2.PolicyAppService_realmsIncludeUsersIncludeRolesResponse.SerializeToString,
            ),
            'projects_include_realms_include_users_include_roles': grpc.unary_unary_rpc_method_handler(
                    servicer.projects_include_realms_include_users_include_roles,
                    request_deserializer=identity_dot_policy__app__service__pb2.PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesRequest.FromString,
                    response_serializer=identity_dot_policy__app__service__pb2.PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.identity.policy.PolicyAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PolicyAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def users_include_access_roles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.identity.policy.PolicyAppService/users_include_access_roles',
            identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeAccessRolesRequest.SerializeToString,
            identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeAccessRolesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def users_include_roles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.identity.policy.PolicyAppService/users_include_roles',
            identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeRolesRequest.SerializeToString,
            identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeRolesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def users_include_realms_and_roles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.identity.policy.PolicyAppService/users_include_realms_and_roles',
            identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeRealmsAndRolesRequest.SerializeToString,
            identity_dot_policy__app__service__pb2.PolicyAppService_usersIncludeRealmsAndRolesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def realms_include_users_include_roles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.identity.policy.PolicyAppService/realms_include_users_include_roles',
            identity_dot_policy__app__service__pb2.PolicyAppService_realmsIncludeUsersIncludeRolesRequest.SerializeToString,
            identity_dot_policy__app__service__pb2.PolicyAppService_realmsIncludeUsersIncludeRolesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def projects_include_realms_include_users_include_roles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.identity.policy.PolicyAppService/projects_include_realms_include_users_include_roles',
            identity_dot_policy__app__service__pb2.PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesRequest.SerializeToString,
            identity_dot_policy__app__service__pb2.PolicyAppService_projectsIncludeRealmsIncludeUsersIncludeRolesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
