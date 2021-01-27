"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.organization.Organization import Organization

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__OrganizationUpdated, "Organization Updated", "event", "message")
"""
class OrganizationUpdated(DomainEvent):
    def __init__(self, oldObject: Organization, newObject: Organization):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.ORGANIZATION_UPDATED.value)
        self._data = {'old': oldObject.toMap(), 'new': newObject.toMap()}
