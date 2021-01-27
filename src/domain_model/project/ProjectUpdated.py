"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

import src.domain_model.ou.Ou as Ou

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.project.Project import Project

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__ProjectUpdated, "Project Updated", "event", "message")
"""
class ProjectUpdated(DomainEvent):
    def __init__(self, oldObj: Ou, newObj: Project):
        super().__init__(id=str(uuid4()), name='project_updated')
        self._data = {'old': oldObj.toMap(), 'new': newObj.toMap()}
