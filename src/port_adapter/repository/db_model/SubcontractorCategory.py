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


class SubcontractorCategory(Base):
    __tablename__ = "subcontractor_category"
    id = Column("id", String(40), primary_key=True)
    name = Column("name", String(40))
    createdAt = Column("created_at", DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column(
        "modified_at", DateTime, nullable=True, onupdate=datetime.utcnow()
    )

    # Relationship
    categorySubcontractors = relationship(
        "Subcontractor", back_populates="subcontractorCategory"
    )

    def __repr__(self):
        return f"[Repo DB Model] SubcontractorCategory(id='{self.id}', name='{self.name}', )"
