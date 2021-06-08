# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import standard_equipment_app_service_pb2 as standard__equipment__app__service__pb2


class StandardEquipmentAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.standard_equipment_by_id = channel.unary_unary(
                '/cafm.project.standard_equipment.StandardEquipmentAppService/standard_equipment_by_id',
                request_serializer=standard__equipment__app__service__pb2.StandardEquipmentAppService_standardEquipmentByIdRequest.SerializeToString,
                response_deserializer=standard__equipment__app__service__pb2.StandardEquipmentAppService_standardEquipmentByIdResponse.FromString,
                )
        self.standard_equipments = channel.unary_unary(
                '/cafm.project.standard_equipment.StandardEquipmentAppService/standard_equipments',
                request_serializer=standard__equipment__app__service__pb2.StandardEquipmentAppService_standardEquipmentsRequest.SerializeToString,
                response_deserializer=standard__equipment__app__service__pb2.StandardEquipmentAppService_standardEquipmentsResponse.FromString,
                )
        self.new_id = channel.unary_unary(
                '/cafm.project.standard_equipment.StandardEquipmentAppService/new_id',
                request_serializer=standard__equipment__app__service__pb2.StandardEquipmentAppService_newIdRequest.SerializeToString,
                response_deserializer=standard__equipment__app__service__pb2.StandardEquipmentAppService_newIdResponse.FromString,
                )


class StandardEquipmentAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def standard_equipment_by_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def standard_equipments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def new_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StandardEquipmentAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'standard_equipment_by_id': grpc.unary_unary_rpc_method_handler(
                    servicer.standard_equipment_by_id,
                    request_deserializer=standard__equipment__app__service__pb2.StandardEquipmentAppService_standardEquipmentByIdRequest.FromString,
                    response_serializer=standard__equipment__app__service__pb2.StandardEquipmentAppService_standardEquipmentByIdResponse.SerializeToString,
            ),
            'standard_equipments': grpc.unary_unary_rpc_method_handler(
                    servicer.standard_equipments,
                    request_deserializer=standard__equipment__app__service__pb2.StandardEquipmentAppService_standardEquipmentsRequest.FromString,
                    response_serializer=standard__equipment__app__service__pb2.StandardEquipmentAppService_standardEquipmentsResponse.SerializeToString,
            ),
            'new_id': grpc.unary_unary_rpc_method_handler(
                    servicer.new_id,
                    request_deserializer=standard__equipment__app__service__pb2.StandardEquipmentAppService_newIdRequest.FromString,
                    response_serializer=standard__equipment__app__service__pb2.StandardEquipmentAppService_newIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.standard_equipment.StandardEquipmentAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StandardEquipmentAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def standard_equipment_by_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.standard_equipment.StandardEquipmentAppService/standard_equipment_by_id',
            standard__equipment__app__service__pb2.StandardEquipmentAppService_standardEquipmentByIdRequest.SerializeToString,
            standard__equipment__app__service__pb2.StandardEquipmentAppService_standardEquipmentByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def standard_equipments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.standard_equipment.StandardEquipmentAppService/standard_equipments',
            standard__equipment__app__service__pb2.StandardEquipmentAppService_standardEquipmentsRequest.SerializeToString,
            standard__equipment__app__service__pb2.StandardEquipmentAppService_standardEquipmentsResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/cafm.project.standard_equipment.StandardEquipmentAppService/new_id',
            standard__equipment__app__service__pb2.StandardEquipmentAppService_newIdRequest.SerializeToString,
            standard__equipment__app__service__pb2.StandardEquipmentAppService_newIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
