"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)


class EquipmentCategory(Base):
    __tablename__ = 'equipment_category'
    id = Column('id', String(40), primary_key=True)
    name = Column('name', String(40))
    createdAt = Column('created_at', DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column('modified_at', DateTime, nullable=True, onupdate=datetime.utcnow())

    # Relationship
    groups = relationship(
        "EquipmentCategoryGroup",
        back_populates="category", lazy='joined')

    def __repr__(self):
        return f"[Repo DB Model] EquipmentCategory(id='{self.id}', name='{self.name}')"
