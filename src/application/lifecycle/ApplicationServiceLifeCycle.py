"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import Any


class ApplicationServiceLifeCycle:
    _dbContext: Any

    @classmethod
    def begin(cls):
        import src.port_adapter.AppDi as AppDi
        from src.application.lifecycle.BaseDbContainer import BaseDbContainer
        cls._dbContext = AppDi.instance.get(BaseDbContainer).newSession()

    @classmethod
    def success(cls):
        cls._dbContext.commit()

    @classmethod
    def close(cls):
        cls._dbContext.close()

    @classmethod
    def dbContext(cls):
        return cls._dbContext
