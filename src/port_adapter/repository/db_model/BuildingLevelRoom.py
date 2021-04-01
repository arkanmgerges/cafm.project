"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)


class BuildingLevelRoom(Base):
    __tablename__ = 'building_level_room'
    id = Column('id', String(40), primary_key=True)
    name = Column('name', String(40))
    description = Column('description', String(255))
    index = Column('index', Integer)
    buildingLevelId = Column('building_level_id', String(40), ForeignKey('building_level.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=True)
    createdAt = Column('created_at', DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column('modified_at', DateTime, nullable=True, onupdate=datetime.utcnow())

    # Relationship
    level = relationship(
        "BuildingLevel",
        back_populates="rooms", lazy='joined')


    def __repr__(self):
        return f"[Repo DB Model] BuildingLevelRoom(id='{self.id}', name='{self.name}', \
                description='{self.description}', index='{self.index}')"
