# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import maintenance_procedure_operation_app_service_pb2 as maintenance__procedure__operation__app__service__pb2


class MaintenanceProcedureOperationAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.maintenanceProcedureOperationById = channel.unary_unary(
                '/cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService/maintenanceProcedureOperationById',
                request_serializer=maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdRequest.SerializeToString,
                response_deserializer=maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdResponse.FromString,
                )
        self.maintenanceProcedureOperations = channel.unary_unary(
                '/cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService/maintenanceProcedureOperations',
                request_serializer=maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest.SerializeToString,
                response_deserializer=maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsResponse.FromString,
                )
        self.maintenanceProcedureOperationsByMaintenanceProcedureId = channel.unary_unary(
                '/cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService/maintenanceProcedureOperationsByMaintenanceProcedureId',
                request_serializer=maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest.SerializeToString,
                response_deserializer=maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdResponse.FromString,
                )
        self.newId = channel.unary_unary(
                '/cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService/newId',
                request_serializer=maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_newIdRequest.SerializeToString,
                response_deserializer=maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_newIdResponse.FromString,
                )


class MaintenanceProcedureOperationAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def maintenanceProcedureOperationById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def maintenanceProcedureOperations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def maintenanceProcedureOperationsByMaintenanceProcedureId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def newId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MaintenanceProcedureOperationAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'maintenanceProcedureOperationById': grpc.unary_unary_rpc_method_handler(
                    servicer.maintenanceProcedureOperationById,
                    request_deserializer=maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdRequest.FromString,
                    response_serializer=maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdResponse.SerializeToString,
            ),
            'maintenanceProcedureOperations': grpc.unary_unary_rpc_method_handler(
                    servicer.maintenanceProcedureOperations,
                    request_deserializer=maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest.FromString,
                    response_serializer=maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsResponse.SerializeToString,
            ),
            'maintenanceProcedureOperationsByMaintenanceProcedureId': grpc.unary_unary_rpc_method_handler(
                    servicer.maintenanceProcedureOperationsByMaintenanceProcedureId,
                    request_deserializer=maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest.FromString,
                    response_serializer=maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdResponse.SerializeToString,
            ),
            'newId': grpc.unary_unary_rpc_method_handler(
                    servicer.newId,
                    request_deserializer=maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_newIdRequest.FromString,
                    response_serializer=maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_newIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MaintenanceProcedureOperationAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def maintenanceProcedureOperationById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService/maintenanceProcedureOperationById',
            maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdRequest.SerializeToString,
            maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def maintenanceProcedureOperations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService/maintenanceProcedureOperations',
            maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsRequest.SerializeToString,
            maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def maintenanceProcedureOperationsByMaintenanceProcedureId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService/maintenanceProcedureOperationsByMaintenanceProcedureId',
            maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdRequest.SerializeToString,
            maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_maintenanceProcedureOperationsByMaintenanceProcedureIdResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/cafm.project.maintenance_procedure_operation.MaintenanceProcedureOperationAppService/newId',
            maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_newIdRequest.SerializeToString,
            maintenance__procedure__operation__app__service__pb2.MaintenanceProcedureOperationAppService_newIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)