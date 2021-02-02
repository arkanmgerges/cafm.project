"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship

import src.port_adapter.AppDi as AppDi
from src.port_adapter.repository.db_model.user__role__junction import associationTable

Base = AppDi.instance.get(AppDi.DbBase)
class Role(Base):
    __tablename__ = 'role'
    id = Column('id', String(40), primary_key=True)
    name = Column('name', String(50))
    title = Column('title', String(50))
    createdAt = Column('created_at', DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column('modified_at', DateTime, nullable=True, onupdate=datetime.utcnow())

    # Relationship
    users = relationship(
        "User",
        secondary=associationTable,
        back_populates="roles")

    def __repr__(self):
        return f"[Repo DB Model] Role(id='{self.id}', name='{self.name}')"
