"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.BuildingApplicationService import BuildingApplicationService
from src.application.BuildingLevelApplicationService import (
    BuildingLevelApplicationService,
)
from src.application.BuildingLevelRoomApplicationService import (
    BuildingLevelRoomApplicationService,
)
from src.application.DailyCheckProcedureApplicationService import (
    DailyCheckProcedureApplicationService,
)
from src.application.DailyCheckProcedureOperationApplicationService import (
    DailyCheckProcedureOperationApplicationService,
)
from src.application.DailyCheckProcedureOperationParameterApplicationService import (
    DailyCheckProcedureOperationParameterApplicationService,
)
from src.application.DailyCheckProcedureOperationLabelApplicationService import (
    DailyCheckProcedureOperationLabelApplicationService,
)
from src.application.EquipmentApplicationService import EquipmentApplicationService
from src.application.EquipmentCategoryGroupApplicationService import (
    EquipmentCategoryGroupApplicationService,
)
from src.application.EquipmentInputApplicationService import (
    EquipmentInputApplicationService,
)
from src.application.EquipmentModelApplicationService import (
    EquipmentModelApplicationService,
)
from src.application.EquipmentProjectCategoryApplicationService import (
    EquipmentProjectCategoryApplicationService,
)
from src.application.MaintenanceProcedureApplicationService import (
    MaintenanceProcedureApplicationService,
)
from src.application.MaintenanceProcedureOperationApplicationService import (
    MaintenanceProcedureOperationApplicationService,
)
from src.application.MaintenanceProcedureOperationParameterApplicationService import (
    MaintenanceProcedureOperationParameterApplicationService,
)
from src.application.MaintenanceProcedureOperationLabelApplicationService import (
    MaintenanceProcedureOperationLabelApplicationService,
)
from src.application.ManufacturerApplicationService import (
    ManufacturerApplicationService,
)
from src.application.OrganizationApplicationService import (
    OrganizationApplicationService,
)
from src.application.StandardEquipmentApplicationService import (
    StandardEquipmentApplicationService,
)
from src.application.StandardEquipmentCategoryApplicationService import (
    StandardEquipmentCategoryApplicationService,
)
from src.application.StandardEquipmentCategoryGroupApplicationService import (
    StandardEquipmentCategoryGroupApplicationService,
)
from src.application.StandardMaintenanceProcedureApplicationService import (
    StandardMaintenanceProcedureApplicationService,
)
from src.application.SubcontractorApplicationService import (
    SubcontractorApplicationService,
)
from src.application.SubcontractorCategoryApplicationService import (
    SubcontractorCategoryApplicationService,
)
from src.application.UnitApplicationService import UnitApplicationService
from src.domain_model.resource.exception.DomainModelException import (
    DomainModelException,
)
from src.domain_model.resource.exception.ProcessBulkDomainException import (
    ProcessBulkDomainException,
)
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.port_adapter.repository.resource.exception.IntegrityErrorRepositoryException import \
    IntegrityErrorRepositoryException
from src.resource.common.DateTimeHelper import DateTimeHelper


