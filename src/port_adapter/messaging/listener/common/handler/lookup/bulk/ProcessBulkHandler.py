"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.SubcontractorLookupApplicationService import SubcontractorLookupApplicationService
from src.domain_model.resource.exception.DomainModelException import DomainModelException
from src.domain_model.resource.exception.ProcessBulkDomainException import ProcessBulkDomainException
from src.domain_model.resource.exception.UnAuthorizedException import (
    UnAuthorizedException,
)
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper


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

        totalItemCount = dataDict["total_item_count"]
        try:
            # The is the final result of all the data items in the dataDict["data"]
            dataDict["data"].sort(key=self._sortKeyByCommand)
            batchedDataItems = self._batchSimilar(dataDict["data"])
            for batchedDataCommand, batchedDataValue in batchedDataItems.items():
                entityName = batchedDataCommand[batchedDataCommand.index("_") + 1 :]
                commandMethod = batchedDataCommand[: batchedDataCommand.index("_") :]
                appService = self._appServiceByEntityNameAndCommandMethod(entityName, commandMethod)
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
                "data": {"data": dataDict["data"], "total_item_count": totalItemCount},
                "metadata": metadataDict,
            }
        except ProcessBulkDomainException as e:
            return {
                "name": self._commandConstant.value,
                "created_on": DateTimeHelper.utcNow(),
                "data": {"data": dataDict["data"], "total_item_count": totalItemCount, "exceptions": e.extra},
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

    def _sortKeyByCommand(self, item: dict):
        command = item['_request_data']['command']
        commandMethod = command[: command.index("_"):]
        switcher = {
            'create': 0,
            'update': 1,
            'assign': 2,
            'delete': 3
        }
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

    def _appServiceByEntityNameAndCommandMethod(self, entityName, commandMethod):
        dataItems = [
            {"entityName": "subcontractor", "commandMethods": ["create", "update", "delete"], "appService": SubcontractorLookupApplicationService},
            {"entityName": "subcontractor_category", "commandMethods": ["update"], "appService": SubcontractorLookupApplicationService},
        ]
        for item in dataItems:
            if entityName == item["entityName"] and commandMethod in item["commandMethods"]:
                return AppDi.instance.get(item["appService"])
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
