"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import random
# https://www.youtube.com/watch?v=dQK0VLahrDk&list=PLXs6ze70rLY9u0X6qz_91bCvsjq3Kqn_O&index=5
from datetime import datetime

import src.port_adapter.AppDi as AppDi
import src.resource.proto._generated
from src.port_adapter.api.grpc.listener.DailyCheckProcedureAppServiceListener import (
    DailyCheckProcedureAppServiceListener,
)
from src.port_adapter.api.grpc.listener.DailyCheckProcedureOperationAppServiceListener import (
    DailyCheckProcedureOperationAppServiceListener,
)
from src.port_adapter.api.grpc.listener.DailyCheckProcedureOperationParameterAppServiceListener import (
    DailyCheckProcedureOperationParameterAppServiceListener,
)
from src.port_adapter.api.grpc.listener.EquipmentAppServiceListener import (
    EquipmentAppServiceListener,
)
from src.port_adapter.api.grpc.listener.EquipmentCategoryGroupAppServiceListener import (
    EquipmentCategoryGroupAppServiceListener,
)
from src.port_adapter.api.grpc.listener.EquipmentInputAppServiceListener import (
    EquipmentInputAppServiceListener,
)
from src.port_adapter.api.grpc.listener.EquipmentModelAppServiceListener import (
    EquipmentModelAppServiceListener,
)
from src.port_adapter.api.grpc.listener.EquipmentProjectCategoryAppServiceListener import (
    EquipmentProjectCategoryAppServiceListener,
)
from src.port_adapter.api.grpc.listener.MaintenanceProcedureAppServiceListener import (
    MaintenanceProcedureAppServiceListener,
)
from src.port_adapter.api.grpc.listener.MaintenanceProcedureOperationAppServiceListener import (
    MaintenanceProcedureOperationAppServiceListener,
)
from src.port_adapter.api.grpc.listener.MaintenanceProcedureOperationParameterAppServiceListener import (
    MaintenanceProcedureOperationParameterAppServiceListener,
)
from src.port_adapter.api.grpc.listener.ManufacturerAppServiceListener import (
    ManufacturerAppServiceListener,
)
from src.port_adapter.api.grpc.listener.OrganizationAppServiceListener import (
    OrganizationAppServiceListener,
)
from src.port_adapter.api.grpc.listener.ProjectAppServiceListener import (
    ProjectAppServiceListener,
)
from src.port_adapter.api.grpc.listener.RoleAppServiceListener import (
    RoleAppServiceListener,
)
from src.port_adapter.api.grpc.listener.StandardEquipmentAppServiceListener import (
    StandardEquipmentAppServiceListener,
)
from src.port_adapter.api.grpc.listener.StandardEquipmentCategoryAppServiceListener import (
    StandardEquipmentCategoryAppServiceListener,
)
from src.port_adapter.api.grpc.listener.StandardEquipmentCategoryGroupAppServiceListener import (
    StandardEquipmentCategoryGroupAppServiceListener,
)
from src.port_adapter.api.grpc.listener.StandardMaintenanceProcedureAppServiceListener import (
    StandardMaintenanceProcedureAppServiceListener,
)
from src.port_adapter.api.grpc.listener.SubcontractorAppServiceListener import (
    SubcontractorAppServiceListener,
)
from src.port_adapter.api.grpc.listener.SubcontractorCategoryAppServiceListener import (
    SubcontractorCategoryAppServiceListener,
)
from src.port_adapter.api.grpc.listener.UnitAppServiceListener import (
    UnitAppServiceListener,
)
from src.port_adapter.api.grpc.listener.UserAppServiceListener import (
    UserAppServiceListener,
)
from src.port_adapter.api.grpc.listener.lookup.OrganizationLookupAppServiceListener import \
    OrganizationLookupAppServiceListener
from src.port_adapter.api.grpc.listener.lookup.UserLookupAppServiceListener import (
    UserLookupAppServiceListener,
)
from src.port_adapter.api.grpc.listener.lookup.ProjectLookupAppServiceListener import (
    ProjectLookupAppServiceListener,
)
from src.port_adapter.api.grpc.listener.lookup.DailyCheckProcedureLookupAppServiceListener import \
    DailyCheckProcedureLookupAppServiceListener
from src.port_adapter.api.grpc.listener.lookup.EquipmentLookupAppServiceListener import \
    EquipmentLookupAppServiceListener
