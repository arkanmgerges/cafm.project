"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


import json

import src.port_adapter.AppDi as AppDi
from src.application.ProjectApplicationService import ProjectApplicationService
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class UpdateProjectHandler(Handler):

    def __init__(self):
        self._commandConstant = CommonCommandConstant.UPDATE_PROJECT

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{UpdateProjectHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')

        appService: ProjectApplicationService = AppDi.instance.get(ProjectApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        id = dataDict['id'] if 'id' in dataDict else None
        appService.updateProject(
            id=id,
            name=dataDict["name"],
            cityId=dataDict["city_id"],
            countryId=dataDict["country_id"],
            startDate=dataDict["start_date"] if 'start_date' in dataDict else 0,
            beneficiaryId=dataDict["beneficiary_id"],
            addressLine=dataDict["address_line"],
            token=metadataDict['token'])
        data = {'id': id, "name":dataDict["name"], "city_id":dataDict["city_id"], "country_id":dataDict["country_id"],
                "beneficiary_id":dataDict["beneficiary_id"], "address_line":dataDict["address_line"], "state":dataDict["state"]}
        if 'start_date' in dataDict:
            data['start_date'] = dataDict["start_date"]
        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': data,'metadata': metadataDict}
