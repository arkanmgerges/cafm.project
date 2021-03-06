"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4
from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.state.State import State


class StateCreated(DomainEvent):
    def __init__(self, obj: State):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.STATE_CREATED.value)
        self._data = obj.toMap()
