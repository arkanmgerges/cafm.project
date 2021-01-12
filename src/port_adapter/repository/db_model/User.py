"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

import src.port_adapter.AppDi as AppDi
from src.port_adapter.repository.db_model.user_organization_junction import associationTable as \
    organizationAssociationTable
from src.port_adapter.repository.db_model.user_role_junction import associationTable as roleAssociationTable

Base = AppDi.instance.get(AppDi.DbBase)


class User(Base):
    __tablename__ = 'user'
    id = Column('id', String(40), primary_key=True)
    email = Column('email', String(50))
    firstName = Column('first_name', String(25))
    lastName = Column('last_name', String(25))
    addressOne = Column('address_one', String(255))
    addressTwo = Column('address_two', String(255))
    postalCode = Column('postal_code', String(30))
    phoneNumber = Column('phone_number', String(30))
    avatarImage = Column('avatar_image', String(255))
    countryId = Column('country_id', Integer, ForeignKey('country.geoname_id'), nullable=False)
    cityId = Column('city_id', Integer, ForeignKey('city.geoname_id'), nullable=False)
    countryStateName = Column('subdivision_1_name', String(100))
    startDate = Column('start_date', DateTime, nullable=True)
    createdAt = Column('created_at', DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column('modified_at', DateTime, nullable=True, onupdate=datetime.utcnow())

    # Relationship
    city = relationship('City', uselist=False)
    country = relationship('Country', uselist=False)
    roles = relationship(
        "Role",
        secondary=roleAssociationTable,
        back_populates="users")
    organizations = relationship(
        "Organization",
        secondary=organizationAssociationTable,
        back_populates="users")

    def __repr__(self):
        return f"[Repo DB Model] User(id='{self.id}', email='{self.email}', \
                firstName='{self.firstName}', lastName='{self.lastName}', addressOne='{self.addressOne}', \
                addressTwo='{self.addressTwo}', postalCode='{self.postalCode}', avatarImage='{self.avatarImage}', \
                countryId='{self.countryId}', cityId='{self.cityId}', countryStateName='{self.countryStateName}', \
                startDate='{self.startDate}')"
