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


class DailyCheckProcedureOperationParameter(Base):
    __tablename__ = 'daily_check_procedure_operation_parameter'
    id = Column('id', String(40), primary_key=True)
    name = Column('name', String(255))
    unitId = Column('unit_id', String(40), ForeignKey('unit.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=True)
    dailyCheckProcedureOperationId = Column('daily_check_procedure_operation_id', String(40), ForeignKey('daily_check_procedure_operation.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=True)
    minValue = Column('min_value', Float)
    maxValue = Column('max_value', Float)
    createdAt = Column('created_at', DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column('modified_at', DateTime, nullable=True, onupdate=datetime.utcnow())


    def __repr__(self):
        return f"[Repo DB Model] DailyCheckProcedureOperationParameter(id='{self.id}', name='{self.name}', unitId='{self.unitId}', dailyCheckProcedureOperationId='{self.dailyCheckProcedureOperationId}', minValue='{self.minValue}', maxValue='{self.maxValue}', )"
