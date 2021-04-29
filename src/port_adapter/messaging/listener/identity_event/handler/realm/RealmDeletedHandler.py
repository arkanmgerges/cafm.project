"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from src.port_adapter.messaging.listener.common.handler.realm.RealmDeletedHandler import (
    RealmDeletedHandler as Handler,
)

"""
c4model|cb|project:ComponentQueue(project__messaging_identity_event_handler__RealmDeletedHandler, "CommonEventConstant.REALM_DELETED.value", "identity event consumer", "")
c4model:Rel(project__messaging_identity_event_handler__RealmDeletedHandler, identity__domainmodel_event__RealmDeleted, "consume")
c4model:Rel(project__messaging_identity_event_handler__RealmDeletedHandler, project__messaging_project_command_handler__DeleteOrganizationHandler, "CommonCommandConstant.DELETE_ORGANIZATION.value", "message")
"""


class RealmDeletedHandler(Handler):
    pass
