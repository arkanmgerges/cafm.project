"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
# https://www.youtube.com/watch?v=dQK0VLahrDk&list=PLXs6ze70rLY9u0X6qz_91bCvsjq3Kqn_O&index=5
from src.port_adapter.api.grpc.listener.ProjectAppServiceListener import ProjectAppServiceListener
from src.resource.proto._generated.project_app_service_pb2_grpc import add_ProjectAppServiceServicer_to_server

"""The Python implementation of the GRPC Seans-gRPC server."""
from concurrent import futures

import grpc


from src.resource.logging.logger import logger


def serve():
    """The main serve function of the server.
    This opens the socket, and listens for incoming grpc conformant packets"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    add_ProjectAppServiceServicer_to_server(ProjectAppServiceListener(), server)

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
    serve()
