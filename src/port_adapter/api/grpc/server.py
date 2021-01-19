"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import random
# https://www.youtube.com/watch?v=dQK0VLahrDk&list=PLXs6ze70rLY9u0X6qz_91bCvsjq3Kqn_O&index=5
from datetime import datetime

import src.port_adapter.AppDi as AppDi
from src.port_adapter.api.grpc.listener.ProjectAppServiceListener import ProjectAppServiceListener
from src.port_adapter.api.grpc.listener.UserAppServiceListener import UserAppServiceListener
from src.resource.logging.opentelemetry.OpenTelemetry import OpenTelemetry
from src.resource.proto._generated.project_app_service_pb2_grpc import add_ProjectAppServiceServicer_to_server
from src.resource.proto._generated.user_app_service_pb2_grpc import add_UserAppServiceServicer_to_server

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
