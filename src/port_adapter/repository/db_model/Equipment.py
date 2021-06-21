"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)


class Equipment(Base):
    __tablename__ = "equipment"
    id = Column("id", String(40), primary_key=True)
    name = Column("name", String(40))
    projectId = Column(
        "project_id",
        String(40),
        ForeignKey("project.id", onupdate="CASCADE"),
        nullable=True,
    )
    manufacturerId = Column(
        "manufacturer_id",
        String(40),
        ForeignKey("manufacturer.id", onupdate="CASCADE"),
        nullable=True,
    )
    equipmentModelId = Column(
        "equipment_model_id",
        String(40),
        ForeignKey("equipment_model.id", onupdate="CASCADE"),
        nullable=True,
    )
    equipmentProjectCategoryId = Column(
        "equipment_project_category_id",
        String(40),
        ForeignKey(
            "equipment_project_category.id", onupdate="CASCADE"
        ),
        nullable=True,
    )
    equipmentCategoryGroupId = Column(
        "equipment_category_group_id",
        String(40),
        ForeignKey(
            "equipment_category_group.id", onupdate="CASCADE"
        ),
        nullable=True,
    )
    buildingId = Column(
        "building_id",
        String(40),
        ForeignKey("building.id", onupdate="CASCADE"),
        nullable=True,
    )
    buildingLevelId = Column(
        "building_level_id",
        String(40),
        ForeignKey("building_level.id", onupdate="CASCADE"),
        nullable=True,
    )
    buildingLevelRoomId = Column(
        "building_level_room_id",
        String(40),
        ForeignKey("building_level_room.id", onupdate="CASCADE"),
        nullable=True,
    )
    quantity = Column("quantity", Integer)
    createdAt = Column("created_at", DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column(
        "modified_at", DateTime, nullable=True, onupdate=datetime.utcnow()
    )

    # Relationship
    building = relationship("Building", lazy="select")
    buildingLevel = relationship("BuildingLevel", lazy="select")
    buildingLevelRoom = relationship("BuildingLevelRoom", lazy="select")

    manufacturer = relationship("Manufacturer", lazy="select")
    equipmentModel = relationship("EquipmentModel", lazy="select")
    equipmentProjectCategory = relationship("EquipmentProjectCategory", lazy="select")
    equipmentCategoryGroup = relationship("EquipmentCategoryGroup", lazy="select")
    maintenanceProcedures = relationship("MaintenanceProcedure", lazy="select")

    def __repr__(self):
        return f"[Repo DB Model] Building(id='{self.id}', projectId='{self.projectId}', \
                name='{self.name}')"
