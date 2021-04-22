"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

import json
import src.port_adapter.AppDi as AppDi
from src.application.MaintenanceProcedureApplicationService import (
    MaintenanceProcedureApplicationService,
)
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class CreateMaintenanceProcedureHandler(Handler):
    def __init__(self):
        self._commandConstant = CommonCommandConstant.CREATE_MAINTENANCE_PROCEDURE

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData["name"]
        data = messageData["data"]
        metadata = messageData["metadata"]

        logger.debug(
            f"[{CreateMaintenanceProcedureHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}"
        )
        appService: MaintenanceProcedureApplicationService = AppDi.instance.get(
            MaintenanceProcedureApplicationService
        )
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        id = (
            dataDict["maintenance_procedure_id"]
            if "maintenance_procedure_id" in dataDict
            else None
        )

        obj = appService.createMaintenanceProcedure(
            id=id,
            name=dataDict["name"],
            type=dataDict["type"],
            subType=dataDict["sub_type"],
            frequency=dataDict["frequency"],
            startDate=dataDict["start_date"],
            subcontractorId=dataDict["subcontractor_id"],
            equipmentId=dataDict["equipment_id"],
            token=metadataDict["token"],
        )
        data = dataDict
        data["maintenance_procedure_id"] = obj.id()
        return {
            "name": self._commandConstant.value,
            "created_on": DateTimeHelper.utcNow(),
            "data": data,
            "metadata": metadataDict,
        }
