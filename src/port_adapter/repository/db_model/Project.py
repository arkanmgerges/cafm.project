"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from sqlalchemy import Column, Integer, String, Boolean
import src.port_adapter.AppDi as AppDi

Base = AppDi.instance.get(AppDi.DbBase)
class Project(Base):
    __tablename__ = 'project'
    id = Column('id', String(40), primary_key=True)
    name = Column('name', String(40))
    cityId = Column('city_id', Integer)
    countryId = Column('country_id', Integer)
    addressLine = Column('address_line', String(256))
    beneficiaryId = Column('beneficiary_id', String(40))
    state = Column('state', String(30))

    def __repr__(self):
        return f"Project(id='{self.id}', name='{self.name}', cityId='{self.cityId}', \
                countryId='{self.countryId}', addressLine='{self.addressLine}', beneficiaryId='{self.beneficiaryId}', \
                state='{self.state}')"
