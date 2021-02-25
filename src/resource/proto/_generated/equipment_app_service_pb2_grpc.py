# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import equipment_app_service_pb2 as equipment__app__service__pb2


class EquipmentAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.equipmentById = channel.unary_unary(
                '/cafm.project.equipment.EquipmentAppService/equipmentById',
                request_serializer=equipment__app__service__pb2.EquipmentAppService_equipmentByIdRequest.SerializeToString,
                response_deserializer=equipment__app__service__pb2.EquipmentAppService_equipmentByIdResponse.FromString,
                )
        self.equipments = channel.unary_unary(
                '/cafm.project.equipment.EquipmentAppService/equipments',
                request_serializer=equipment__app__service__pb2.EquipmentAppService_equipmentsRequest.SerializeToString,
                response_deserializer=equipment__app__service__pb2.EquipmentAppService_equipmentsResponse.FromString,
                )


class EquipmentAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def equipmentById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def equipments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EquipmentAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'equipmentById': grpc.unary_unary_rpc_method_handler(
                    servicer.equipmentById,
                    request_deserializer=equipment__app__service__pb2.EquipmentAppService_equipmentByIdRequest.FromString,
                    response_serializer=equipment__app__service__pb2.EquipmentAppService_equipmentByIdResponse.SerializeToString,
            ),
            'equipments': grpc.unary_unary_rpc_method_handler(
                    servicer.equipments,
                    request_deserializer=equipment__app__service__pb2.EquipmentAppService_equipmentsRequest.FromString,
                    response_serializer=equipment__app__service__pb2.EquipmentAppService_equipmentsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.equipment.EquipmentAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class EquipmentAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def equipmentById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.equipment.EquipmentAppService/equipmentById',
            equipment__app__service__pb2.EquipmentAppService_equipmentByIdRequest.SerializeToString,
            equipment__app__service__pb2.EquipmentAppService_equipmentByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def equipments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.equipment.EquipmentAppService/equipments',
            equipment__app__service__pb2.EquipmentAppService_equipmentsRequest.SerializeToString,
            equipment__app__service__pb2.EquipmentAppService_equipmentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
