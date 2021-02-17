"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import time
from typing import Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.BuildingApplicationService import BuildingApplicationService
from src.application.BuildingLevelApplicationService import BuildingLevelApplicationService
from src.application.BuildingLevelRoomApplicationService import BuildingLevelRoomApplicationService
from src.application.ProjectApplicationService import ProjectApplicationService
from src.domain_model.project.Project import Project
from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.room.BuildingLevelRoom import BuildingLevelRoom
from src.domain_model.resource.exception.BuildingDoesNotExistException import BuildingDoesNotExistException
from src.domain_model.resource.exception.ProjectDoesNotExistException import ProjectDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.domain_model.token.TokenService import TokenService
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project_app_service_pb2 import ProjectAppService_projectByNameResponse, \
    ProjectAppService_projectsResponse, ProjectAppService_projectByIdResponse, ProjectAppService_buildingsResponse, \
    ProjectAppService_buildingLevelsResponse, ProjectAppService_buildingLevelRoomsResponse, \
    ProjectAppService_buildingByIdResponse, ProjectAppService_buildingLevelByIdResponse, \
    ProjectAppService_buildingLevelRoomByIdResponse
from src.resource.proto._generated.project_app_service_pb2_grpc import ProjectAppServiceServicer


class ProjectAppServiceListener(ProjectAppServiceServicer):
    """The listener function implements the rpc call as described in the .proto file"""

    def __init__(self):
        self.counter = 0
        self.last_print_time = time.time()
        self._tokenService = TokenService()

    def __str__(self):
        return self.__class__.__name__

    # region Project
    """
    c4model|cb|project:Component(project__grpc__ProjectAppServiceListener__projectByName, "Get project by name", "grpc listener", "Get a project by name")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def projectByName(self, request, context):
        try:
            token = self._token(context)
            projectAppService: ProjectApplicationService = AppDi.instance.get(ProjectApplicationService)
            project: Project = projectAppService.projectByName(name=request.name, token=token)
            response = ProjectAppService_projectByNameResponse()
            self._addObjectToResponse(obj=project, response=response)
            return response
        except ProjectDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Project does not exist')
            return ProjectAppService_projectByNameResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return ProjectAppService_projectByNameResponse()
        # except Exception as e:
        #     context.set_code(grpc.StatusCode.UNKNOWN)
        #     context.set_details(f'{e}')
        #     return identity_pb2.ProjectResponse()

    """
    c4model|cb|project:Component(project__grpc__ProjectAppServiceListener__projects, "Get projects", "grpc listener", "Get all projects")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def projects(self, request, context):
        try:
            token = self._token(context)
            metadata = context.invocation_metadata()
            resultSize = request.resultSize if request.resultSize >= 0 else 10
            claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
            logger.debug(
                f'[{ProjectAppServiceListener.projects.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}')
            projectAppService: ProjectApplicationService = AppDi.instance.get(ProjectApplicationService)

            orderData = [{"orderBy": o.orderBy, "direction": o.direction} for o in request.order]
            result: dict = projectAppService.projects(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData)
            response = ProjectAppService_projectsResponse()
            for project in result['items']:
                response.projects.add(id=project.id(), name=project.name(), cityId=project.cityId(),
                                      countryId=project.countryId(), addressLine=project.addressLine(),
                                      beneficiaryId=project.beneficiaryId(), state=project.state().value)
            response.itemCount = result['itemCount']
            logger.debug(f'[{ProjectAppServiceListener.projects.__qualname__}] - response: {response}')
            return ProjectAppService_projectsResponse(projects=response.projects, itemCount=response.itemCount)
        except ProjectDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('No projects found')
            return ProjectAppService_projectsResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return ProjectAppService_projectsResponse()

    """
    c4model|cb|project:Component(project__grpc__ProjectAppServiceListener__projectById, "Get project by id", "grpc listener", "Get a project by id")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def projectById(self, request, context):
        try:
            token = self._token(context)
            projectAppService: ProjectApplicationService = AppDi.instance.get(ProjectApplicationService)
            project: Project = projectAppService.projectById(id=request.id, token=token)
            logger.debug(f'[{ProjectAppServiceListener.projectById.__qualname__}] - response: {project}')
            response = ProjectAppService_projectByIdResponse()
            self._addObjectToResponse(obj=project, response=response)
            return response
        except ProjectDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('Project does not exist')
            return ProjectAppService_projectByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return ProjectAppService_projectByIdResponse()

    @debugLogger
    def _addObjectToResponse(self, obj: Project, response: Any):
        response.project.id = obj.id()
        response.project.name = obj.name()
        response.project.cityId = obj.cityId()
        response.project.countryId = obj.countryId()
        response.project.beneficiaryId = obj.beneficiaryId()
        response.project.addressLine = obj.addressLine()
        response.project.state = obj.state().value

    # endregion

    # region Building, Level & Room
    """
    c4model|cb|project:Component(project__grpc__ProjectAppServiceListener__buildings, "Get buildings", "grpc listener", "Get all buildings")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def buildings(self, request, context):
        try:
            token = self._token(context)
            metadata = context.invocation_metadata()
            resultSize = request.resultSize if request.resultSize >= 0 else 10
            include = request.include
            projectId = request.projectId
            claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
            logger.debug(
                f'[{ProjectAppServiceListener.buildings.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
    resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}')
            buildingAppService: BuildingApplicationService = AppDi.instance.get(BuildingApplicationService)

            orderData = [{"orderBy": o.orderBy, "direction": o.direction} for o in request.order]
            result: dict = buildingAppService.buildings(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
                include=include,
                projectId=projectId)

            rpcResponse = ProjectAppService_buildingsResponse()
            for building in result['items']:
                rpcBuilding = rpcResponse.buildings.add()
                self._addBuildingToRpcResponse(building=building, rpcResponse=rpcBuilding)
                if len(building.levels()) > 0:
                    # Add levels
                    for level in building.levels():
                        rpcLevel = rpcBuilding.buildingLevels.add()
                        self._addLevelToRpcResponse(level=level, rpcResponse=rpcLevel)
                        if len(level.rooms()) > 0:
                            # Add rooms
                            for room in level.rooms():
                                rpcRoom = rpcLevel.buildingLevelRooms.add()
                                self._addRoomToRpcResponse(room=room, rpcResponse=rpcRoom)

                rpcResponse.itemCount = result['itemCount']
            logger.debug(f'[{ProjectAppServiceListener.buildings.__qualname__}] - response: {rpcResponse}')
            return rpcResponse
        except BuildingDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('No projects found')
            return ProjectAppService_buildingsResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return ProjectAppService_buildingsResponse()

    """
    c4model|cb|project:Component(project__grpc__ProjectAppServiceListener__buildingById, "Get building by id", "grpc listener", "Get building by id")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def buildingById(self, request, context):
        try:
            token = self._token(context)
            metadata = context.invocation_metadata()
            id = request.id
            include = request.include
            claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
            logger.debug(
                f'[{ProjectAppServiceListener.buildingById.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\ttoken: {token}')
            buildingAppService: BuildingApplicationService = AppDi.instance.get(BuildingApplicationService)

            result: Building = buildingAppService.buildingById(id=id, token=token, include=include)

            rpcResponse = ProjectAppService_buildingByIdResponse()
            rpcBuilding = rpcResponse.building
            self._addBuildingToRpcResponse(building=result, rpcResponse=rpcBuilding)
            if len(result.levels()) > 0:
                # Add levels
                for level in result.levels():
                    rpcLevel = rpcBuilding.buildingLevels.add()
                    self._addLevelToRpcResponse(level=level, rpcResponse=rpcLevel)
                    if len(level.rooms()) > 0:
                        # Add rooms
                        for room in level.rooms():
                            rpcRoom = rpcLevel.buildingLevelRooms.add()
                            self._addRoomToRpcResponse(room=room, rpcResponse=rpcRoom)

            logger.debug(f'[{ProjectAppServiceListener.buildingById.__qualname__}] - response: {rpcResponse}')
            return rpcResponse
        except BuildingDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('No projects found')
            return ProjectAppService_buildingByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return ProjectAppService_buildingByIdResponse()

    """
    c4model|cb|project:Component(project__grpc__ProjectAppServiceListener__buildingLevels, "Get building levels", "grpc listener", "Get all building levels")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def buildingLevels(self, request, context):
        try:
            token = self._token(context)
            metadata = context.invocation_metadata()
            resultSize = request.resultSize if request.resultSize >= 0 else 10
            include = request.include
            buildingId = request.buildingId
            claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
            logger.debug(
                f'[{ProjectAppServiceListener.buildingLevels.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
        resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}')
            appService: BuildingLevelApplicationService = AppDi.instance.get(BuildingLevelApplicationService)

            orderData = [{"orderBy": o.orderBy, "direction": o.direction} for o in request.order]
            result: dict = appService.buildingLevels(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
                include=include,
                buildingId=buildingId)

            rpcResponse = ProjectAppService_buildingLevelsResponse()
            for level in result['items']:
                rpcLevel = rpcResponse.buildingLevels.add()
                self._addLevelToRpcResponse(level=level, rpcResponse=rpcLevel)
                if len(level.rooms()) > 0:
                    # Add rooms
                    for room in level.rooms():
                        rpcRoom = rpcLevel.buildingLevelRooms.add()
                        self._addRoomToRpcResponse(room=room, rpcResponse=rpcRoom)

                rpcResponse.itemCount = result['itemCount']
            logger.debug(f'[{ProjectAppServiceListener.buildingLevels.__qualname__}] - response: {rpcResponse}')
            return rpcResponse
        except BuildingDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('No projects found')
            return ProjectAppService_buildingLevelsResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return ProjectAppService_buildingLevelsResponse()

    """
    c4model|cb|project:Component(project__grpc__ProjectAppServiceListener__buildingLevelById, "Get building level by id", "grpc listener", "Get building level by id")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def buildingLevelById(self, request, context):
        try:
            token = self._token(context)
            metadata = context.invocation_metadata()
            id = request.id
            include = request.include
            claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
            logger.debug(
                f'[{ProjectAppServiceListener.buildingLevelById.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\ttoken: {token}')
            appService: BuildingLevelApplicationService = AppDi.instance.get(BuildingLevelApplicationService)

            result: BuildingLevel = appService.buildingLevelById(id=id, token=token, include=include)

            rpcResponse = ProjectAppService_buildingLevelByIdResponse()
            rpcLevel = rpcResponse.buildingLevel
            self._addLevelToRpcResponse(level=result, rpcResponse=rpcLevel)
            if len(result.rooms()) > 0:
                # Add rooms
                for room in result.rooms():
                    rpcRoom = rpcLevel.buildingLevelRooms.add()
                    self._addRoomToRpcResponse(room=room, rpcResponse=rpcRoom)

            logger.debug(f'[{ProjectAppServiceListener.buildingLevelById.__qualname__}] - response: {rpcResponse}')
            return rpcResponse
        except BuildingDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('No projects found')
            return ProjectAppService_buildingLevelByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return ProjectAppService_buildingLevelByIdResponse()

    """
    c4model|cb|project:Component(project__grpc__ProjectAppServiceListener__buildingLevelRooms, "Get building level rooms", "grpc listener", "Get all building level rooms")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def buildingLevelRooms(self, request, context):
        try:
            token = self._token(context)
            metadata = context.invocation_metadata()
            resultSize = request.resultSize if request.resultSize >= 0 else 10
            buildingLevelId = request.buildingLevelId
            claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
            logger.debug(
                f'[{ProjectAppServiceListener.buildingLevels.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\t \
        resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}')
            appService: BuildingLevelRoomApplicationService = AppDi.instance.get(BuildingLevelRoomApplicationService)

            orderData = [{"orderBy": o.orderBy, "direction": o.direction} for o in request.order]
            result: dict = appService.buildingLevelRooms(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
                buildingLevelId=buildingLevelId)

            rpcResponse = ProjectAppService_buildingLevelRoomsResponse()
            for room in result['items']:
                rpcRoom = rpcResponse.buildingLevelRooms.add()
                self._addRoomToRpcResponse(room=room, rpcResponse=rpcRoom)

                rpcResponse.itemCount = result['itemCount']
            logger.debug(f'[{ProjectAppServiceListener.buildingLevelRooms.__qualname__}] - response: {rpcResponse}')
            return rpcResponse
        except BuildingDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('No projects found')
            return ProjectAppService_buildingLevelRoomsResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return ProjectAppService_buildingLevelRoomsResponse()

    """
        c4model|cb|project:Component(project__grpc__ProjectAppServiceListener__buildingLevelRoomById, "Get building level room by id", "grpc listener", "Get building level room by id")
        """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def buildingLevelRoomById(self, request, context):
        try:
            token = self._token(context)
            metadata = context.invocation_metadata()
            id = request.id
            claims = self._tokenService.claimsFromToken(token=metadata[0].value) if 'token' in metadata[0] else None
            logger.debug(
                f'[{ProjectAppServiceListener.buildingLevelRoomById.__qualname__}] - metadata: {metadata}\n\t claims: {claims}\n\ttoken: {token}')
            appService: BuildingLevelRoomApplicationService = AppDi.instance.get(BuildingLevelRoomApplicationService)

            result: BuildingLevelRoom = appService.buildingLevelRoomById(id=id, token=token)

            rpcResponse = ProjectAppService_buildingLevelRoomByIdResponse()
            rpcRoom = rpcResponse.buildingLevelRoom
            self._addRoomToRpcResponse(room=result, rpcResponse=rpcRoom)

            logger.debug(f'[{ProjectAppServiceListener.buildingLevelRoomById.__qualname__}] - response: {rpcResponse}')
            return rpcResponse
        except BuildingDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details('No projects found')
            return ProjectAppService_buildingLevelRoomByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details('Un Authorized')
            return ProjectAppService_buildingLevelRoomByIdResponse()

    def _addRoomToRpcResponse(self, room: BuildingLevelRoom, rpcResponse):
        rpcResponse.id = room.id()
        rpcResponse.name = room.name()
        rpcResponse.index = room.index()
        rpcResponse.description = room.description()
        rpcResponse.buildingLevelId = room.buildingLevelId()

    def _addLevelToRpcResponse(self, level: BuildingLevel, rpcResponse):
        rpcResponse.id = level.id()
        rpcResponse.name = level.name()
        for x in level.buildingIds():
            rpcResponse.buildingIds.append(x)

    def _addBuildingToRpcResponse(self, building: Building, rpcResponse):
        rpcResponse.id = building.id()
        rpcResponse.projectId = building.projectId()
        rpcResponse.name = building.name()

    # endregion

    @debugLogger
    def _token(self, context) -> str:
        metadata = context.invocation_metadata()
        if 'token' in metadata[0]:
            return metadata[0].value
        return ''
