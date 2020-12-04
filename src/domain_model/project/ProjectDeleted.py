"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from uuid import uuid4

from src.domain_model.event.DomainEvent import DomainEvent
from src.domain_model.project.Project import Project


class ProjectDeleted(DomainEvent):
    def __init__(self, obj: Project):
        super().__init__(id=str(uuid4()), name='project_deleted')
        self._data = obj.toMap()
