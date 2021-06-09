# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import project_app_service_pb2 as project__app__service__pb2


class ProjectAppServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.projectById = channel.unary_unary(
                '/cafm.project.project.ProjectAppService/projectById',
                request_serializer=project__app__service__pb2.ProjectAppService_projectByIdRequest.SerializeToString,
                response_deserializer=project__app__service__pb2.ProjectAppService_projectByIdResponse.FromString,
                )
        self.projectsByOrganizationId = channel.unary_unary(
                '/cafm.project.project.ProjectAppService/projectsByOrganizationId',
                request_serializer=project__app__service__pb2.ProjectAppService_projectsByOrganizationIdRequest.SerializeToString,
                response_deserializer=project__app__service__pb2.ProjectAppService_projectsByOrganizationIdResponse.FromString,
                )
        self.projects = channel.unary_unary(
                '/cafm.project.project.ProjectAppService/projects',
                request_serializer=project__app__service__pb2.ProjectAppService_projectsRequest.SerializeToString,
                response_deserializer=project__app__service__pb2.ProjectAppService_projectsResponse.FromString,
                )
        self.buildings = channel.unary_unary(
                '/cafm.project.project.ProjectAppService/buildings',
                request_serializer=project__app__service__pb2.ProjectAppService_buildingsRequest.SerializeToString,
                response_deserializer=project__app__service__pb2.ProjectAppService_buildingsResponse.FromString,
                )
        self.buildingById = channel.unary_unary(
                '/cafm.project.project.ProjectAppService/buildingById',
                request_serializer=project__app__service__pb2.ProjectAppService_buildingByIdRequest.SerializeToString,
                response_deserializer=project__app__service__pb2.ProjectAppService_buildingByIdResponse.FromString,
                )
        self.buildingLevels = channel.unary_unary(
                '/cafm.project.project.ProjectAppService/buildingLevels',
                request_serializer=project__app__service__pb2.ProjectAppService_buildingLevelsRequest.SerializeToString,
                response_deserializer=project__app__service__pb2.ProjectAppService_buildingLevelsResponse.FromString,
                )
        self.buildingLevelById = channel.unary_unary(
                '/cafm.project.project.ProjectAppService/buildingLevelById',
                request_serializer=project__app__service__pb2.ProjectAppService_buildingLevelByIdRequest.SerializeToString,
                response_deserializer=project__app__service__pb2.ProjectAppService_buildingLevelByIdResponse.FromString,
                )
        self.buildingLevelRooms = channel.unary_unary(
                '/cafm.project.project.ProjectAppService/buildingLevelRooms',
                request_serializer=project__app__service__pb2.ProjectAppService_buildingLevelRoomsRequest.SerializeToString,
                response_deserializer=project__app__service__pb2.ProjectAppService_buildingLevelRoomsResponse.FromString,
                )
        self.buildingLevelRoomById = channel.unary_unary(
                '/cafm.project.project.ProjectAppService/buildingLevelRoomById',
                request_serializer=project__app__service__pb2.ProjectAppService_buildingLevelRoomByIdRequest.SerializeToString,
                response_deserializer=project__app__service__pb2.ProjectAppService_buildingLevelRoomByIdResponse.FromString,
                )
        self.newId = channel.unary_unary(
                '/cafm.project.project.ProjectAppService/newId',
                request_serializer=project__app__service__pb2.ProjectAppService_newIdRequest.SerializeToString,
                response_deserializer=project__app__service__pb2.ProjectAppService_newIdResponse.FromString,
                )
        self.newBuildingId = channel.unary_unary(
                '/cafm.project.project.ProjectAppService/newBuildingId',
                request_serializer=project__app__service__pb2.ProjectAppService_newBuildingIdRequest.SerializeToString,
                response_deserializer=project__app__service__pb2.ProjectAppService_newBuildingIdResponse.FromString,
                )
        self.newBuildingLevelId = channel.unary_unary(
                '/cafm.project.project.ProjectAppService/newBuildingLevelId',
                request_serializer=project__app__service__pb2.ProjectAppService_newBuildingLevelIdRequest.SerializeToString,
                response_deserializer=project__app__service__pb2.ProjectAppService_newBuildingLevelIdResponse.FromString,
                )
        self.newBuildingLevelRoomId = channel.unary_unary(
                '/cafm.project.project.ProjectAppService/newBuildingLevelRoomId',
                request_serializer=project__app__service__pb2.ProjectAppService_newBuildingLevelRoomIdRequest.SerializeToString,
                response_deserializer=project__app__service__pb2.ProjectAppService_newBuildingLevelRoomIdResponse.FromString,
                )


class ProjectAppServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def projectById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def projectsByOrganizationId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def projects(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def buildings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def buildingById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def buildingLevels(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def buildingLevelById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def buildingLevelRooms(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def buildingLevelRoomById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def newId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def newBuildingId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def newBuildingLevelId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def newBuildingLevelRoomId(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectAppServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'projectById': grpc.unary_unary_rpc_method_handler(
                    servicer.projectById,
                    request_deserializer=project__app__service__pb2.ProjectAppService_projectByIdRequest.FromString,
                    response_serializer=project__app__service__pb2.ProjectAppService_projectByIdResponse.SerializeToString,
            ),
            'projectsByOrganizationId': grpc.unary_unary_rpc_method_handler(
                    servicer.projectsByOrganizationId,
                    request_deserializer=project__app__service__pb2.ProjectAppService_projectsByOrganizationIdRequest.FromString,
                    response_serializer=project__app__service__pb2.ProjectAppService_projectsByOrganizationIdResponse.SerializeToString,
            ),
            'projects': grpc.unary_unary_rpc_method_handler(
                    servicer.projects,
                    request_deserializer=project__app__service__pb2.ProjectAppService_projectsRequest.FromString,
                    response_serializer=project__app__service__pb2.ProjectAppService_projectsResponse.SerializeToString,
            ),
            'buildings': grpc.unary_unary_rpc_method_handler(
                    servicer.buildings,
                    request_deserializer=project__app__service__pb2.ProjectAppService_buildingsRequest.FromString,
                    response_serializer=project__app__service__pb2.ProjectAppService_buildingsResponse.SerializeToString,
            ),
            'buildingById': grpc.unary_unary_rpc_method_handler(
                    servicer.buildingById,
                    request_deserializer=project__app__service__pb2.ProjectAppService_buildingByIdRequest.FromString,
                    response_serializer=project__app__service__pb2.ProjectAppService_buildingByIdResponse.SerializeToString,
            ),
            'buildingLevels': grpc.unary_unary_rpc_method_handler(
                    servicer.buildingLevels,
                    request_deserializer=project__app__service__pb2.ProjectAppService_buildingLevelsRequest.FromString,
                    response_serializer=project__app__service__pb2.ProjectAppService_buildingLevelsResponse.SerializeToString,
            ),
            'buildingLevelById': grpc.unary_unary_rpc_method_handler(
                    servicer.buildingLevelById,
                    request_deserializer=project__app__service__pb2.ProjectAppService_buildingLevelByIdRequest.FromString,
                    response_serializer=project__app__service__pb2.ProjectAppService_buildingLevelByIdResponse.SerializeToString,
            ),
            'buildingLevelRooms': grpc.unary_unary_rpc_method_handler(
                    servicer.buildingLevelRooms,
                    request_deserializer=project__app__service__pb2.ProjectAppService_buildingLevelRoomsRequest.FromString,
                    response_serializer=project__app__service__pb2.ProjectAppService_buildingLevelRoomsResponse.SerializeToString,
            ),
            'buildingLevelRoomById': grpc.unary_unary_rpc_method_handler(
                    servicer.buildingLevelRoomById,
                    request_deserializer=project__app__service__pb2.ProjectAppService_buildingLevelRoomByIdRequest.FromString,
                    response_serializer=project__app__service__pb2.ProjectAppService_buildingLevelRoomByIdResponse.SerializeToString,
            ),
            'newId': grpc.unary_unary_rpc_method_handler(
                    servicer.newId,
                    request_deserializer=project__app__service__pb2.ProjectAppService_newIdRequest.FromString,
                    response_serializer=project__app__service__pb2.ProjectAppService_newIdResponse.SerializeToString,
            ),
            'newBuildingId': grpc.unary_unary_rpc_method_handler(
                    servicer.newBuildingId,
                    request_deserializer=project__app__service__pb2.ProjectAppService_newBuildingIdRequest.FromString,
                    response_serializer=project__app__service__pb2.ProjectAppService_newBuildingIdResponse.SerializeToString,
            ),
            'newBuildingLevelId': grpc.unary_unary_rpc_method_handler(
                    servicer.newBuildingLevelId,
                    request_deserializer=project__app__service__pb2.ProjectAppService_newBuildingLevelIdRequest.FromString,
                    response_serializer=project__app__service__pb2.ProjectAppService_newBuildingLevelIdResponse.SerializeToString,
            ),
            'newBuildingLevelRoomId': grpc.unary_unary_rpc_method_handler(
                    servicer.newBuildingLevelRoomId,
                    request_deserializer=project__app__service__pb2.ProjectAppService_newBuildingLevelRoomIdRequest.FromString,
                    response_serializer=project__app__service__pb2.ProjectAppService_newBuildingLevelRoomIdResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cafm.project.project.ProjectAppService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProjectAppService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def projectById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.project.ProjectAppService/projectById',
            project__app__service__pb2.ProjectAppService_projectByIdRequest.SerializeToString,
            project__app__service__pb2.ProjectAppService_projectByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def projectsByOrganizationId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.project.ProjectAppService/projectsByOrganizationId',
            project__app__service__pb2.ProjectAppService_projectsByOrganizationIdRequest.SerializeToString,
            project__app__service__pb2.ProjectAppService_projectsByOrganizationIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def projects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.project.ProjectAppService/projects',
            project__app__service__pb2.ProjectAppService_projectsRequest.SerializeToString,
            project__app__service__pb2.ProjectAppService_projectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def buildings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.project.ProjectAppService/buildings',
            project__app__service__pb2.ProjectAppService_buildingsRequest.SerializeToString,
            project__app__service__pb2.ProjectAppService_buildingsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def buildingById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.project.ProjectAppService/buildingById',
            project__app__service__pb2.ProjectAppService_buildingByIdRequest.SerializeToString,
            project__app__service__pb2.ProjectAppService_buildingByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def buildingLevels(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.project.ProjectAppService/buildingLevels',
            project__app__service__pb2.ProjectAppService_buildingLevelsRequest.SerializeToString,
            project__app__service__pb2.ProjectAppService_buildingLevelsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def buildingLevelById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.project.ProjectAppService/buildingLevelById',
            project__app__service__pb2.ProjectAppService_buildingLevelByIdRequest.SerializeToString,
            project__app__service__pb2.ProjectAppService_buildingLevelByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def buildingLevelRooms(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.project.ProjectAppService/buildingLevelRooms',
            project__app__service__pb2.ProjectAppService_buildingLevelRoomsRequest.SerializeToString,
            project__app__service__pb2.ProjectAppService_buildingLevelRoomsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def buildingLevelRoomById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.project.ProjectAppService/buildingLevelRoomById',
            project__app__service__pb2.ProjectAppService_buildingLevelRoomByIdRequest.SerializeToString,
            project__app__service__pb2.ProjectAppService_buildingLevelRoomByIdResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/cafm.project.project.ProjectAppService/newId',
            project__app__service__pb2.ProjectAppService_newIdRequest.SerializeToString,
            project__app__service__pb2.ProjectAppService_newIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def newBuildingId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.project.ProjectAppService/newBuildingId',
            project__app__service__pb2.ProjectAppService_newBuildingIdRequest.SerializeToString,
            project__app__service__pb2.ProjectAppService_newBuildingIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def newBuildingLevelId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.project.ProjectAppService/newBuildingLevelId',
            project__app__service__pb2.ProjectAppService_newBuildingLevelIdRequest.SerializeToString,
            project__app__service__pb2.ProjectAppService_newBuildingLevelIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def newBuildingLevelRoomId(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cafm.project.project.ProjectAppService/newBuildingLevelRoomId',
            project__app__service__pb2.ProjectAppService_newBuildingLevelRoomIdRequest.SerializeToString,
            project__app__service__pb2.ProjectAppService_newBuildingLevelRoomIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
