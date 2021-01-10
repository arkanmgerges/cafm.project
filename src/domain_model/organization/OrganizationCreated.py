"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.organization.Organization import Organization


class OrganizationCreated(DomainEvent):
    def __init__(self, object: Organization):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.Organization_CREATED.value)
        self._data = object.toMap()
