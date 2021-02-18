"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from sqlalchemy.sql.sqltypes import DateTime

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)


class EquipmentCategoryGroup(Base):
    __tablename__ = 'equipment_category_group'
    id = Column('id', String(40), primary_key=True)
    name = Column('name', String(40))
    equipmentCategoryId = Column('equipment_category_id', String(40), ForeignKey('equipment_category.id', ondelete='CASCADE'), nullable=False)
    createdAt = Column('created_at', DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column('modified_at', DateTime, nullable=True, onupdate=datetime.utcnow())

    # Relationship
    category = relationship(
        "EquipmentCategory",
        back_populates="groups", lazy='joined')

    def __repr__(self):
        return f"[Repo DB Model] EquipmentCategoryGroup(id='{self.id}', name='{self.name}')"
