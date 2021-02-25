"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""



from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)


class EquipmentInput(Base):
    __tablename__ = 'equipment_input'
    id = Column('id', String(40), primary_key=True)
    name = Column('name', String(40))
    value = Column('value', String(40))
    unitId = Column('unit_id', String(40), ForeignKey('unit.id'), nullable=False)
    createdAt = Column('created_at', DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column('modified_at', DateTime, nullable=True, onupdate=datetime.utcnow())


    def __repr__(self):
        return f"[Repo DB Model] EquipmentInput(id='{self.id}', name='{self.name}', value='{self.value}', unitId='{self.unitId}', )"
