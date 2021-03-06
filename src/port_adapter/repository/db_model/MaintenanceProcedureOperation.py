"""
The file is generated by a scaffold script
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""


from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship
import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)


class MaintenanceProcedureOperation(Base):
    __tablename__ = "maintenance_procedure_operation"
    id = Column("id", String(40), primary_key=True)
    name = Column("name", String(255))
    description = Column("description", String(255))
    type = Column("type", String(10))
    maintenanceProcedureId = Column(
        "maintenance_procedure_id",
        String(40),
        ForeignKey("maintenance_procedure.id", onupdate="CASCADE"),
        nullable=True,
    )
    createdAt = Column("created_at", DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column(
        "modified_at", DateTime, nullable=True, onupdate=datetime.utcnow()
    )

    # Relationships
    procedure = relationship(
        "MaintenanceProcedure", back_populates="operations", lazy="joined"
    )

    parameters = relationship(
        "MaintenanceProcedureOperationParameter",
        back_populates="operation",
        lazy="joined",
    )

    def __repr__(self):
        return f"[Repo DB Model] MaintenanceProcedureOperation(id='{self.id}', name='{self.name}', description='{self.description}', type='{self.type}', maintenanceProcedureId='{self.maintenanceProcedureId}', )"
