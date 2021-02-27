# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import daily_check_procedure_operation_parameter_app_service_pb2 as daily__check__procedure__operation__parameter__app__service__pb2


class DailyCheckProcedureOperationParameterAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.dailyCheckProcedureOperationParameterById = channel.unary_unary(
                '/cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService/dailyCheckProcedureOperationParameterById',
                request_serializer=daily__check__procedure__operation__parameter__app__service__pb2.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdRequest.SerializeToString,
                response_deserializer=daily__check__procedure__operation__parameter__app__service__pb2.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse.FromString,
                )
        self.dailyCheckProcedureOperationParameters = channel.unary_unary(
                '/cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService/dailyCheckProcedureOperationParameters',
                request_serializer=daily__check__procedure__operation__parameter__app__service__pb2.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest.SerializeToString,
                response_deserializer=daily__check__procedure__operation__parameter__app__service__pb2.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse.FromString,
                )


class DailyCheckProcedureOperationParameterAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def dailyCheckProcedureOperationParameterById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def dailyCheckProcedureOperationParameters(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DailyCheckProcedureOperationParameterAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'dailyCheckProcedureOperationParameterById': grpc.unary_unary_rpc_method_handler(
                    servicer.dailyCheckProcedureOperationParameterById,
                    request_deserializer=daily__check__procedure__operation__parameter__app__service__pb2.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdRequest.FromString,
                    response_serializer=daily__check__procedure__operation__parameter__app__service__pb2.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse.SerializeToString,
            ),
            'dailyCheckProcedureOperationParameters': grpc.unary_unary_rpc_method_handler(
                    servicer.dailyCheckProcedureOperationParameters,
                    request_deserializer=daily__check__procedure__operation__parameter__app__service__pb2.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest.FromString,
                    response_serializer=daily__check__procedure__operation__parameter__app__service__pb2.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DailyCheckProcedureOperationParameterAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def dailyCheckProcedureOperationParameterById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService/dailyCheckProcedureOperationParameterById',
            daily__check__procedure__operation__parameter__app__service__pb2.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdRequest.SerializeToString,
            daily__check__procedure__operation__parameter__app__service__pb2.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParameterByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def dailyCheckProcedureOperationParameters(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.daily_check_procedure_operation_parameter.DailyCheckProcedureOperationParameterAppService/dailyCheckProcedureOperationParameters',
            daily__check__procedure__operation__parameter__app__service__pb2.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersRequest.SerializeToString,
            daily__check__procedure__operation__parameter__app__service__pb2.DailyCheckProcedureOperationParameterAppService_dailyCheckProcedureOperationParametersResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
