from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

import src.port_adapter.AppDi as AppDi
from src.port_adapter.repository.db_model.role__tag__junction import (
    associationTable as roleAssociationTable,
)
Base = AppDi.instance.get(AppDi.DbBase)


class Tag(Base):
    __tablename__ = "tag"
    id = Column("id", String(40), primary_key=True)
    name = Column("name", String(40))
    createdAt = Column("created_at", DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column(
        "modified_at", DateTime, nullable=True, onupdate=datetime.utcnow()
    )

    # Relationship
    roles = relationship(
        "Role",
        secondary=roleAssociationTable,
        back_populates="tags",
    )

    def __repr__(self):
        return f"[Repo DB Model] Tag(id='{self.id}', name='{self.name}')"
