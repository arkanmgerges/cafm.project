"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json

from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.resource.exception.UnAuthorizedException import UnAuthorizedException
from src.port_adapter.messaging.listener.CommandConstant import CommonCommandConstant
from src.port_adapter.messaging.listener.project_command.handler.Handler import Handler
from src.resource.common.DateTimeHelper import DateTimeHelper
from src.resource.logging.logger import logger

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__UserToRealmAssignedHandler, "User to Realm Assigned", "identity event consumer", "User to Realm Assigned")
c4model:Rel(identity__domainmodel_event__UserToRealmAssigned, project__messaging_identity_event_handler__UserToRealmAssignedHandler, "User to Realm Assigned", "message")
c4model:Rel(project__messaging_identity_event_handler__UserToRealmAssignedHandler, project__messaging_project_command_handler__AssignUserToOrganizationHandler, "Assign User to Organization", "message")
"""
class UserToRealmAssignedHandler(Handler):

    def __init__(self):
        self._eventConstant = CommonEventConstant.USER_TO_REALM_ASSIGNED
        self._commandConstant = CommonCommandConstant.ASSIGN_USER_TO_ORGANIZATION

    def canHandle(self, name: str) -> bool:
        return name == self._eventConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{UserToRealmAssignedHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': {'organization_id': dataDict['realm_id'], 'user_id': dataDict['user_id']},
                'metadata': metadataDict}