from src.port_adapter.api.grpc.listener.lookup.SubcontractorLookupAppServiceListener import \
    SubcontractorLookupAppServiceListener
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.daily_check_procedure_app_service_pb2_grpc import (
    add_DailyCheckProcedureAppServiceServicer_to_server,
)
from src.resource.proto._generated.daily_check_procedure_operation_app_service_pb2_grpc import (
    add_DailyCheckProcedureOperationAppServiceServicer_to_server,
)
from src.resource.proto._generated.daily_check_procedure_operation_parameter_app_service_pb2_grpc import (
    add_DailyCheckProcedureOperationParameterAppServiceServicer_to_server,
)
from src.resource.proto._generated.equipment_app_service_pb2_grpc import (
    add_EquipmentAppServiceServicer_to_server,
)
from src.resource.proto._generated.equipment_category_group_app_service_pb2_grpc import (
    add_EquipmentCategoryGroupAppServiceServicer_to_server,
)
from src.resource.proto._generated.equipment_input_app_service_pb2_grpc import (
    add_EquipmentInputAppServiceServicer_to_server,
)
from src.resource.proto._generated.equipment_model_app_service_pb2_grpc import (
    add_EquipmentModelAppServiceServicer_to_server,
)
from src.resource.proto._generated.equipment_project_category_app_service_pb2_grpc import (
    add_EquipmentProjectCategoryAppServiceServicer_to_server,
)
from src.resource.proto._generated.lookup.daily_check_procedure.daily_check_procedure_lookup_app_service_pb2_grpc import \
    add_DailyCheckProcedureLookupAppServiceServicer_to_server
from src.resource.proto._generated.lookup.equipment.equipment_lookup_app_service_pb2_grpc import \
    add_EquipmentLookupAppServiceServicer_to_server
from src.resource.proto._generated.lookup.organization.organization_lookup_app_service_pb2_grpc import \
    add_OrganizationLookupAppServiceServicer_to_server
from src.resource.proto._generated.lookup.project.project_lookup_app_service_pb2_grpc import \
    add_ProjectLookupAppServiceServicer_to_server
from src.resource.proto._generated.lookup.subcontractor.subcontractor_lookup_app_service_pb2_grpc import \
    add_SubcontractorLookupAppServiceServicer_to_server
from src.resource.proto._generated.lookup.user.user_lookup_app_service_pb2_grpc import \
    add_UserLookupAppServiceServicer_to_server
from src.resource.proto._generated.maintenance_procedure_app_service_pb2_grpc import (
    add_MaintenanceProcedureAppServiceServicer_to_server,
)
from src.resource.proto._generated.maintenance_procedure_operation_app_service_pb2_grpc import (
    add_MaintenanceProcedureOperationAppServiceServicer_to_server,
)
from src.resource.proto._generated.maintenance_procedure_operation_parameter_app_service_pb2_grpc import (
    add_MaintenanceProcedureOperationParameterAppServiceServicer_to_server,
)
from src.resource.proto._generated.manufacturer_app_service_pb2_grpc import (
    add_ManufacturerAppServiceServicer_to_server,
)
from src.resource.proto._generated.organization_app_service_pb2_grpc import (
    add_OrganizationAppServiceServicer_to_server,
)
from src.resource.proto._generated.project_app_service_pb2_grpc import (
    add_ProjectAppServiceServicer_to_server,
)
from src.resource.proto._generated.role_app_service_pb2_grpc import (
    add_RoleAppServiceServicer_to_server,
)
from src.resource.proto._generated.standard_equipment_app_service_pb2_grpc import (
    add_StandardEquipmentAppServiceServicer_to_server,
)
from src.resource.proto._generated.standard_equipment_category_app_service_pb2_grpc import (
    add_StandardEquipmentCategoryAppServiceServicer_to_server,
)
from src.resource.proto._generated.standard_equipment_category_group_app_service_pb2_grpc import (
    add_StandardEquipmentCategoryGroupAppServiceServicer_to_server,
)
from src.resource.proto._generated.standard_maintenance_procedure_app_service_pb2_grpc import (
    add_StandardMaintenanceProcedureAppServiceServicer_to_server,
)
from src.resource.proto._generated.subcontractor_app_service_pb2_grpc import (
    add_SubcontractorAppServiceServicer_to_server,
)
from src.resource.proto._generated.subcontractor_category_app_service_pb2_grpc import (
    add_SubcontractorCategoryAppServiceServicer_to_server,
)
from src.resource.proto._generated.unit_app_service_pb2_grpc import (
    add_UnitAppServiceServicer_to_server,
)
from src.resource.proto._generated.user_app_service_pb2_grpc import (
    add_UserAppServiceServicer_to_server,
)


