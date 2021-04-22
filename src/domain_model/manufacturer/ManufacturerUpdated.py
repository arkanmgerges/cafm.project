"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.manufacturer.Manufacturer import Manufacturer

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__ManufacturerUpdated, "CommonEventConstant.MANUFACTURER_UPDATED.value", "message", "event")
"""


class ManufacturerUpdated(DomainEvent):
    def __init__(self, oldObj: Manufacturer, newObj: Manufacturer):
        super().__init__(
            id=str(uuid4()), name=CommonEventConstant.MANUFACTURER_UPDATED.value
        )
        self._data = {"old": oldObj.toMap(), "new": newObj.toMap()}
