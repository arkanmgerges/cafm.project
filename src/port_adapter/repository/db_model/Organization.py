"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship

import src.port_adapter.AppDi as AppDi
from src.port_adapter.repository.db_model.user_organization_junction import associationTable

Base = AppDi.instance.get(AppDi.DbBase)
class Organization(Base):
    __tablename__ = 'organization'
    id = Column('id', String(40), primary_key=True)
    name = Column('name', String(50))
    websiteUrl = Column('website_url', String(50))
    organizationType = Column('organization_type', String(30))
    addressOne = Column('address_one', String(255))
    addressTwo = Column('address_two', String(255))
    postalCode = Column('postal_code', String(30))
    countryId = Column('country_id', Integer, ForeignKey('country.geoname_id'), nullable=False)
    cityId = Column('city_id', Integer, ForeignKey('city.geoname_id'), nullable=False)
    countryStateName = Column('subdivision_1_name', String(100)),
    managerFirstName = Column('manager_first_name', String(50))
    managerLastName = Column('manager_last_name', String(50))
    managerEmail = Column('manager_email', String(50))
    managerPhoneNumber = Column('manager_phone_number', String(25))
    managerAvatar = Column('manager_avatar', String(255))
    createdAt = Column('created_at', DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column('modified_at', DateTime, nullable=True, onupdate=datetime.utcnow())

    # Relationship
    city = relationship('City', uselist=False)
    country = relationship('Country', uselist=False)
    users = relationship(
        "User",
        secondary=associationTable,
        back_populates="organizations")

    def __repr__(self):
        return f"[Repo DB Model] Organization(id='{self.id}', name='{self.name}', \
                websiteUrl='{self.websiteUrl}', organizationType='{self.organizationType}', \
                addressOne='{self.addressOne}', addressTwo='{self.addressTwo}', postalCode='{self.postalCode}', \
                countryId='{self.countryId}', cityId='{self.cityId}', countryStateName='{self.countryStateName}', \
                managerFirstName='{self.managerFirstName}', managerLastName='{self.managerLastName}', \
                managerEmail='{self.managerEmail}', managerPhoneNumber='{self.managerPhoneNumber}', \
                managerAvatar='{self.managerAvatar}')"
