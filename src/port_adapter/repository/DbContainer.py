"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from src.application.lifecycle.BaseDbContainer import BaseDbContainer


class DbContainer (BaseDbContainer):
    @classmethod
    def newSession(cls) -> Session:
        try:
            from sqlalchemy import create_engine
            import os
            dbEngine = create_engine(
                f"mysql+mysqlconnector://{os.getenv('CAFM_PROJECT_DB_USER', 'root')}:{os.getenv('CAFM_PROJECT_DB_PASSWORD', '1234')}@{os.getenv('CAFM_PROJECT_DB_HOST', '127.0.0.1')}:{os.getenv('CAFM_PROJECT_DB_PORT', '3306')}/{os.getenv('CAFM_PROJECT_DB_NAME', 'cafm-project')}"
            )
            SessionFactory = sessionmaker(bind=dbEngine, autoflush=True, autocommit=False)
            return SessionFactory()
        except Exception as e:
            from src.resource.logging.logger import logger
            logger.warn(
                f"[{DbContainer.newSession.__qualname__}] Could not connect to the db, message: {e}"
            )
            raise Exception(f"Could not connect to the db, message: {e}")

