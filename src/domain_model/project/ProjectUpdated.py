"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

import src.domain_model.ou.Ou as Ou

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.event.EventConstant import CommonEventConstant
from src.domain_model.project.Project import Project

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__ProjectUpdated, "CommonEventConstant.PROJECT_UPDATED.value", "message", "event")
"""
class ProjectUpdated(DomainEvent):
    def __init__(self, oldObj: Ou, newObj: Project):
        super().__init__(id=str(uuid4()), name=CommonEventConstant.PROJECT_UPDATED.value)
        self._data = {'old': oldObj.toMap(), 'new': newObj.toMap()}
