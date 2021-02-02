"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

import src.port_adapter.AppDi as AppDi
from src.port_adapter.repository.db_model.building__level__junction import associationTable as levelAssociationTable

Base = AppDi.instance.get(AppDi.DbBase)


class Building(Base):
    __tablename__ = 'building'
    id = Column('id', String(40), primary_key=True)
    projectId = Column('project_id', String(40), ForeignKey('project.id'), nullable=False)
    name = Column('name', String(40))
    createdAt = Column('created_at', DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column('modified_at', DateTime, nullable=True, onupdate=datetime.utcnow())

    # Relationship
    levels = relationship(
        "BuildingLevel",
        secondary=levelAssociationTable,
        back_populates="buildings", lazy='joined')


    def __repr__(self):
        return f"[Repo DB Model] Building(id='{self.id}', projectId='{self.projectId}', \
                name='{self.name}')"
