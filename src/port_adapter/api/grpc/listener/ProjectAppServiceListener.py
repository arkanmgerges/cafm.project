"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import time
from typing import Any

import grpc

import src.port_adapter.AppDi as AppDi
from src.application.BuildingApplicationService import BuildingApplicationService
from src.application.BuildingLevelApplicationService import (
    BuildingLevelApplicationService,
)
from src.application.BuildingLevelRoomApplicationService import (
    BuildingLevelRoomApplicationService,
)
from src.application.ProjectApplicationService import ProjectApplicationService
from src.domain_model.project.Project import Project
from src.domain_model.project.building.Building import Building
from src.domain_model.project.building.level.BuildingLevel import BuildingLevel
from src.domain_model.project.building.level.room.BuildingLevelRoom import (
    BuildingLevelRoom,
)
from src.domain_model.resource.exception.BuildingDoesNotExistException import (
    BuildingDoesNotExistException,
)
from src.domain_model.resource.exception.BuildingLevelDoesNotExistException import (
    BuildingLevelDoesNotExistException,
)
from src.domain_model.resource.exception.BuildingLevelRoomDoesNotExistException import (
    BuildingLevelRoomDoesNotExistException,
)
from src.domain_model.resource.exception.ProjectDoesNotExistException import (
    ProjectDoesNotExistException,
)
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.domain_model.resource.exception.ProjectDoesNotExistException import (
    ProjectDoesNotExistException,
)
from src.domain_model.token.TokenService import TokenService
from src.port_adapter.api.grpc.listener.BaseListener import BaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.logger import logger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project_app_service_pb2 import (
    ProjectAppService_projectsResponse,
    ProjectAppService_projectsByOrganizationIdResponse,
    ProjectAppService_projectByIdResponse,
    ProjectAppService_buildingsResponse,
    ProjectAppService_buildingLevelsResponse,
    ProjectAppService_buildingLevelRoomsResponse,
    ProjectAppService_buildingByIdResponse,
    ProjectAppService_buildingLevelByIdResponse,
    ProjectAppService_buildingLevelRoomByIdResponse,
    ProjectAppService_newIdResponse,
    ProjectAppService_newBuildingIdResponse,
    ProjectAppService_newBuildingLevelIdResponse,
    ProjectAppService_newBuildingLevelRoomIdResponse,
)
from src.resource.proto._generated.project_app_service_pb2_grpc import (
    ProjectAppServiceServicer,
)


