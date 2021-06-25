# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import standard_maintenance_procedure_operation_parameter_app_service_pb2 as standard__maintenance__procedure__operation__parameter__app__service__pb2


class StandardMaintenanceProcedureOperationParameterAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.standard_maintenance_procedure_operation_parameter_by_id = channel.unary_unary(
                '/cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameterAppService/standard_maintenance_procedure_operation_parameter_by_id',
                request_serializer=standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParameterByIdRequest.SerializeToString,
                response_deserializer=standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParameterByIdResponse.FromString,
                )
        self.standard_maintenance_procedure_operation_parameters = channel.unary_unary(
                '/cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameterAppService/standard_maintenance_procedure_operation_parameters',
                request_serializer=standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersRequest.SerializeToString,
                response_deserializer=standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersResponse.FromString,
                )
        self.standard_maintenance_procedure_operation_parameters_by_standard_maintenance_procedure_operation_id = channel.unary_unary(
                '/cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameterAppService/standard_maintenance_procedure_operation_parameters_by_standard_maintenance_procedure_operation_id',
                request_serializer=standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersByStandardMaintenanceProcedureOperationIdRequest.SerializeToString,
                response_deserializer=standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersByStandardMaintenanceProcedureOperationIdResponse.FromString,
                )
        self.new_id = channel.unary_unary(
                '/cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameterAppService/new_id',
                request_serializer=standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_newIdRequest.SerializeToString,
                response_deserializer=standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_newIdResponse.FromString,
                )


class StandardMaintenanceProcedureOperationParameterAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def standard_maintenance_procedure_operation_parameter_by_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def standard_maintenance_procedure_operation_parameters(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def standard_maintenance_procedure_operation_parameters_by_standard_maintenance_procedure_operation_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def new_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StandardMaintenanceProcedureOperationParameterAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'standard_maintenance_procedure_operation_parameter_by_id': grpc.unary_unary_rpc_method_handler(
                    servicer.standard_maintenance_procedure_operation_parameter_by_id,
                    request_deserializer=standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParameterByIdRequest.FromString,
                    response_serializer=standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParameterByIdResponse.SerializeToString,
            ),
            'standard_maintenance_procedure_operation_parameters': grpc.unary_unary_rpc_method_handler(
                    servicer.standard_maintenance_procedure_operation_parameters,
                    request_deserializer=standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersRequest.FromString,
                    response_serializer=standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersResponse.SerializeToString,
            ),
            'standard_maintenance_procedure_operation_parameters_by_standard_maintenance_procedure_operation_id': grpc.unary_unary_rpc_method_handler(
                    servicer.standard_maintenance_procedure_operation_parameters_by_standard_maintenance_procedure_operation_id,
                    request_deserializer=standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersByStandardMaintenanceProcedureOperationIdRequest.FromString,
                    response_serializer=standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersByStandardMaintenanceProcedureOperationIdResponse.SerializeToString,
            ),
            'new_id': grpc.unary_unary_rpc_method_handler(
                    servicer.new_id,
                    request_deserializer=standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_newIdRequest.FromString,
                    response_serializer=standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_newIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameterAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StandardMaintenanceProcedureOperationParameterAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def standard_maintenance_procedure_operation_parameter_by_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameterAppService/standard_maintenance_procedure_operation_parameter_by_id',
            standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParameterByIdRequest.SerializeToString,
            standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParameterByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def standard_maintenance_procedure_operation_parameters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameterAppService/standard_maintenance_procedure_operation_parameters',
            standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersRequest.SerializeToString,
            standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def standard_maintenance_procedure_operation_parameters_by_standard_maintenance_procedure_operation_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameterAppService/standard_maintenance_procedure_operation_parameters_by_standard_maintenance_procedure_operation_id',
            standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersByStandardMaintenanceProcedureOperationIdRequest.SerializeToString,
            standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_standardMaintenanceProcedureOperationParametersByStandardMaintenanceProcedureOperationIdResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/cafm.project.standard_maintenance_procedure_operation_parameter.StandardMaintenanceProcedureOperationParameterAppService/new_id',
            standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_newIdRequest.SerializeToString,
            standard__maintenance__procedure__operation__parameter__app__service__pb2.StandardMaintenanceProcedureOperationParameterAppService_newIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
