"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.messaging.listener.common.handler.project.building.CreateBuildingHandler import \
    CreateBuildingHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_project_command_handler__CreateBuildingHandler, "CommonCommandConstant.CREATE_PROJECT.value", "project command consumer", "")
c4model:Rel(project__messaging_project_command_handler__CreateBuildingHandler, project__domainmodel_event__BuildingCreated, "create", "message")
"""


class CreateBuildingHandler(Handler):
    pass