class ProjectAppServiceListener(ProjectAppServiceServicer, BaseListener):
    """The listener function implements the rpc call as described in the .proto file"""

    def __init__(self):
        self.counter = 0
        self.last_print_time = time.time()
        self._tokenService = TokenService()

    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def newId(self, request, context):
        try:
            token = self._token(context)

            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{ProjectAppServiceListener.newId.__qualname__}] - claims: {claims}\n\t \
                    token: {token}"
            )
            appService: ProjectApplicationService = AppDi.instance.get(
                ProjectApplicationService
            )
            return ProjectAppService_newIdResponse(id=appService.newId())
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return ProjectAppService_newIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def newBuildingId(self, request, context):
        try:
            token = self._token(context)

            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{ProjectAppServiceListener.newId.__qualname__}] - claims: {claims}\n\t \
                    token: {token}"
            )
            appService: BuildingApplicationService = AppDi.instance.get(
                BuildingApplicationService
            )
            return ProjectAppService_newBuildingIdResponse(id=appService.newId())
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return ProjectAppService_newBuildingIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def newBuildingLevelId(self, request, context):
        try:
            token = self._token(context)

            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{ProjectAppServiceListener.newId.__qualname__}] - claims: {claims}\n\t \
                    token: {token}"
            )
            appService: BuildingLevelApplicationService = AppDi.instance.get(
                BuildingLevelApplicationService
            )
            return ProjectAppService_newBuildingLevelIdResponse(id=appService.newId())
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return ProjectAppService_newBuildingLevelIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def newBuildingLevelRoomId(self, request, context):
        try:
            token = self._token(context)

            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{ProjectAppServiceListener.newId.__qualname__}] - claims: {claims}\n\t \
                    token: {token}"
            )
            appService: BuildingLevelRoomApplicationService = AppDi.instance.get(
                BuildingLevelRoomApplicationService
            )
            return ProjectAppService_newBuildingLevelRoomIdResponse(
                id=appService.newId()
            )
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return ProjectAppService_newBuildingLevelRoomIdResponse()

    """
    c4model|cb|project:Component(project__grpc__ProjectAppServiceListener__projects, "Get projects", "grpc listener", "Get all projects")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def projects(self, request, context):
        try:
            token = self._token(context)

            resultSize = request.resultSize if request.resultSize >= 0 else 10
            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{ProjectAppServiceListener.projects.__qualname__}] - claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            projectAppService: ProjectApplicationService = AppDi.instance.get(
                ProjectApplicationService
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = projectAppService.projects(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
            )
            response = ProjectAppService_projectsResponse()
            for item in result["items"]:
                response.projects.add(
                    id=item.id(),
                    name=item.name(),
                    cityId=item.cityId(),
                    countryId=item.countryId(),
                    startDate=item.startDate() if item.startDate() is not None else 0,
                    beneficiaryId=item.beneficiaryId(),
                    addressLine=item.addressLine(),
                    addressLineTwo=item.addressLineTwo(),
                    state=item.state().value,
                )
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{ProjectAppServiceListener.projects.__qualname__}] - response: {response}"
            )
            return ProjectAppService_projectsResponse(
                projects=response.projects, totalItemCount=response.totalItemCount
            )
        except ProjectDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No projects found")
            return ProjectAppService_projectsResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return ProjectAppService_projectsResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def projectsByOrganizationId(self, request, context):
        try:
            token = self._token(context)

            resultSize = request.resultSize if request.resultSize >= 0 else 10
            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{ProjectAppServiceListener.projectsByOrganizationId.__qualname__}] - claims: {claims}\n\t \
resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            projectAppService: ProjectApplicationService = AppDi.instance.get(
                ProjectApplicationService
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = projectAppService.projectsByOrganizationId(
                organizationId=request.organizationId,
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
            )
            response = ProjectAppService_projectsByOrganizationIdResponse()
            for item in result["items"]:
                response.projects.add(
                    id=item.id(),
                    name=item.name(),
                    cityId=item.cityId(),
                    countryId=item.countryId(),
                    startDate=item.startDate() if item.startDate() is not None else 0,
                    beneficiaryId=item.beneficiaryId(),
                    addressLine=item.addressLine(),
                    addressLineTwo=item.addressLineTwo(),
                    state=item.state().value,
                )
            response.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{ProjectAppServiceListener.projectsByOrganizationId.__qualname__}] - response: {response}"
            )
            return ProjectAppService_projectsByOrganizationIdResponse(
                projects=response.projects, totalItemCount=response.totalItemCount
            )
        except ProjectDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No projects found")
            return ProjectAppService_projectsByOrganizationIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return ProjectAppService_projectsByOrganizationIdResponse()

    """
    c4model|cb|project:Component(project__grpc__ProjectAppServiceListener__projectById, "Get project by id", "grpc listener", "Get a project by id")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def projectById(self, request, context):
        try:
            token = self._token(context)
            appService: ProjectApplicationService = AppDi.instance.get(
                ProjectApplicationService
            )
            obj: Project = appService.projectById(id=request.id, token=token)
            logger.debug(
                f"[{ProjectAppServiceListener.projectById.__qualname__}] - response: {obj}"
            )
            response = ProjectAppService_projectByIdResponse()
            self._addObjectToResponse(obj=obj, response=response)
            return response
        except ProjectDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("project does not exist")
            return ProjectAppService_projectByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return ProjectAppService_projectByIdResponse()

    @debugLogger
    def _addObjectToResponse(self, obj: Project, response: Any):
        response.project.id = obj.id()
        response.project.name = obj.name() if obj.name() is not None else ""
        response.project.cityId = obj.cityId() if obj.cityId() is not None else 0
        response.project.countryId = (
            obj.countryId() if obj.countryId() is not None else 0
        )
        response.project.startDate = (
            obj.startDate() if obj.startDate() is not None else 0
        )
        response.project.beneficiaryId = (
            obj.beneficiaryId() if obj.beneficiaryId() is not None else ""
        )
        response.project.addressLine = (
            obj.addressLine() if obj.addressLine() is not None else ""
        )
        response.project.addressLineTwo = (
            obj.addressLineTwo() if obj.addressLineTwo() is not None else ""
        )
        response.project.state = obj.state().value
        response.project.developerName = (
            obj.developerName() if obj.developerName() is not None else ""
        )
        response.project.developerCityId = (
            obj.developerCityId() if obj.developerCityId() is not None else 0
        )
        response.project.developerCountryId = (
            obj.developerCountryId() if obj.developerCountryId() is not None else 0
        )
        response.project.developerAddressLineOne = (
            obj.developerAddressLineOne()
            if obj.developerAddressLineOne() is not None
            else ""
        )
        response.project.developerAddressLineTwo = (
            obj.developerAddressLineTwo()
            if obj.developerAddressLineTwo() is not None
            else ""
        )
        response.project.developerContact = (
            obj.developerContact() if obj.developerContact() is not None else ""
        )
        response.project.developerEmail = (
            obj.developerEmail() if obj.developerEmail() is not None else ""
        )
        response.project.developerPhoneNumber = (
            obj.developerPhoneNumber() if obj.developerPhoneNumber() is not None else ""
        )
        response.project.developerWarranty = (
            obj.developerWarranty() if obj.developerWarranty() is not None else ""
        )

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

            resultSize = request.resultSize if request.resultSize >= 0 else 10
            include = request.include
            projectId = request.projectId
            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{ProjectAppServiceListener.buildings.__qualname__}] - claims: {claims}\n\t \
    resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            buildingAppService: BuildingApplicationService = AppDi.instance.get(
                BuildingApplicationService
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = buildingAppService.buildings(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
                include=include,
                projectId=projectId,
            )

            rpcResponse = ProjectAppService_buildingsResponse()
            for building in result["items"]:
                rpcBuilding = rpcResponse.buildings.add()
                self._addBuildingToRpcResponse(
                    building=building, rpcResponse=rpcBuilding
                )
                if len(building.levels()) > 0:
                    # Add levels
                    for level in building.levels():
                        rpcLevel = rpcBuilding.buildingLevels.add()
                        self._addLevelToRpcResponse(level=level, rpcResponse=rpcLevel)
                        if len(level.rooms()) > 0:
                            # Add rooms
                            for room in level.rooms():
                                rpcRoom = rpcLevel.buildingLevelRooms.add()
                                self._addRoomToRpcResponse(
                                    room=room, rpcResponse=rpcRoom
                                )

                rpcResponse.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{ProjectAppServiceListener.buildings.__qualname__}] - response: {rpcResponse}"
            )
            return rpcResponse
        except BuildingDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No projects found")
            return ProjectAppService_buildingsResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return ProjectAppService_buildingsResponse()

    """
    c4model|cb|project:Component(project__grpc__ProjectAppServiceListener__buildingById, "Get building by id", "grpc listener", "Get building by id")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def buildingById(self, request, context):
        try:
            token = self._token(context)

            id = request.id
            include = request.include
            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{ProjectAppServiceListener.buildingById.__qualname__}] - claims: {claims}\n\ttoken: {token}"
            )
            buildingAppService: BuildingApplicationService = AppDi.instance.get(
                BuildingApplicationService
            )

            result: Building = buildingAppService.buildingById(
                id=id, token=token, include=include
            )

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

            logger.debug(
                f"[{ProjectAppServiceListener.buildingById.__qualname__}] - response: {rpcResponse}"
            )
            return rpcResponse
        except BuildingDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No projects found")
            return ProjectAppService_buildingByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return ProjectAppService_buildingByIdResponse()

    """
    c4model|cb|project:Component(project__grpc__ProjectAppServiceListener__buildingLevels, "Get building levels", "grpc listener", "Get all building levels")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def buildingLevels(self, request, context):
        try:
            token = self._token(context)

            resultSize = request.resultSize if request.resultSize >= 0 else 10
            include = request.include
            buildingId = request.buildingId
            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{ProjectAppServiceListener.buildingLevels.__qualname__}] - claims: {claims}\n\t \
        resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            appService: BuildingLevelApplicationService = AppDi.instance.get(
                BuildingLevelApplicationService
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = appService.buildingLevels(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
                include=include,
                buildingId=buildingId,
            )

            rpcResponse = ProjectAppService_buildingLevelsResponse()
            for level in result["items"]:
                rpcLevel = rpcResponse.buildingLevels.add()
                self._addLevelToRpcResponse(level=level, rpcResponse=rpcLevel)
                if len(level.rooms()) > 0:
                    # Add rooms
                    for room in level.rooms():
                        rpcRoom = rpcLevel.buildingLevelRooms.add()
                        self._addRoomToRpcResponse(room=room, rpcResponse=rpcRoom)

                rpcResponse.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{ProjectAppServiceListener.buildingLevels.__qualname__}] - response: {rpcResponse}"
            )
            return rpcResponse
        except BuildingDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No building levels found")
            return ProjectAppService_buildingLevelsResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return ProjectAppService_buildingLevelsResponse()

    """
    c4model|cb|project:Component(project__grpc__ProjectAppServiceListener__buildingLevelById, "Get building level by id", "grpc listener", "Get building level by id")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def buildingLevelById(self, request, context):
        try:
            token = self._token(context)

            id = request.id
            include = request.include
            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{ProjectAppServiceListener.buildingLevelById.__qualname__}] - claims: {claims}\n\ttoken: {token}"
            )
            appService: BuildingLevelApplicationService = AppDi.instance.get(
                BuildingLevelApplicationService
            )

            result: BuildingLevel = appService.buildingLevelById(
                id=id, token=token, include=include
            )

            rpcResponse = ProjectAppService_buildingLevelByIdResponse()
            rpcLevel = rpcResponse.buildingLevel
            self._addLevelToRpcResponse(level=result, rpcResponse=rpcLevel)
            if len(result.rooms()) > 0:
                # Add rooms
                for room in result.rooms():
                    rpcRoom = rpcLevel.buildingLevelRooms.add()
                    self._addRoomToRpcResponse(room=room, rpcResponse=rpcRoom)

            logger.debug(
                f"[{ProjectAppServiceListener.buildingLevelById.__qualname__}] - response: {rpcResponse}"
            )
            return rpcResponse
        except BuildingLevelDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No building level found")
            return ProjectAppService_buildingLevelByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return ProjectAppService_buildingLevelByIdResponse()

    """
    c4model|cb|project:Component(project__grpc__ProjectAppServiceListener__buildingLevelRooms, "Get building level rooms", "grpc listener", "Get all building level rooms")
    """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def buildingLevelRooms(self, request, context):
        try:
            token = self._token(context)

            resultSize = request.resultSize if request.resultSize >= 0 else 10
            buildingLevelId = request.buildingLevelId
            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{ProjectAppServiceListener.buildingLevels.__qualname__}] - claims: {claims}\n\t \
        resultFrom: {request.resultFrom}, resultSize: {resultSize}, token: {token}"
            )
            appService: BuildingLevelRoomApplicationService = AppDi.instance.get(
                BuildingLevelRoomApplicationService
            )

            orderData = [
                {"orderBy": o.orderBy, "direction": o.direction} for o in request.order
            ]
            result: dict = appService.buildingLevelRooms(
                resultFrom=request.resultFrom,
                resultSize=resultSize,
                token=token,
                order=orderData,
                buildingLevelId=buildingLevelId,
            )

            rpcResponse = ProjectAppService_buildingLevelRoomsResponse()
            for room in result["items"]:
                rpcRoom = rpcResponse.buildingLevelRooms.add()
                self._addRoomToRpcResponse(room=room, rpcResponse=rpcRoom)

                rpcResponse.totalItemCount = result["totalItemCount"]
            logger.debug(
                f"[{ProjectAppServiceListener.buildingLevelRooms.__qualname__}] - response: {rpcResponse}"
            )
            return rpcResponse
        except BuildingLevelRoomDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No building level rooms found")
            return ProjectAppService_buildingLevelRoomsResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return ProjectAppService_buildingLevelRoomsResponse()

    """
        c4model|cb|project:Component(project__grpc__ProjectAppServiceListener__buildingLevelRoomById, "Get building level room by id", "grpc listener", "Get building level room by id")
        """

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def buildingLevelRoomById(self, request, context):
        try:
            token = self._token(context)

            id = request.id
            claims = (
                self._tokenService.claimsFromToken(token=token)
                if "token" != ""
                else None
            )
            logger.debug(
                f"[{ProjectAppServiceListener.buildingLevelRoomById.__qualname__}] - claims: {claims}\n\ttoken: {token}"
            )
            appService: BuildingLevelRoomApplicationService = AppDi.instance.get(
                BuildingLevelRoomApplicationService
            )

            result: BuildingLevelRoom = appService.buildingLevelRoomById(
                id=id, token=token
            )

            rpcResponse = ProjectAppService_buildingLevelRoomByIdResponse()
            rpcRoom = rpcResponse.buildingLevelRoom
            self._addRoomToRpcResponse(room=result, rpcResponse=rpcRoom)

            logger.debug(
                f"[{ProjectAppServiceListener.buildingLevelRoomById.__qualname__}] - response: {rpcResponse}"
            )
            return rpcResponse
        except BuildingLevelRoomDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No building level room found")
            return ProjectAppService_buildingLevelRoomByIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
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
        rpcResponse.isSubLevel = level.isSubLevel()
        for x in level.buildingIds():
            rpcResponse.buildingIds.append(x)

    def _addBuildingToRpcResponse(self, building: Building, rpcResponse):
        rpcResponse.id = building.id()
        rpcResponse.projectId = building.projectId()
        rpcResponse.name = building.name()

    # endregion

    @debugLogger
    def _token(self, context) -> str:
        return super()._token(context=context)
