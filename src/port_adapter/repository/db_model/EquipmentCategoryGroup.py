"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

import src.port_adapter.AppDi as AppDi
from src.port_adapter.repository.db_model.equipment_project_category__equipment_category_group__junction import (
    associationTable,
)

Base = AppDi.instance.get(AppDi.DbBase)


class EquipmentCategoryGroup(Base):
    __tablename__ = "equipment_category_group"
    id = Column("id", String(40), primary_key=True)
    name = Column("name", String(40))
    projectId = Column("project_id", String(40))
    createdAt = Column("created_at", DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column(
        "modified_at", DateTime, nullable=True, onupdate=datetime.utcnow()
    )

    # Relationship
    equipmentProjectCategories = relationship(
        "EquipmentProjectCategory",
        secondary=associationTable,
        back_populates="equipmentCategoryGroups",
    )

    def __repr__(self):
        return f"[Repo DB Model] EquipmentCategoryGroup(id='{self.id}', name='{self.name}, project_id='{self.projectId}')"
