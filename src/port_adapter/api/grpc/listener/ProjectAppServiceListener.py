"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
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
from src.domain_model.resource.exception.BuildingLevelDoesNotExistException import BuildingLevelDoesNotExistException
from src.domain_model.resource.exception.BuildingLevelRoomDoesNotExistException import \
    BuildingLevelRoomDoesNotExistException
from src.domain_model.resource.exception.ProjectDoesNotExistException import ProjectDoesNotExistException
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.api.grpc.listener.CommonBaseListener import CommonBaseListener
from src.resource.logging.decorator import debugLogger
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project_app_service_pb2 import (
    ProjectAppService_projectsResponse,
    ProjectAppService_projectByIdResponse,
    ProjectAppService_newIdResponse, ProjectAppService_newBuildingIdResponse,
    ProjectAppService_newBuildingLevelIdResponse, ProjectAppService_newBuildingLevelRoomIdResponse,
    ProjectAppService_buildingsResponse, ProjectAppService_buildingByIdResponse,
    ProjectAppService_buildingLevelsResponse, ProjectAppService_buildingLevelByIdResponse,
    ProjectAppService_buildingLevelRoomsResponse, ProjectAppService_buildingLevelRoomByIdResponse,
    ProjectAppService_projectsByOrganizationIdResponse,
)
from src.resource.proto._generated.project_app_service_pb2_grpc import (
    ProjectAppServiceServicer,
)


