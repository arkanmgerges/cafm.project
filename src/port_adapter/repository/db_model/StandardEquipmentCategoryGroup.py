"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship
import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)


class StandardEquipmentCategoryGroup(Base):
    __tablename__ = 'standard_equipment_category_group'
    id = Column('id', String(40), primary_key=True)
    name = Column('name', String(40))
    standardEquipmentCategoryId = Column('standard_equipment_category_id', String(40),
                                         ForeignKey('standard_equipment_category.id', ondelete='CASCADE'),
                                         nullable=False)
    createdAt = Column('created_at', DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column('modified_at', DateTime, nullable=True, onupdate=datetime.utcnow())

    # Relationship
    standardCategory = relationship(
        "StandardEquipmentCategory",
        back_populates="standardGroups", lazy='joined')

    def __repr__(self):
        return f"[Repo DB Model] StandardEquipmentCategoryGroup(id='{self.id}', name='{self.name}', " \
               f"standardEquipmentCategoryId='{self.standardEquipmentCategoryId}', ) "
