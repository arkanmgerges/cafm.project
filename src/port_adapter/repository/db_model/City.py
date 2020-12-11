"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
import src.port_adapter.AppDi as AppDi
from src.port_adapter.AppDi import DbBase

Base = AppDi.instance.get(DbBase)
class City(Base):
    __tablename__ = 'city'
    geoNameId = Column('geoname_id', Integer, primary_key=True)
    localeCode = Column('locale_code', String(4))
    continentCode = Column('continent_code', String(4))
    continentName = Column('continent_name', String(15))
    countryIsoCode = Column('country_iso_code', String(4), ForeignKey('country.country_iso_code'))
    countryName = Column('country_name', String(50))
    subdivisionOneIsoCode = Column('subdivision_1_iso_code', String(15))
    subdivisionOneIsoName = Column('subdivision_1_name', String(15))
    subdivisionTwoIsoCode = Column('subdivision_2_iso_code', String(15))
    subdivisionTwoIsoName = Column('subdivision_2_name', String(15))
    cityName = Column('city_name', String(50))
    metroCode = Column('metro_code', Integer)
    timeZone = Column('time_zone', String(30))
    isInEuropeanUnion = Column('is_in_european_union', Boolean)
    country = relationship("Country", back_populates="cities")

    def __repr__(self):
        return f"City(geoNameId='{self.geoNameId}', localeCode='{self.localeCode}', continentCode='{self.continentCode}', \
                continentName='{self.continentName}', countryIsoCode='{self.countryIsoCode}', countryName='{self.countryName}', \
                subdivisionOneIsoCode='{self.subdivisionOneIsoCode}', subdivisionOneIsoName='{self.subdivisionOneIsoName}', \
                subdivisionTwoIsoCode='{self.subdivisionTwoIsoCode}', subdivisionTwoIsoName='{self.subdivisionTwoIsoName}', \
                cityName='{self.cityName}', metroCode='{self.metroCode}', timeZone='{self.timeZone}', isInEuropeanUnion='{self.isInEuropeanUnion}')"
