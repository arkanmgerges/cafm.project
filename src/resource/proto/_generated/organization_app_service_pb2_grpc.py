# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import organization_app_service_pb2 as organization__app__service__pb2


class OrganizationAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.organizationByName = channel.unary_unary(
                '/cafm.project.organization.OrganizationAppService/organizationByName',
                request_serializer=organization__app__service__pb2.OrganizationAppService_organizationByNameRequest.SerializeToString,
                response_deserializer=organization__app__service__pb2.OrganizationAppService_organizationByNameResponse.FromString,
                )
        self.organizationById = channel.unary_unary(
                '/cafm.project.organization.OrganizationAppService/organizationById',
                request_serializer=organization__app__service__pb2.OrganizationAppService_organizationByIdRequest.SerializeToString,
                response_deserializer=organization__app__service__pb2.OrganizationAppService_organizationByIdResponse.FromString,
                )
        self.organizations = channel.unary_unary(
                '/cafm.project.organization.OrganizationAppService/organizations',
                request_serializer=organization__app__service__pb2.OrganizationAppService_organizationsRequest.SerializeToString,
                response_deserializer=organization__app__service__pb2.OrganizationAppService_organizationsResponse.FromString,
                )
        self.organizationsByType = channel.unary_unary(
                '/cafm.project.organization.OrganizationAppService/organizationsByType',
                request_serializer=organization__app__service__pb2.OrganizationAppService_organizationsByTypeRequest.SerializeToString,
                response_deserializer=organization__app__service__pb2.OrganizationAppService_organizationsByTypeResponse.FromString,
                )
        self.newId = channel.unary_unary(
                '/cafm.project.organization.OrganizationAppService/newId',
                request_serializer=organization__app__service__pb2.OrganizationAppService_newIdRequest.SerializeToString,
                response_deserializer=organization__app__service__pb2.OrganizationAppService_newIdResponse.FromString,
                )


class OrganizationAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def organizationByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def organizationById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def organizations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def organizationsByType(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def newId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_OrganizationAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'organizationByName': grpc.unary_unary_rpc_method_handler(
                    servicer.organizationByName,
                    request_deserializer=organization__app__service__pb2.OrganizationAppService_organizationByNameRequest.FromString,
                    response_serializer=organization__app__service__pb2.OrganizationAppService_organizationByNameResponse.SerializeToString,
            ),
            'organizationById': grpc.unary_unary_rpc_method_handler(
                    servicer.organizationById,
                    request_deserializer=organization__app__service__pb2.OrganizationAppService_organizationByIdRequest.FromString,
                    response_serializer=organization__app__service__pb2.OrganizationAppService_organizationByIdResponse.SerializeToString,
            ),
            'organizations': grpc.unary_unary_rpc_method_handler(
                    servicer.organizations,
                    request_deserializer=organization__app__service__pb2.OrganizationAppService_organizationsRequest.FromString,
                    response_serializer=organization__app__service__pb2.OrganizationAppService_organizationsResponse.SerializeToString,
            ),
            'organizationsByType': grpc.unary_unary_rpc_method_handler(
                    servicer.organizationsByType,
                    request_deserializer=organization__app__service__pb2.OrganizationAppService_organizationsByTypeRequest.FromString,
                    response_serializer=organization__app__service__pb2.OrganizationAppService_organizationsByTypeResponse.SerializeToString,
            ),
            'newId': grpc.unary_unary_rpc_method_handler(
                    servicer.newId,
                    request_deserializer=organization__app__service__pb2.OrganizationAppService_newIdRequest.FromString,
                    response_serializer=organization__app__service__pb2.OrganizationAppService_newIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.organization.OrganizationAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class OrganizationAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def organizationByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.organization.OrganizationAppService/organizationByName',
            organization__app__service__pb2.OrganizationAppService_organizationByNameRequest.SerializeToString,
            organization__app__service__pb2.OrganizationAppService_organizationByNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def organizationById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.organization.OrganizationAppService/organizationById',
            organization__app__service__pb2.OrganizationAppService_organizationByIdRequest.SerializeToString,
            organization__app__service__pb2.OrganizationAppService_organizationByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def organizations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.organization.OrganizationAppService/organizations',
            organization__app__service__pb2.OrganizationAppService_organizationsRequest.SerializeToString,
            organization__app__service__pb2.OrganizationAppService_organizationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def organizationsByType(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.organization.OrganizationAppService/organizationsByType',
            organization__app__service__pb2.OrganizationAppService_organizationsByTypeRequest.SerializeToString,
            organization__app__service__pb2.OrganizationAppService_organizationsByTypeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def newId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.organization.OrganizationAppService/newId',
            organization__app__service__pb2.OrganizationAppService_newIdRequest.SerializeToString,
            organization__app__service__pb2.OrganizationAppService_newIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
