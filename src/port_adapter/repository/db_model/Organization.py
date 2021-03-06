"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

import src.port_adapter.AppDi as AppDi
from src.port_adapter.repository.db_model.subcontractor__organization__junction import (
    associationTable as subcontractorAssociationTable,
)
from src.port_adapter.repository.db_model.role__organization__junction import (
    associationTable as roleAssociationTable,
)
from src.port_adapter.repository.db_model.project__organization__junction import (
    associationTable as projectAssociationTable,
)

Base = AppDi.instance.get(AppDi.DbBase)


class Organization(Base):
    __tablename__ = "organization"
    id = Column("id", String(40), primary_key=True)
    name = Column("name", String(50))
    websiteUrl = Column("website_url", String(50))
    organizationType = Column("organization_type", String(30))
    addressOne = Column("address_one", String(255))
    addressTwo = Column("address_two", String(255))
    postalCode = Column("postal_code", String(30))
    countryId = Column(
        "country_id",
        Integer,
        nullable=True,
    )
    cityId = Column(
        "city_id",
        Integer,
        nullable=True,
    )
    countryStateName = Column("subdivision_1_name", String(100))
    countryStateIsoCode = Column("subdivision_1_iso_code", String(15))
    managerFirstName = Column("manager_first_name", String(50))
    managerLastName = Column("manager_last_name", String(50))
    managerEmail = Column("manager_email", String(50))
    managerPhoneNumber = Column("manager_phone_number", String(25))
    managerAvatar = Column("manager_avatar", String(255))
    createdAt = Column("created_at", DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column(
        "modified_at", DateTime, nullable=True, onupdate=datetime.utcnow()
    )

    # Relationship
    roles = relationship(
        "Role",
        secondary=roleAssociationTable,
        back_populates="organizations",
    )
    subcontractors = relationship(
        "Subcontractor",
        secondary=subcontractorAssociationTable,
        back_populates="organizations",
    )
    projects = relationship(
        "Project",
        secondary=projectAssociationTable,
        back_populates="organizations",
    )

    def __repr__(self):
        return f"[Repo DB Model] Organization(id='{self.id}', name='{self.name}', \
                websiteUrl='{self.websiteUrl}', organizationType='{self.organizationType}', \
                addressOne='{self.addressOne}', addressTwo='{self.addressTwo}', postalCode='{self.postalCode}', \
                countryId='{self.countryId}', cityId='{self.cityId}', \
                    countryStateName='{self.countryStateName}', \
                    countryStateIsoCode='{self.countryStateIsoCode}', \
                managerFirstName='{self.managerFirstName}', managerLastName='{self.managerLastName}', \
                managerEmail='{self.managerEmail}', managerPhoneNumber='{self.managerPhoneNumber}', \
                managerAvatar='{self.managerAvatar}')"
