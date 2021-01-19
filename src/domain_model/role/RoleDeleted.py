"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.role.Role import Role


class RoleDeleted(DomainEvent):
    def __init__(self, obj: Role):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.ROLE_DELETED.value)
        self._data = obj.toMap()
