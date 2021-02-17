"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.subcontractor.Subcontractor import Subcontractor

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__SubcontractorUpdated, "CommonEventConstant.SUBCONTRACTOR_UPDATED.value", "message", "event")
"""


class SubcontractorUpdated(DomainEvent):
    def __init__(self, oldObject: Subcontractor, newObject: Subcontractor):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.SUBCONTRACTOR_UPDATED.value)
        self._data = {'old': oldObject.toMap(), 'new': newObject.toMap()}
