"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

import src.domain_model.user.User as User
from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__UserDeleted, "User Deleted", "event", "message")
"""


class UserDeleted(DomainEvent):
    def __init__(self, user: User):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.USER_DELETED.value)
        self._data = user.toMap()
