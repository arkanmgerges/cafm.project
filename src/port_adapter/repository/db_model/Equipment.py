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
    __tablename__ = 'equipment'
    id = Column('id', String(40), primary_key=True)
    name = Column('name', String(40))
    projectId = Column('project_id', String(40), ForeignKey('project.id'), nullable=False)
    manufacturerId = Column('manufacturer_id', String(40), ForeignKey('manufacturer.id'), nullable=False)
    equipmentModelId = Column('equipment_model_id', String(40), ForeignKey('equipment_model.id'), nullable=False)
    equipmentProjectCategoryId = Column('equipment_project_category_id', String(40), ForeignKey('equipment_project_category.id'), nullable=False)
    equipmentCategoryId = Column('equipment_category_id', String(40), ForeignKey('equipment_category.id'), nullable=False)
    equipmentCategoryGroupId = Column('equipment_category_group_id', String(40), ForeignKey('equipment_category_group.id'), nullable=False)
    buildingId = Column('building_id', String(40), ForeignKey('building.id'), nullable=False)
    buildingLevelId = Column('building_level_id', String(40), ForeignKey('building_level.id'), nullable=False)
    buildingLevelRoomId = Column('building_level_room_id', String(40), ForeignKey('building_level_room.id'), nullable=False)
    quantity = Column('quantity', Integer)
    createdAt = Column('created_at', DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column('modified_at', DateTime, nullable=True, onupdate=datetime.utcnow())

    # Relationship
    building = relationship(
        "Building", lazy='joined')
    buildingLevel = relationship(
        "BuildingLevel", lazy='joined')
    buildingLevelRoom = relationship(
        "BuildingLevelRoom", lazy='joined')

    manufacturer = relationship('Manufacturer', lazy='joined')
    equipmentModel = relationship('EquipmentModel', lazy='joined')
    equipmentProjectCategory = relationship('EquipmentProjectCategory', lazy='joined')
    equipmentCategory = relationship('EquipmentCategory', lazy='joined')
    equipmentCategoryGroup = relationship('EquipmentCategoryGroup', lazy='joined')



    def __repr__(self):
        return f"[Repo DB Model] Building(id='{self.id}', projectId='{self.projectId}', \
                name='{self.name}')"
