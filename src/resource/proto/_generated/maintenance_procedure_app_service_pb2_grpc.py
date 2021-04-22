# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import maintenance_procedure_app_service_pb2 as maintenance__procedure__app__service__pb2


class MaintenanceProcedureAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.maintenanceProcedureById = channel.unary_unary(
            "/cafm.project.maintenance_procedure.MaintenanceProcedureAppService/maintenanceProcedureById",
            request_serializer=maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProcedureByIdRequest.SerializeToString,
            response_deserializer=maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProcedureByIdResponse.FromString,
        )
        self.maintenanceProcedures = channel.unary_unary(
            "/cafm.project.maintenance_procedure.MaintenanceProcedureAppService/maintenanceProcedures",
            request_serializer=maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresRequest.SerializeToString,
            response_deserializer=maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresResponse.FromString,
        )
        self.maintenanceProceduresByEquipmentId = channel.unary_unary(
            "/cafm.project.maintenance_procedure.MaintenanceProcedureAppService/maintenanceProceduresByEquipmentId",
            request_serializer=maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdRequest.SerializeToString,
            response_deserializer=maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdResponse.FromString,
        )
        self.newId = channel.unary_unary(
            "/cafm.project.maintenance_procedure.MaintenanceProcedureAppService/newId",
            request_serializer=maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_newIdRequest.SerializeToString,
            response_deserializer=maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_newIdResponse.FromString,
        )


class MaintenanceProcedureAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def maintenanceProcedureById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def maintenanceProcedures(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def maintenanceProceduresByEquipmentId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def newId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_MaintenanceProcedureAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "maintenanceProcedureById": grpc.unary_unary_rpc_method_handler(
            servicer.maintenanceProcedureById,
            request_deserializer=maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProcedureByIdRequest.FromString,
            response_serializer=maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProcedureByIdResponse.SerializeToString,
        ),
        "maintenanceProcedures": grpc.unary_unary_rpc_method_handler(
            servicer.maintenanceProcedures,
            request_deserializer=maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresRequest.FromString,
            response_serializer=maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresResponse.SerializeToString,
        ),
        "maintenanceProceduresByEquipmentId": grpc.unary_unary_rpc_method_handler(
            servicer.maintenanceProceduresByEquipmentId,
            request_deserializer=maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdRequest.FromString,
            response_serializer=maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdResponse.SerializeToString,
        ),
        "newId": grpc.unary_unary_rpc_method_handler(
            servicer.newId,
            request_deserializer=maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_newIdRequest.FromString,
            response_serializer=maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_newIdResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "cafm.project.maintenance_procedure.MaintenanceProcedureAppService",
        rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class MaintenanceProcedureAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def maintenanceProcedureById(
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
            "/cafm.project.maintenance_procedure.MaintenanceProcedureAppService/maintenanceProcedureById",
            maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProcedureByIdRequest.SerializeToString,
            maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProcedureByIdResponse.FromString,
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
    def maintenanceProcedures(
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
            "/cafm.project.maintenance_procedure.MaintenanceProcedureAppService/maintenanceProcedures",
            maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresRequest.SerializeToString,
            maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresResponse.FromString,
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
    def maintenanceProceduresByEquipmentId(
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
            "/cafm.project.maintenance_procedure.MaintenanceProcedureAppService/maintenanceProceduresByEquipmentId",
            maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdRequest.SerializeToString,
            maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_maintenanceProceduresByEquipmentIdResponse.FromString,
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
            "/cafm.project.maintenance_procedure.MaintenanceProcedureAppService/newId",
            maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_newIdRequest.SerializeToString,
            maintenance__procedure__app__service__pb2.MaintenanceProcedureAppService_newIdResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
