"""
@author: Mohammad S. moso<moso@develoop.run>
"""
import json

import src.port_adapter.AppDi as AppDi
from src.application.SubcontractorApplicationService import SubcontractorApplicationService
from src.domain_model.subcontractor.Subcontractor import Subcontractor
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.common.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger


class CreateSubcontractorHandler(Handler):

    def __init__(self):
        self._commandConstant = CommonCommandConstant.CREATE_SUBCONTRACTOR

    def canHandle(self, name: str) -> bool:
        return name == self._commandConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{CreateSubcontractorHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        appService: SubcontractorApplicationService = AppDi.instance.get(SubcontractorApplicationService)
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        id = dataDict['id'] if 'id' in dataDict else None
        obj: Subcontractor = appService.createSubcontractor(id=id,
                                                            companyName=dataDict['company_name'],
                                                            websiteUrl=dataDict['website_url'],
                                                            contactPerson=dataDict['contact_person'],
                                                            email=dataDict['email'],
                                                            phoneNumber=dataDict['phone_number'],
                                                            addressOne=dataDict['address_one'],
                                                            addressTwo=dataDict['address_two'],
                                                            token=metadataDict['token'])
        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': {'id': obj.id()},
                'metadata': metadataDict}