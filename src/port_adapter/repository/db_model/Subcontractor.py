"""
@author: Mohammad S. moso<moso@develoop.run>
"""
from datetime import datetime

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

import src.port_adapter.AppDi as AppDi
from src.port_adapter.repository.db_model.subcontractor__organization__junction import associationTable

Base = AppDi.instance.get(AppDi.DbBase)


class Subcontractor(Base):
    __tablename__ = 'subcontractor'
    id = Column('id', String(40), primary_key=True)
    companyName = Column('company_name', String(50))
    websiteUrl = Column('website', String(50))
    contactPerson = Column('contact_person', String(255))
    email = Column('email', String(50))
    phoneNumber = Column('phone_number', String(30))
    addressOne = Column('address_one', String(255))
    addressTwo = Column('address_two', String(255))
    createdAt = Column('created_at', DateTime, nullable=True, default=datetime.utcnow())
    modifiedAt = Column('modified_at', DateTime, nullable=True, onupdate=datetime.utcnow())

    # Relationship
    organizations = relationship(
        "Organization",
        secondary=associationTable,
        back_populates="subcontractors")

    def __repr__(self):
        return f"[Repo DB Model] Subcontractor(id='{self.id}', companyName='{self.companyName}', \
                websiteUrl='{self.websiteUrl}', contactPerson='{self.contactPerson}', email='{self.email}', \
                phoneNumber='{self.phoneNumber}', addressOne='{self.addressOne}', addressTwo='{self.addressTwo}')"
