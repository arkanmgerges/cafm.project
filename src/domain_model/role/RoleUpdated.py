"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.role.Role import Role

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__RoleUpdated, "Role Updated", "event", "message")
"""
class RoleUpdated(DomainEvent):
    def __init__(self, oldObj: Role, newObj: Role):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.ROLE_UPDATED.value)
        self._data = {'old': oldObj.toMap(), 'new': newObj.toMap()}

