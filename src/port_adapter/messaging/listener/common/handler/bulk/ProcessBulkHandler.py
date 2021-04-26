"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
from time import sleep

import src.port_adapter.AppDi as AppDi
from src.application.DailyCheckProcedureApplicationService import DailyCheckProcedureApplicationService
from src.application.EquipmentApplicationService import EquipmentApplicationService
from src.application.EquipmentCategoryApplicationService import EquipmentCategoryApplicationService
from src.application.EquipmentCategoryGroupApplicationService import EquipmentCategoryGroupApplicationService
from src.application.EquipmentInputApplicationService import EquipmentInputApplicationService
from src.application.EquipmentModelApplicationService import EquipmentModelApplicationService
from src.application.EquipmentProjectCategoryApplicationService import EquipmentProjectCategoryApplicationService
from src.application.MaintenanceProcedureApplicationService import MaintenanceProcedureApplicationService
from src.application.ManufacturerApplicationService import ManufacturerApplicationService
from src.application.OrganizationApplicationService import OrganizationApplicationService
from src.application.ProjectApplicationService import ProjectApplicationService
from src.application.RoleApplicationService import RoleApplicationService
from src.application.StandardEquipmentApplicationService import StandardEquipmentApplicationService
from src.application.StandardEquipmentCategoryApplicationService import StandardEquipmentCategoryApplicationService
from src.application.StandardEquipmentCategoryGroupApplicationService import \
    StandardEquipmentCategoryGroupApplicationService
from src.application.StandardMaintenanceProcedureApplicationService import \
    StandardMaintenanceProcedureApplicationService
from src.application.SubcontractorApplicationService import SubcontractorApplicationService
from src.application.SubcontractorCategoryApplicationService import SubcontractorCategoryApplicationService
from src.application.UnitApplicationService import UnitApplicationService
from src.application.UserApplicationService import UserApplicationService
from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class ProcessBulkHandler(Handler):
    def __init__(self):
        self._commandConstant = CommonCommandConstant.PROCESS_BULK
        self._handlers = []

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict, extraData: dict = None) -> dict:
        data = messageData["data"]
        metadata = messageData["metadata"]

        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if "token" not in metadataDict:
            raise UnAuthorizedException()

        itemCount = dataDict["item_count"]
        try:
            # The is the final result of all the data items in the dataDict["data"]
            requestParamsList = []
            batchedDataItems = self._batchSimilar(dataDict["data"])
            for batchedDataCommand, batchedDataValue in batchedDataItems.items():
                entityName = batchedDataCommand[batchedDataCommand.index('_') + 1:]
                appService = self._appServiceByEntityName(entityName)
                commandMethod = batchedDataCommand[:batchedDataCommand.index('_'):]
                if appService is not None:
                    requestParamsList = []
                    for dataItem in batchedDataValue:
                        requestData = dataItem["_request_data"]
                        requestParamsList.append(requestData["command_data"])
                if commandMethod == "create":
                    appService.bulkCreate(objListParams=requestParamsList, token=metadataDict["token"])
                elif commandMethod == "update":
                    appService.bulkUpdate(objListParams=requestParamsList, token=metadataDict["token"])
                elif commandMethod == "delete":
                    appService.bulkDelete(objListParams=requestParamsList, token=metadataDict["token"])
            return {
                "name": self._commandConstant.value,
                "created_on": DateTimeHelper.utcNow(),
                "data": {"data": dataDict["data"], "item_count": itemCount},
                "metadata": metadataDict,
            }
        except ProcessBulkDomainException as e:
            return {
                "name": self._commandConstant.value,
                "created_on": DateTimeHelper.utcNow(),
                "data": {"data": dataDict["data"], "item_count": itemCount,
                         "exceptions": e.extra},
                "metadata": metadataDict,
            }
        except DomainModelException as e:
            return {
                "name": self._commandConstant.value,
                "created_on": DateTimeHelper.utcNow(),
                "data": {"data": dataDict["data"], "item_count": itemCount,
                         "exceptions": [{"reason": {"message": e.message, "code": e.code}}]},
                "metadata": metadataDict,
            }
        except Exception as e:
            # Loop continuously and print the error
            logger.error(e)
            sleep(2)

    def _batchSimilar(self, data):
        result = {}
        for item in data:
            command = item['_request_data']['command']
            if command not in result:
                result[command] = []
            result[command].append(item)
        return result
    
    def _appServiceByEntityName(self, entityName):
        entityToAppService = {
            'project': ProjectApplicationService,
            'role': RoleApplicationService,
            'user': UserApplicationService,
            'organization': OrganizationApplicationService,
            'unit': UnitApplicationService,
            'subcontractor': SubcontractorApplicationService,
            'subcontractor_category': SubcontractorCategoryApplicationService,
            'equipment': EquipmentApplicationService,
            'equipment_category': EquipmentCategoryApplicationService,
            'equipment_category_group': EquipmentCategoryGroupApplicationService,
            'equipment_input': EquipmentInputApplicationService,
            'equipment_model': EquipmentModelApplicationService,
            'equipment_project_category': EquipmentProjectCategoryApplicationService,
            'daily_check_procedure': DailyCheckProcedureApplicationService,
            'maintenance_procedure': MaintenanceProcedureApplicationService,
            'standard_maintenance_procedure': StandardMaintenanceProcedureApplicationService,
            'manufacturer': ManufacturerApplicationService,
            'standard_equipment': StandardEquipmentApplicationService,
            'standard_equipment_category': StandardEquipmentCategoryApplicationService,
            'standard_equipment_category_group': StandardEquipmentCategoryGroupApplicationService,
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
    #             result = handler.handleCommand(
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
