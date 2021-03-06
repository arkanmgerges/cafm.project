"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

import src.port_adapter.AppDi as AppDi
from src.port_adapter.repository.db_model.role__project__junction import (
    associationTable as roleAssociationTable,
)
from src.port_adapter.repository.db_model.project__organization__junction import (
    associationTable as organizationAssociationTable,
)

Base = AppDi.instance.get(AppDi.DbBase)


class Project(Base):
    __tablename__ = "project"
    id = Column("id", String(40), primary_key=True)
    name = Column("name", String(40))
    cityId = Column("city_id", Integer)
    countryId = Column("country_id", Integer)
    startDate = Column("start_date", DateTime, nullable=True)
    addressLine = Column("address_line", String(256))
    addressLineTwo = Column("address_line_two", String(256))
    beneficiaryId = Column("beneficiary_id", String(40))
    postalCode = Column("postal_code", String(40))
    countryStateName = Column("subdivision_1_name", String(100))
    countryStateIsoCode = Column("subdivision_1_iso_code", String(15))
    state = Column("state", String(30))
    developerName = Column("developer_name", String(40))
    developerCityId = Column(
        "developer_city_id",
        Integer,
        nullable=True,
    )
    developerCountryId = Column(
        "developer_country_id",
        Integer,
        nullable=True,
    )
    developerAddressLineOne = Column("developer_address_line_one", String(256))
    developerAddressLineTwo = Column("developer_address_line_two", String(256))
    developerContact = Column("developer_contact_person", String(100))
    developerEmail = Column("developer_email", String(50))
    developerPhoneNumber = Column("developer_phone_number", String(25))
    developerWarranty = Column("developer_warranty", String(255))
    developerPostalCode = Column("developer_postal_code", String(255))
    developerCountryStateName = Column(
        "developer_subdivision_1_name", String(100))
    developerCountryStateIsoCode = Column(
        "developer_subdivision_1_iso_code", String(15))
    modifiedAt = Column("modified_at", DateTime)
    createdAt = Column("created_at", DateTime)

    # Relationship
    roles = relationship(
        "Role",
        secondary=roleAssociationTable,
        back_populates="projects",
    )
    organizations = relationship(
        "Organization",
        secondary=organizationAssociationTable,
        back_populates="projects",
    )

    def __repr__(self):
        return f"[Repo DB Model] Project(id='{self.id}', name='{self.name}', cityId='{self.cityId}', \
                countryId='{self.countryId}', addressLine='{self.addressLine}', addressLineTwo='{self.addressLineTwo}', \
                startDate='{self.startDate}', beneficiaryId='{self.beneficiaryId}', state='{self.state}', \
                postalCode='{self.postalCode}', \
                countryStateName='{self.countryStateName}', \
                countryStateIsoCode='{self.countryStateIsoCode}', \
                developerName='{self.developerName}', developerCityId='{self.developerCityId}', \
                developerCountryId='{self.developerCountryId}', developerAddressLineOne='{self.developerAddressLineOne}', \
                developerAddressLineTwo='{self.developerAddressLineTwo}', developerContactPerson='{self.developerContact}', \
                developerEmail='{self.developerEmail}', developerPhone='{self.developerPhoneNumber}', developerWarranty='{self.developerWarranty}, \
                developerPostalCode='{self.developerPostalCode} \
                developerCountryStateName='{self.developerCountryStateName}', \
                developerCountryStateIsoCode='{self.developerCountryStateIsoCode}', \
                createdAt='{self.createdAt}', \
                modifiedAt='{self.modifiedAt}', \
                 ')"
