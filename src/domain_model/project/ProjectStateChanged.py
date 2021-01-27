"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.project.ProjectState import ProjectState

"""
c4model|cb|project:ComponentQueue(project__domainmodel_event__ProjectStateChanged, "Project State Changed", "event", "message")
"""
class ProjectStateChanged(DomainEvent):
    def __init__(self, oldState: ProjectState, newState: ProjectState):
        super().__init__(id=str(uuid4()), name='project_state_changed')
        self._data = {"old_state": oldState.value, "new_state": newState.value}
