"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.subcontractor.Subcontractor import Subcontractor

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__SubcontractorDeleted, "CommonEventConstant.SUBCONTRACTOR_DELETED.value", "event", "message")
"""
class SubcontractorDeleted(DomainEvent):
    def __init__(self, object: Subcontractor):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.SUBCONTRACTOR_DELETED.value)
        self._data = object.toMap()
