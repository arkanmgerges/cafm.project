"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

import src.port_adapter.AppDi as AppDi
from src.port_adapter.repository.db_model.building__level__junction import associationTable as buildingAssociationTable

Base = AppDi.instance.get(AppDi.DbBase)


class BuildingLevel(Base):
    __tablename__ = 'building_level'
    id = Column('id', String(40), primary_key=True)
    name = Column('name', String(40))
    createdAt = Column('created_at', DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column('modified_at', DateTime, nullable=True, onupdate=datetime.utcnow())

    # Relationship
    buildings = relationship(
        "Building",
        secondary=buildingAssociationTable,
        back_populates="levels", lazy='joined')

    rooms = relationship('BuildingLevelRoom', back_populates="level", lazy='joined')


    def __repr__(self):
        return f"[Repo DB Model] BuildingLevel(id='{self.id}', name='{self.name}')"
