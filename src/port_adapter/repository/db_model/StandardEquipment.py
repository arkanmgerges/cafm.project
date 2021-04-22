"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)


class StandardEquipment(Base):
    __tablename__ = "standard_equipment"
    id = Column("id", String(40), primary_key=True)
    name = Column("name", String(40))
    manufacturerId = Column(
        "manufacturer_id",
        String(40),
        ForeignKey("manufacturer.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=True,
    )
    equipmentModelId = Column(
        "equipment_model_id",
        String(40),
        ForeignKey("equipment_model.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=True,
    )
    standardEquipmentCategoryId = Column(
        "standard_equipment_category_id",
        String(40),
        ForeignKey(
            "standard_equipment_category.id", ondelete="CASCADE", onupdate="CASCADE"
        ),
        nullable=True,
    )
    standardEquipmentCategoryGroupId = Column(
        "standard_equipment_category_group_id",
        String(40),
        ForeignKey(
            "standard_equipment_category_group.id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=True,
    )
    createdAt = Column("created_at", DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column(
        "modified_at", DateTime, nullable=True, onupdate=datetime.utcnow()
    )

    # Relationship
    standardManufacturer = relationship("Manufacturer", lazy="select")
    standardEquipmentModel = relationship("EquipmentModel", lazy="select")
    standardEquipmentCategory = relationship("StandardEquipmentCategory", lazy="select")
    standardEquipmentCategoryGroup = relationship(
        "StandardEquipmentCategoryGroup", lazy="select"
    )

    def __repr__(self):
        return f"[Repo DB Model] name='{self.name}')"
