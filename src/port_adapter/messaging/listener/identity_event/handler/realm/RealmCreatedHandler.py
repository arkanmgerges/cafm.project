"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from src.port_adapter.messaging.listener.common.handler.realm.RealmCreatedHandler import RealmCreatedHandler as Handler

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__RealmCreatedHandler, "CommonEventConstant.REALM_CREATED.value", "identity event consumer", "")
c4model:Rel(project__messaging_identity_event_handler__RealmCreatedHandler, identity__domainmodel_event__RealmCreated, "consume")
c4model:Rel(project__messaging_identity_event_handler__RealmCreatedHandler, project__messaging_project_command_handler__CreateOrganizationHandler, "CommonCommandConstant.CREATE_ORGANIZATION.value", "message")
"""


class RealmCreatedHandler(Handler):
    pass