class ProjectAppServiceListener(
    CommonBaseListener, ProjectAppServiceServicer
):
    """The listener function implements the rpc call as described in the .proto file"""
    def __init__(self):

        self._appService: ProjectApplicationService = AppDi.instance.get(
            ProjectApplicationService
        )
        super().__init__()


    def __str__(self):
        return self.__class__.__name__

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_id(self, request, context):
        self._appService: ProjectApplicationService = AppDi.instance.get(
            ProjectApplicationService
        )
        return super().newId(request=request, context=context, response=ProjectAppService_newIdResponse)

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_building_id(self, request, context):
        from src.application.BuildingApplicationService import BuildingApplicationService
        self._appService = AppDi.instance.get(BuildingApplicationService)
        return super().newId(request=request, context=context, response=ProjectAppService_newBuildingIdResponse)

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_building_level_id(self, request, context):
        from src.application.BuildingLevelApplicationService import BuildingLevelApplicationService
        self._appService = AppDi.instance.get(BuildingLevelApplicationService)
        return super().newId(request=request, context=context, response=ProjectAppService_newBuildingLevelIdResponse)

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def new_building_level_room_id(self, request, context):
        from src.application.BuildingLevelRoomApplicationService import BuildingLevelRoomApplicationService
        self._appService = AppDi.instance.get(BuildingLevelRoomApplicationService)
        return super().newId(request=request, context=context, response=ProjectAppService_newBuildingLevelRoomIdResponse)

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def projects_by_state(self, request, context):
        response = ProjectAppService_projectsResponse
        try:
            projectAppService: ProjectApplicationService = (
                AppDi.instance.get(ProjectApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                  appServiceMethod=projectAppService.projectsByState,
                                  responseAttribute='projects',
                                  appServiceParams={"state": request.state}
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
    def projects_by_organization_id(self, request, context):
        response = ProjectAppService_projectsByOrganizationIdResponse
        try:
            projectAppService: ProjectApplicationService = (
                AppDi.instance.get(ProjectApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                  appServiceMethod=projectAppService.projectsByOrganizationId,
                                  responseAttribute='projects',
                                  appServiceParams={"organizationId": request.organization_id}
                                  )
        except ProjectDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No projects found")
            return ProjectAppService_projectsByOrganizationIdResponse()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return ProjectAppService_projectsByOrganizationIdResponse()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def projects(self, request, context):
        response = ProjectAppService_projectsResponse
        try:
            projectAppService: ProjectApplicationService = (
                AppDi.instance.get(ProjectApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                     appServiceMethod=projectAppService.projects,
                                     responseAttribute='projects'
                                     )

        except ProjectDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No projects found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def buildings(self, request, context):
        response = ProjectAppService_buildingsResponse
        try:
            buildingAppService: BuildingApplicationService = (
                AppDi.instance.get(BuildingApplicationService)
            )
            return super().models(request=request, context=context, response=response,
                                  appServiceMethod=buildingAppService.buildings,
                                  responseAttribute='buildings',
                                  appServiceParams={"include": request.include, "projectId": request.project_id}
                                  )
        except BuildingDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No projects found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def building_by_id(self, request, context):
        response = ProjectAppService_buildingByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            appService: BuildingApplicationService = (
                AppDi.instance.get(BuildingApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                    response=response,
                                    appServiceMethod=appService.buildingById,
                                    responseAttribute='building',
                                    appServiceParams={'id': request.id, "include": request.include}
                                    )
        except BuildingDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No projects found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def building_levels(self, request, context):
        response = ProjectAppService_buildingLevelsResponse
        try:
            buildingLevelAppService: BuildingLevelApplicationService = (AppDi.instance.get(BuildingLevelApplicationService))
            return super().models(request=request, context=context, response=response,
                                  appServiceMethod=buildingLevelAppService.buildingLevels,
                                  responseAttribute='building_levels',
                                  appServiceParams={"include": request.include, "buildingId": request.building_id}
                                  )
        except BuildingDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No building found")
            return response()
        except BuildingLevelDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No building level(s) found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def building_level_by_id(self, request, context):
        response = ProjectAppService_buildingLevelByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            appService: BuildingLevelApplicationService = (
                AppDi.instance.get(BuildingLevelApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                    response=response,
                                    appServiceMethod=appService.buildingLevelById,
                                    responseAttribute='building_level',
                                    appServiceParams={'id': request.id, "include": request.include}
                                    )
        except BuildingDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No building found")
            return response()
        except BuildingLevelDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No building level found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def building_level_rooms(self, request, context):
        response = ProjectAppService_buildingLevelRoomsResponse
        try:
            appService: BuildingLevelRoomApplicationService = (
                AppDi.instance.get(BuildingLevelRoomApplicationService))
            return super().models(request=request, context=context, response=response,
                                  appServiceMethod=appService.buildingLevelRooms,
                                  responseAttribute='building_level_rooms',
                                  appServiceParams={"buildingLevelId": request.building_level_id}
                                  )
        except BuildingDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No building found")
            return response()
        except BuildingLevelDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No building level(s) found")
            return response()
        except BuildingLevelRoomDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No building level room(s) found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()

    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def building_level_room_by_id(self, request, context):
        response = ProjectAppService_buildingLevelRoomByIdResponse
        try:
            appService: BuildingLevelRoomApplicationService = (
                AppDi.instance.get(BuildingLevelRoomApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                    response=response,
                                    appServiceMethod=appService.buildingLevelRoomById,
                                    responseAttribute='building_level_room',
                                    appServiceParams={'id': request.id}
                                    )

        except BuildingDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No building found")
            return response()
        except BuildingLevelDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No building level(s) found")
            return response()
        except BuildingLevelRoomDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("No building level room(s) found")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()


    @debugLogger
    @OpenTelemetry.grpcTraceOTel
    def project_by_id(self, request, context):
        response = ProjectAppService_projectByIdResponse
        try:
            import src.port_adapter.AppDi as AppDi
            projectAppService: ProjectApplicationService = (
                AppDi.instance.get(ProjectApplicationService)
            )
            return super().oneModel(request=request, context=context,
                                     response=response,
                                     appServiceMethod=projectAppService.projectById,
                                     responseAttribute='project',
                                     appServiceParams={'id': request.id}
                                     )
        except ProjectDoesNotExistException:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("daily check procedure does not exist")
            return response()
        except UnAuthorizedException:
            context.set_code(grpc.StatusCode.PERMISSION_DENIED)
            context.set_details("Un Authorized")
            return response()


    def _addObjectToGrpcResponse(self, obj: Any, grpcResponseObject):
        if isinstance(obj, Project):
            self._addProjectObjectToGrpcResponse(obj, grpcResponseObject)
        elif isinstance(obj, Building):
            self._addBuildingObjectToGrpcResponse(obj, grpcResponseObject)
        elif isinstance(obj, BuildingLevel):
            self._addBuildingLevelObjectToGrpcResponse(obj, grpcResponseObject)
        elif isinstance(obj, BuildingLevelRoom):
            self._addBuildingLevelRoomObjectToGrpcResponse(obj, grpcResponseObject)

    def _addBuildingObjectToGrpcResponse(self, obj: Building, grpcResponseObject):
        grpcResponseObject.id = obj.id() if obj.id() is not None else ''
        grpcResponseObject.project_id = obj.projectId() if obj.projectId() is not None else ''
        grpcResponseObject.name = obj.name() if obj.name() is not None else ''
        if len(obj.levels()) > 0:
            # Add levels
            for level in obj.levels():
                grpcLevel = grpcResponseObject.building_levels.add()
                self._addBuildingLevelObjectToGrpcResponse(obj=level, grpcResponseObject=grpcLevel)

    def _addBuildingLevelObjectToGrpcResponse(self, obj: BuildingLevel, grpcResponseObject):
        grpcResponseObject.id = obj.id() if obj.id() is not None else ''
        grpcResponseObject.name = obj.name() if obj.name() is not None else ''
        grpcResponseObject.is_sub_level = obj.isSubLevel() if obj.isSubLevel() is not None else False
        for x in obj.buildingIds():
            grpcResponseObject.building_ids.append(x)
        if len(obj.rooms()) > 0:
            # Add rooms
            for room in obj.rooms():
                grpcRoom = grpcResponseObject.building_level_rooms.add()
                self._addBuildingLevelRoomObjectToGrpcResponse(
                    obj=room, grpcResponseObject=grpcRoom)

    def _addBuildingLevelRoomObjectToGrpcResponse(self, obj: BuildingLevelRoom, grpcResponseObject):
        grpcResponseObject.id = obj.id() if obj.id() is not None else ''
        grpcResponseObject.name = obj.name() if obj.name() is not None else ''
        grpcResponseObject.index = obj.index() if obj.index() is not None else 0
        grpcResponseObject.description = obj.description() if obj.description() is not None else ''
        grpcResponseObject.building_level_id = obj.buildingLevelId() if obj.buildingLevelId() is not None else ''

    def _addProjectObjectToGrpcResponse(self, obj: Project, grpcResponseObject):
        kwargs = {
            "id": obj.id(),
            "name": obj.name() if obj.name() is not None else '',
            "city_id": obj.cityId() if obj.cityId() is not None else 0,
            "country_id": obj.countryId() if obj.countryId() is not None else 0,
            "start_date": obj.startDate() if obj.startDate() is not None else 0,
            "beneficiary_id": obj.beneficiaryId() if obj.beneficiaryId() is not None else '',
            "address_line": obj.addressLine() if obj.addressLine() is not None else '',
            "state": obj.state().value if obj.state() is not None else '',
            "address_line_two": obj.addressLineTwo() if obj.addressLineTwo() is not None else '',
            "developer_name": obj.developerName() if obj.developerName() is not None else '',
            "developer_city_id": obj.developerCityId() if obj.developerCityId() is not None else 0,
            "developer_country_id": obj.developerCountryId() if obj.developerCountryId() is not None else 0,
            "developer_address_line_one": obj.developerAddressLineOne() if obj.developerAddressLineOne() is not None else '',
            "developer_address_line_two": obj.developerAddressLineTwo() if obj.developerAddressLineTwo() is not None else '',
            "developer_contact": obj.developerContact() if obj.developerContact() is not None else '',
            "developer_email": obj.developerEmail() if obj.developerEmail() is not None else '',
            "developer_phone_number": obj.developerPhoneNumber() if obj.developerPhoneNumber() is not None else '',
            "developer_warranty": obj.developerWarranty() if obj.developerWarranty() is not None else '',
        }
        for k, v in kwargs.items():
            setattr(grpcResponseObject, k, v)
