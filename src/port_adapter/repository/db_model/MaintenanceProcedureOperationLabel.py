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


class MaintenanceProcedureOperationLabel(Base):
    __tablename__ = 'maintenance_procedure_operation_label'
    id = Column('id', String(40), primary_key=True)
    label = Column('label', String(40))
    generateAlert = Column('generate_alert', Integer)
    maintenanceProcedureOperationId = Column('maintenance_procedure_operation_id', String(40), ForeignKey('maintenance_procedure_operation.id'), nullable=False)
    createdAt = Column('created_at', DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column('modified_at', DateTime, nullable=True, onupdate=datetime.utcnow())


    def __repr__(self):
        return f"[Repo DB Model] MaintenanceProcedureOperationLabel(id='{self.id}', label='{self.label}', generateAlert='{self.generateAlert}', maintenanceProcedureOperationId='{self.maintenanceProcedureOperationId}', )"