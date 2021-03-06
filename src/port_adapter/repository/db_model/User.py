"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

import src.port_adapter.AppDi as AppDi
from src.port_adapter.repository.db_model.user__role__junction import (
    associationTable as roleAssociationTable,
)

Base = AppDi.instance.get(AppDi.DbBase)


class User(Base):
    __tablename__ = "user"
    id = Column("id", String(40), primary_key=True)
    email = Column("email", String(50))
    firstName = Column("first_name", String(255))
    lastName = Column("last_name", String(255))
    addressOne = Column("address_one", String(255))
    addressTwo = Column("address_two", String(255))
    postalCode = Column("postal_code", String(30))
    phoneNumber = Column("phone_number", String(30))
    avatarImage = Column("avatar_image", String(255))
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
    startDate = Column("start_date", DateTime, nullable=True)
    createdAt = Column("created_at", DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column(
        "modified_at", DateTime, nullable=True, onupdate=datetime.utcnow()
    )

    # Relationship
    roles = relationship("Role", secondary=roleAssociationTable, back_populates="users")

    def __repr__(self):
        return f"[Repo DB Model] User(id='{self.id}', email='{self.email}', \
                firstName='{self.firstName}', lastName='{self.lastName}', addressOne='{self.addressOne}', \
                addressTwo='{self.addressTwo}', postalCode='{self.postalCode}, phoneNumber='{self.phoneNumber}', \
                avatarImage='{self.avatarImage}', \
                countryId='{self.countryId}', cityId='{self.cityId}', \
                    countryStateName='{self.countryStateName}', \
                    countryStateIsoCode='{self.countryStateIsoCode}', \
                startDate='{self.startDate}')"
