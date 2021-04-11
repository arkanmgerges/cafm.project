"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
import src.port_adapter.AppDi as AppDi
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import DateTime

Base = AppDi.instance.get(AppDi.DbBase)


class Project(Base):
    __tablename__ = 'project'
    id = Column('id', String(40), primary_key=True)
    name = Column('name', String(40))
    cityId = Column('city_id', Integer)
    countryId = Column('country_id', Integer)
    startDate = Column('start_date', DateTime, nullable=True)
    addressLine = Column('address_line', String(256))
    addressLineTwo = Column('address_line_two', String(256))
    beneficiaryId = Column('beneficiary_id', String(40))
    state = Column('state', String(30))

    def __repr__(self):
        return f"[Repo DB Model] Project(id='{self.id}', name='{self.name}', cityId='{self.cityId}', \
                countryId='{self.countryId}', addressLine='{self.addressLine}', addressLineTwo='{self.addressLineTwo}', \
                startDate='{self.startDate}', beneficiaryId='{self.beneficiaryId}', state='{self.state}')"
