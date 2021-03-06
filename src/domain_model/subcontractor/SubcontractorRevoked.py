"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.organization.Organization import Organization
from src.domain_model.subcontractor.Subcontractor import Subcontractor

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__SubcontractorRevoked, "CommonEventConstant.SUBCONTRACTOR_REVOKED.value", "message", "event")
"""


class SubcontractorRevoked(DomainEvent):
    def __init__(self, subcontractor: Subcontractor, organization: Organization):
        super().__init__(
            id=str(uuid4()), name=CommonEventConstant.SUBCONTRACTOR_REVOKED.value
        )
        self._data = {
            "Subcontractor_id": subcontractor.id(),
            "organization_id": organization.id(),
        }
