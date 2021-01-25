"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


class DbSession:
    @staticmethod
    def newSession(dbEngine: Engine) -> Session:
        SessionFactory = sessionmaker(bind=dbEngine)
        return SessionFactory()
