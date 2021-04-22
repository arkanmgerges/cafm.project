"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.manufacturer.Manufacturer import Manufacturer

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__ManufacturerDeleted, "CommonEventConstant.MANUFACTURER_DELETED.value", "message", "event")
"""


class ManufacturerDeleted(DomainEvent):
    def __init__(self, obj: Manufacturer):
        super().__init__(
            id=str(uuid4()), name=CommonEventConstant.MANUFACTURER_DELETED.value
        )
        self._data = obj.toMap()
