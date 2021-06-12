"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from abc import ABC, abstractmethod


class BaseDbContainer(ABC):
    @abstractmethod
    def newSession(self):
        pass