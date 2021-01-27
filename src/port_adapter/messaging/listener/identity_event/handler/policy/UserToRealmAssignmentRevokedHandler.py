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
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__UserToRealmAssignmentRevokedHandler, "User to Realm Assignement Revoked", "identity event consumer", "User to Realm Assignment Revoked")
c4model:Rel(identity__domainmodel_event__UserToRealmAssignmentRevoked, project__messaging_identity_event_handler__UserToRealmAssignmentRevokedHandler, "User to Realm Assignment Revoked", "message")
c4model:Rel(project__messaging_identity_event_handler__UserToRealmAssignmentRevokedHandler, project__messaging_project_command_handler__RevokeUserToOrganizationAssignmentHandler, "Revoke User to Organization Assignment", "message")
"""
class UserToRealmAssignmentRevokedHandler(Handler):

    def __init__(self):
        self._eventConstant = CommonEventConstant.USER_TO_REALM_ASSIGNMENT_REVOKED
        self._commandConstant = CommonCommandConstant.REVOKE_USER_TO_ORGANIZATION_ASSIGNMENT

    def canHandle(self, name: str) -> bool:
        return name == self._eventConstant.value

    def handleCommand(self, messageData: dict) -> dict:
        name = messageData['name']
        data = messageData['data']
        metadata = messageData['metadata']

        logger.debug(
            f'[{UserToRealmAssignmentRevokedHandler.handleCommand.__qualname__}] - received args:\ntype(name): {type(name)}, name: {name}\ntype(data): {type(data)}, data: {data}\ntype(metadata): {type(metadata)}, metadata: {metadata}')
        dataDict = json.loads(data)
        metadataDict = json.loads(metadata)

        if 'token' not in metadataDict:
            raise UnAuthorizedException()

        return {'name': self._commandConstant.value, 'created_on': DateTimeHelper.utcNow(),
                'data': {'organization_id': dataDict['realm_id'], 'user_id': dataDict['user_id']},
                'metadata': metadataDict}
