"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import random
# https://www.youtube.com/watch?v=dQK0VLahrDk&list=PLXs6ze70rLY9u0X6qz_91bCvsjq3Kqn_O&index=5
from datetime import datetime

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.grpc.listener.EquipmentAppServiceListener import EquipmentAppServiceListener
from src.port_adapter.api.grpc.listener.EquipmentCategoryAppServiceListener import EquipmentCategoryAppServiceListener
from src.port_adapter.api.grpc.listener.EquipmentCategoryGroupAppServiceListener import \
    EquipmentCategoryGroupAppServiceListener
from src.port_adapter.api.grpc.listener.EquipmentInputAppServiceListener import EquipmentInputAppServiceListener
from src.port_adapter.api.grpc.listener.EquipmentModelAppServiceListener import EquipmentModelAppServiceListener
from src.port_adapter.api.grpc.listener.EquipmentProjectCategoryAppServiceListener import \
    EquipmentProjectCategoryAppServiceListener
from src.port_adapter.api.grpc.listener.ManufacturerAppServiceListener import ManufacturerAppServiceListener
from src.port_adapter.api.grpc.listener.OrganizationAppServiceListener import OrganizationAppServiceListener
from src.port_adapter.api.grpc.listener.ProjectAppServiceListener import ProjectAppServiceListener
from src.port_adapter.api.grpc.listener.UnitAppServiceListener import UnitAppServiceListener
from src.port_adapter.api.grpc.listener.UserAppServiceListener import UserAppServiceListener
from src.port_adapter.api.grpc.listener.UserLookupAppServiceListener import UserLookupAppServiceListener
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.equipment_app_service_pb2_grpc import add_EquipmentAppServiceServicer_to_server
from src.resource.proto._generated.equipment_category_app_service_pb2_grpc import \
    add_EquipmentCategoryAppServiceServicer_to_server
from src.resource.proto._generated.equipment_category_group_app_service_pb2_grpc import \
    add_EquipmentCategoryGroupAppServiceServicer_to_server
from src.resource.proto._generated.equipment_input_app_service_pb2_grpc import \
    add_EquipmentInputAppServiceServicer_to_server
from src.resource.proto._generated.equipment_model_app_service_pb2_grpc import \
    add_EquipmentModelAppServiceServicer_to_server
from src.resource.proto._generated.equipment_project_category_app_service_pb2_grpc import \
    add_EquipmentProjectCategoryAppServiceServicer_to_server
from src.resource.proto._generated.manufacturer_app_service_pb2_grpc import add_ManufacturerAppServiceServicer_to_server
from src.resource.proto._generated.organization_app_service_pb2_grpc import add_OrganizationAppServiceServicer_to_server
from src.resource.proto._generated.project_app_service_pb2_grpc import add_ProjectAppServiceServicer_to_server
from src.resource.proto._generated.unit_app_service_pb2_grpc import add_UnitAppServiceServicer_to_server
from src.resource.proto._generated.user_app_service_pb2_grpc import add_UserAppServiceServicer_to_server
from src.resource.proto._generated.user_lookup_app_service_pb2_grpc import add_UserLookupAppServiceServicer_to_server

"""The Python implementation of the GRPC Seans-gRPC server."""
from concurrent import futures

import grpc


from src.resource.logging.logger import logger


def serve():
    """The main serve function of the server.
    This opens the socket, and listens for incoming grpc conformant packets"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    add_ProjectAppServiceServicer_to_server(ProjectAppServiceListener(), server)
    add_UserAppServiceServicer_to_server(UserAppServiceListener(), server)
    add_OrganizationAppServiceServicer_to_server(OrganizationAppServiceListener(), server)
    add_UserLookupAppServiceServicer_to_server(UserLookupAppServiceListener(), server)
    add_EquipmentModelAppServiceServicer_to_server(EquipmentModelAppServiceListener(), server)
    add_ManufacturerAppServiceServicer_to_server(ManufacturerAppServiceListener(), server)
    add_EquipmentProjectCategoryAppServiceServicer_to_server(EquipmentProjectCategoryAppServiceListener(), server)
    add_EquipmentCategoryAppServiceServicer_to_server(EquipmentCategoryAppServiceListener(), server)
    add_EquipmentCategoryGroupAppServiceServicer_to_server(EquipmentCategoryGroupAppServiceListener(), server)
    add_EquipmentAppServiceServicer_to_server(EquipmentAppServiceListener(), server)
    add_UnitAppServiceServicer_to_server(UnitAppServiceListener(), server)
    add_EquipmentInputAppServiceServicer_to_server(EquipmentInputAppServiceListener(), server)

    port = "[::]:9999"
    server.add_insecure_port(port)
    logger.info(f'Identity server started/restarted on port {port}')
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
