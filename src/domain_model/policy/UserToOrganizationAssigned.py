"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.organization.Organization import Organization
from src.domain_model.user.User import User

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__UserToOrganizationAssigned, "CommonEventConstant.USER_TO_ORGANIZATION_ASSIGNED.value", "message", "event")
"""


class UserToOrganizationAssigned(DomainEvent):
    def __init__(self, organization: Organization, user: User):
        super().__init__(
            id=str(uuid4()),
            name=CommonEventConstant.USER_TO_ORGANIZATION_ASSIGNED.value,
        )
        self._data = {"user_id": user.id(), "organization_id": organization.id()}
