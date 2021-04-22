"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.port_adapter.repository.db_model.BuildingLevel import BuildingLevel

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__BuildingLevelUpdated, "CommonEventConstant.BUILDING_LEVEL_UPDATED.value", "message", "event")
"""


class BuildingLevelUpdated(DomainEvent):
    def __init__(self, oldObj: BuildingLevel, newObj: BuildingLevel):
        super().__init__(
            id=str(uuid4()), name=CommonEventConstant.BUILDING_LEVEL_UPDATED.value
        )
        self._data = {"old": oldObj.toMap(), "new": newObj.toMap()}
