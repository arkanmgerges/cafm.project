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


class DailyCheckProcedure(Base):
    __tablename__ = 'daily_check_procedure'
    id = Column('id', String(40), primary_key=True)
    name = Column('name', String(40))
    description = Column('description', String(255))
    equipmentId = Column('equipment_id', String(40), ForeignKey('equipment.id'), nullable=True)
    equipmentCategoryGroupId = Column('equipment_category_group_id', String(40), ForeignKey('equipment_category_group.id'), nullable=True)
    createdAt = Column('created_at', DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column('modified_at', DateTime, nullable=True, onupdate=datetime.utcnow())


    def __repr__(self):
        return f"[Repo DB Model] DailyCheckProcedure(id='{self.id}', name='{self.name}', description='{self.description}', equipmentId='{self.equipmentId}', equipmentCategoryGroupId='{self.equipmentCategoryGroupId}', )"