class ProcessBulkHandler(Handler):
    def __init__(self):
        self._commandConstant = CommonCommandConstant.PROCESS_BULK
        self._handlers = []

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleMessage(self, messageData: dict, extraData: dict = None) -> dict:
        data = messageData["data"]
        metadata = messageData["metadata"]

        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        totalItemCount = dataDict["total_item_count"]
        try:
            # The is the final result of all the data items in the dataDict["data"]
            dataDict["data"].sort(key=self._sortKeyByCommand)
            batchedDataItems = self._batchSimilar(dataDict["data"])
            for batchedDataCommand, batchedDataValue in batchedDataItems.items():
                entityName = batchedDataCommand[batchedDataCommand.index("_") + 1 :]
                appService = self._appServiceByEntityName(entityName)
                commandMethod = batchedDataCommand[: batchedDataCommand.index("_") :]
                if appService is not None:
                    requestParamsList = []
                    for dataItem in batchedDataValue:
                        requestData = dataItem["_request_data"]
                        requestParamsList.append(requestData["command_data"])
                    if commandMethod == "create":
                        appService.bulkCreate(
                            objListParams=requestParamsList, token=metadataDict["token"]
                        )
                    elif commandMethod == "update":
                        appService.bulkUpdate(
                            objListParams=requestParamsList, token=metadataDict["token"]
                        )
                    elif commandMethod == "delete":
                        appService.bulkDelete(
                            objListParams=requestParamsList, token=metadataDict["token"]
                        )
            return {
                "name": self._commandConstant.value,
                "created_on": DateTimeHelper.utcNow(),
                "data": {"data": dataDict["data"], "total_item_count": totalItemCount},
                "metadata": metadataDict,
            }
        except ProcessBulkDomainException as e:
            return {
                "name": self._commandConstant.value,
                "created_on": DateTimeHelper.utcNow(),
                "data": {
                    "data": dataDict["data"],
                    "total_item_count": totalItemCount,
                    "exceptions": e.extra,
                },
                "metadata": metadataDict,
            }
        except DomainModelException as e:
            return {
                "name": self._commandConstant.value,
                "created_on": DateTimeHelper.utcNow(),
                "data": {
                    "data": dataDict["data"],
                    "total_item_count": totalItemCount,
                    "exceptions": [{"reason": {"message": e.message, "code": e.code}}],
                },
                "metadata": metadataDict,
            }
        except IntegrityErrorRepositoryException as e:
            return {
                "name": self._commandConstant.value,
                "created_on": DateTimeHelper.utcNow(),
                "data": {
                    "data": dataDict["data"],
                    "total_item_count": totalItemCount,
                    "exceptions": [{"reason": {"message": e.message, "code": e.code}}],
                },
                "metadata": metadataDict,
            }

    def _sortKeyByCommand(self, item: dict):
        command = item["_request_data"]["command"]
        commandMethod = command[: command.index("_") :]
        switcher = {"create": 0, "update": 1, "assign": 2, "delete": 3}
        return switcher.get(commandMethod, 4)

    def _batchSimilar(self, data):
        # The key will be the command like 'create_unit' and the value is the details of the command
        result = {}
        for item in data:
            command = item["_request_data"]["command"]
            if command not in result:
                result[command] = []
            result[command].append(item)
        return result

    def _appServiceByEntityName(self, entityName):
        entityToAppService = {
            # 'project': ProjectApplicationService,
            # 'role': RoleApplicationService,
            # 'user': UserApplicationService,
            "organization": OrganizationApplicationService,
            "unit": UnitApplicationService,
            "building": BuildingApplicationService,
            "building_level": BuildingLevelApplicationService,
            "building_level_room": BuildingLevelRoomApplicationService,
            "subcontractor": SubcontractorApplicationService,
            "subcontractor_category": SubcontractorCategoryApplicationService,
            "equipment": EquipmentApplicationService,
            "equipment_category_group": EquipmentCategoryGroupApplicationService,
            "equipment_input": EquipmentInputApplicationService,
            "equipment_model": EquipmentModelApplicationService,
            "equipment_project_category": EquipmentProjectCategoryApplicationService,
            "daily_check_procedure": DailyCheckProcedureApplicationService,
            "daily_check_procedure_operation": DailyCheckProcedureOperationApplicationService,
            "daily_check_procedure_operation_parameter": DailyCheckProcedureOperationParameterApplicationService,
            "daily_check_procedure_operation_label": DailyCheckProcedureOperationLabelApplicationService,
            "maintenance_procedure": MaintenanceProcedureApplicationService,
            "maintenance_procedure_operation": MaintenanceProcedureOperationApplicationService,
            "maintenance_procedure_operation_parameter": MaintenanceProcedureOperationParameterApplicationService,
            "maintenance_procedure_operation_label": MaintenanceProcedureOperationLabelApplicationService,
            "standard_maintenance": StandardMaintenanceProcedureApplicationService,
            "manufacturer": ManufacturerApplicationService,
            "standard_equipment": StandardEquipmentApplicationService,
            "standard_equipment_category": StandardEquipmentCategoryApplicationService,
            "standard_equipment_category_group": StandardEquipmentCategoryGroupApplicationService,
        }
        if entityName in entityToAppService:
            return AppDi.instance.get(entityToAppService[entityName])
        return None

    # def handleData(self, dataItem, handler, metadata):
    #     requestData = dataItem["_request_data"]
    #     command = requestData["command"]
    #     commandData = requestData["command_data"]
    #     loop = True
    #     while loop:
    #         try:
    #             # Handle the command
    #             result = handler.handleMessage(
    #                 messageData={
    #                     "name": command,
    #                     "data": json.dumps(commandData),
    #                     "metadata": metadata,
    #                 }
    #             )
    #             dataItem["result"] = result
    #             return dataItem
    #         except DomainModelException as e:
    #             # Add the reason for the failure
    #             result = {"reason": {"message": e.message, "code": e.code}}
    #             dataItem["result"] = result
    #             return dataItem
    #         except Exception as e:
    #             # Loop continuously and print the error
    #             logger.error(e)
    #             sleep(2)
