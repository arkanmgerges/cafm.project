# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from project import maintenance_procedure_app_service_pb2 as project_dot_maintenance__procedure__app__service__pb2


class MaintenanceProcedureAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.maintenance_procedure_by_id = channel.unary_unary(
                '/cafm.project.maintenance_procedure.MaintenanceProcedureAppService/maintenance_procedure_by_id',
                request_serializer=project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProcedureByIdRequest.SerializeToString,
                response_deserializer=project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProcedureByIdResponse.FromString,
                )
        self.maintenance_procedures = channel.unary_unary(
                '/cafm.project.maintenance_procedure.MaintenanceProcedureAppService/maintenance_procedures',
                request_serializer=project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresRequest.SerializeToString,
                response_deserializer=project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresResponse.FromString,
                )
        self.maintenance_procedures_by_equipment_id = channel.unary_unary(
                '/cafm.project.maintenance_procedure.MaintenanceProcedureAppService/maintenance_procedures_by_equipment_id',
                request_serializer=project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdRequest.SerializeToString,
                response_deserializer=project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdResponse.FromString,
                )
        self.new_id = channel.unary_unary(
                '/cafm.project.maintenance_procedure.MaintenanceProcedureAppService/new_id',
                request_serializer=project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_newIdRequest.SerializeToString,
                response_deserializer=project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_newIdResponse.FromString,
                )


class MaintenanceProcedureAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def maintenance_procedure_by_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def maintenance_procedures(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def maintenance_procedures_by_equipment_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def new_id(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MaintenanceProcedureAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'maintenance_procedure_by_id': grpc.unary_unary_rpc_method_handler(
                    servicer.maintenance_procedure_by_id,
                    request_deserializer=project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProcedureByIdRequest.FromString,
                    response_serializer=project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProcedureByIdResponse.SerializeToString,
            ),
            'maintenance_procedures': grpc.unary_unary_rpc_method_handler(
                    servicer.maintenance_procedures,
                    request_deserializer=project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresRequest.FromString,
                    response_serializer=project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresResponse.SerializeToString,
            ),
            'maintenance_procedures_by_equipment_id': grpc.unary_unary_rpc_method_handler(
                    servicer.maintenance_procedures_by_equipment_id,
                    request_deserializer=project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdRequest.FromString,
                    response_serializer=project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdResponse.SerializeToString,
            ),
            'new_id': grpc.unary_unary_rpc_method_handler(
                    servicer.new_id,
                    request_deserializer=project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_newIdRequest.FromString,
                    response_serializer=project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_newIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.maintenance_procedure.MaintenanceProcedureAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MaintenanceProcedureAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def maintenance_procedure_by_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.maintenance_procedure.MaintenanceProcedureAppService/maintenance_procedure_by_id',
            project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProcedureByIdRequest.SerializeToString,
            project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProcedureByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def maintenance_procedures(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.maintenance_procedure.MaintenanceProcedureAppService/maintenance_procedures',
            project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresRequest.SerializeToString,
            project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def maintenance_procedures_by_equipment_id(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.maintenance_procedure.MaintenanceProcedureAppService/maintenance_procedures_by_equipment_id',
            project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdRequest.SerializeToString,
            project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/cafm.project.maintenance_procedure.MaintenanceProcedureAppService/new_id',
            project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_newIdRequest.SerializeToString,
            project_dot_maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_newIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