"""The Python implementation of the GRPC Seans-gRPC server."""
from concurrent import futures

import grpc
from grpc_reflection.v1alpha import reflection


from src.resource.logging.logger import logger


def serve():
    """The main serve function of the server.
    This opens the socket, and listens for incoming grpc conformant packets"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    add_ProjectAppServiceServicer_to_server(ProjectAppServiceListener(), server)
    add_UserAppServiceServicer_to_server(UserAppServiceListener(), server)
    add_OrganizationAppServiceServicer_to_server(
        OrganizationAppServiceListener(), server
    )
    add_UserLookupAppServiceServicer_to_server(UserLookupAppServiceListener(), server)
    add_ProjectLookupAppServiceServicer_to_server(ProjectLookupAppServiceListener(), server)
    add_OrganizationLookupAppServiceServicer_to_server(OrganizationLookupAppServiceListener(), server)
    add_EquipmentModelAppServiceServicer_to_server(
        EquipmentModelAppServiceListener(), server
    )
    add_ManufacturerAppServiceServicer_to_server(
        ManufacturerAppServiceListener(), server
    )
    add_EquipmentProjectCategoryAppServiceServicer_to_server(
        EquipmentProjectCategoryAppServiceListener(), server
    )
    add_EquipmentCategoryGroupAppServiceServicer_to_server(
        EquipmentCategoryGroupAppServiceListener(), server
    )
    add_EquipmentAppServiceServicer_to_server(EquipmentAppServiceListener(), server)
    add_UnitAppServiceServicer_to_server(UnitAppServiceListener(), server)
    add_EquipmentInputAppServiceServicer_to_server(
        EquipmentInputAppServiceListener(), server
    )
    add_SubcontractorAppServiceServicer_to_server(
        SubcontractorAppServiceListener(), server
    )
    add_MaintenanceProcedureAppServiceServicer_to_server(
        MaintenanceProcedureAppServiceListener(), server
    )
    add_MaintenanceProcedureOperationAppServiceServicer_to_server(
        MaintenanceProcedureOperationAppServiceListener(), server
    )
    add_MaintenanceProcedureOperationParameterAppServiceServicer_to_server(
        MaintenanceProcedureOperationParameterAppServiceListener(), server
    )
    add_DailyCheckProcedureAppServiceServicer_to_server(
        DailyCheckProcedureAppServiceListener(), server
    )
    add_DailyCheckProcedureOperationAppServiceServicer_to_server(
        DailyCheckProcedureOperationAppServiceListener(), server
    )
    add_DailyCheckProcedureOperationParameterAppServiceServicer_to_server(
        DailyCheckProcedureOperationParameterAppServiceListener(), server
    )
    add_StandardMaintenanceProcedureAppServiceServicer_to_server(
        StandardMaintenanceProcedureAppServiceListener(), server
    )
    add_SubcontractorCategoryAppServiceServicer_to_server(
        SubcontractorCategoryAppServiceListener(), server
    )
    add_StandardEquipmentAppServiceServicer_to_server(
        StandardEquipmentAppServiceListener(), server
    )
    add_StandardEquipmentCategoryAppServiceServicer_to_server(
        StandardEquipmentCategoryAppServiceListener(), server
    )
    add_StandardEquipmentCategoryGroupAppServiceServicer_to_server(
        StandardEquipmentCategoryGroupAppServiceListener(), server
    )
    add_RoleAppServiceServicer_to_server(RoleAppServiceListener(), server)

    add_SubcontractorLookupAppServiceServicer_to_server(
        SubcontractorLookupAppServiceListener(), server
    )

    add_EquipmentLookupAppServiceServicer_to_server(
        EquipmentLookupAppServiceListener(), server
    )

    add_DailyCheckProcedureLookupAppServiceServicer_to_server(
        DailyCheckProcedureLookupAppServiceListener(), server
    )

    SERVICE_NAMES = (
        src.resource.proto._generated.daily_check_procedure_operation_app_service_pb2.DESCRIPTOR.services_by_name['DailyCheckProcedureOperationAppService'].full_name,
        src.resource.proto._generated.daily_check_procedure_operation_parameter_app_service_pb2.DESCRIPTOR.services_by_name['DailyCheckProcedureOperationParameterAppService'].full_name,
        src.resource.proto._generated.equipment_app_service_pb2.DESCRIPTOR.services_by_name['EquipmentAppService'].full_name,
        src.resource.proto._generated.equipment_category_group_app_service_pb2.DESCRIPTOR.services_by_name['EquipmentCategoryGroupAppService'].full_name,
        src.resource.proto._generated.equipment_input_app_service_pb2.DESCRIPTOR.services_by_name['EquipmentInputAppService'].full_name,
        src.resource.proto._generated.equipment_model_app_service_pb2.DESCRIPTOR.services_by_name['EquipmentModelAppService'].full_name,
        src.resource.proto._generated.equipment_project_category_app_service_pb2.DESCRIPTOR.services_by_name['EquipmentProjectCategoryAppService'].full_name,
        src.resource.proto._generated.maintenance_procedure_app_service_pb2.DESCRIPTOR.services_by_name['MaintenanceProcedureAppService'].full_name,
        src.resource.proto._generated.maintenance_procedure_operation_app_service_pb2.DESCRIPTOR.services_by_name['MaintenanceProcedureOperationAppService'].full_name,
        src.resource.proto._generated.maintenance_procedure_operation_parameter_app_service_pb2.DESCRIPTOR.services_by_name['MaintenanceProcedureOperationParameterAppService'].full_name,
        src.resource.proto._generated.manufacturer_app_service_pb2.DESCRIPTOR.services_by_name['ManufacturerAppService'].full_name,
        src.resource.proto._generated.organization_app_service_pb2.DESCRIPTOR.services_by_name['OrganizationAppService'].full_name,
        src.resource.proto._generated.project_app_service_pb2.DESCRIPTOR.services_by_name['ProjectAppService'].full_name,
        src.resource.proto._generated.subcontractor_app_service_pb2.DESCRIPTOR.services_by_name['SubcontractorAppService'].full_name,
        src.resource.proto._generated.unit_app_service_pb2.DESCRIPTOR.services_by_name['UnitAppService'].full_name,
        src.resource.proto._generated.user_app_service_pb2.DESCRIPTOR.services_by_name['UserAppService'].full_name,
        src.resource.proto._generated.standard_maintenance_procedure_app_service_pb2.DESCRIPTOR.services_by_name['StandardMaintenanceProcedureAppService'].full_name,
        src.resource.proto._generated.subcontractor_category_app_service_pb2.DESCRIPTOR.services_by_name['SubcontractorCategoryAppService'].full_name,
        src.resource.proto._generated.standard_equipment_app_service_pb2.DESCRIPTOR.services_by_name['StandardEquipmentAppService'].full_name,
        src.resource.proto._generated.standard_equipment_category_app_service_pb2.DESCRIPTOR.services_by_name['StandardEquipmentCategoryAppService'].full_name,
        src.resource.proto._generated.standard_equipment_category_group_app_service_pb2.DESCRIPTOR.services_by_name['StandardEquipmentCategoryGroupAppService'].full_name,
        src.resource.proto._generated.role_app_service_pb2.DESCRIPTOR.services_by_name['RoleAppService'].full_name,
        src.resource.proto._generated.daily_check_procedure_app_service_pb2.DESCRIPTOR.services_by_name['DailyCheckProcedureAppService'].full_name,
        src.resource.proto._generated.lookup.user.user_lookup_app_service_pb2.DESCRIPTOR.services_by_name['UserLookupAppService'].full_name,
        src.resource.proto._generated.lookup.project.project_lookup_app_service_pb2.DESCRIPTOR.services_by_name['ProjectLookupAppService'].full_name,
        src.resource.proto._generated.lookup.organization.organization_lookup_app_service_pb2.DESCRIPTOR.services_by_name['OrganizationLookupAppService'].full_name,
        src.resource.proto._generated.lookup.equipment.equipment_lookup_app_service_pb2.DESCRIPTOR.services_by_name['EquipmentLookupAppService'].full_name,
        src.resource.proto._generated.lookup.subcontractor.subcontractor_lookup_app_service_pb2.DESCRIPTOR.services_by_name['SubcontractorLookupAppService'].full_name,
        src.resource.proto._generated.lookup.daily_check_procedure.daily_check_procedure_lookup_app_service_pb2.DESCRIPTOR.services_by_name['DailyCheckProcedureLookupAppService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    port = "[::]:9999"
    server.add_insecure_port(port)
    logger.info(f"Project microservice grpc server started/restarted on port {port}")
    server.start()

    # try:
    #     while True:
    #         print("Server Running : threadcount %i" % (threading.active_count()))
    #         time.sleep(10)
    # except KeyboardInterrupt:
    #     print("KeyboardInterrupt")
    #     server.stop(0)
    server.wait_for_termination()


if __name__ == "__main__":
    random.seed(datetime.utcnow().timestamp())
    openTelemetry = AppDi.instance.get(OpenTelemetry)
    serve()
