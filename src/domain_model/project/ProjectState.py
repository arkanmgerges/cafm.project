"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from enum import Enum


class ProjectState(Enum):
    DRAFT = "draft"
    ACTIVE = "active"
    ARCHIVED = "archived"
