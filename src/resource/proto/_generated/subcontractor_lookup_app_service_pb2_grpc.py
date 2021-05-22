# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import subcontractor_lookup_app_service_pb2 as subcontractor__lookup__app__service__pb2


class SubcontractorLookupAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.lookup = channel.unary_unary(
                '/cafm.project.lookup.SubcontractorLookupAppService/lookup',
                request_serializer=subcontractor__lookup__app__service__pb2.SubcontractorLookupAppService_lookupRequest.SerializeToString,
                response_deserializer=subcontractor__lookup__app__service__pb2.SubcontractorLookupAppService_lookupResponse.FromString,
                )


class SubcontractorLookupAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def lookup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SubcontractorLookupAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'lookup': grpc.unary_unary_rpc_method_handler(
                    servicer.lookup,
                    request_deserializer=subcontractor__lookup__app__service__pb2.SubcontractorLookupAppService_lookupRequest.FromString,
                    response_serializer=subcontractor__lookup__app__service__pb2.SubcontractorLookupAppService_lookupResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.lookup.SubcontractorLookupAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SubcontractorLookupAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def lookup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.lookup.SubcontractorLookupAppService/lookup',
            subcontractor__lookup__app__service__pb2.SubcontractorLookupAppService_lookupRequest.SerializeToString,
            subcontractor__lookup__app__service__pb2.SubcontractorLookupAppService_lookupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
