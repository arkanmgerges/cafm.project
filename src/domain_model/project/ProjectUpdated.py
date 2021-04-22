"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.Project import Project

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__ProjectUpdated, "CommonEventConstant.PROJECT_UPDATED.value", "message", "event")
"""


class ProjectUpdated(DomainEvent):
    def __init__(self, oldObj: Project, newObj: Project):
        super().__init__(
            id=str(uuid4()), name=CommonEventConstant.PROJECT_UPDATED.value
        )
        self._data = {"old": oldObj.toMap(), "new": newObj.toMap()}
