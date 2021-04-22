"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
import src.port_adapter.AppDi as AppDi


Base = AppDi.instance.get(AppDi.DbBase)


class Country(Base):
    __tablename__ = "country"
    geoNameId = Column("geoname_id", Integer, primary_key=True)
    localeCode = Column("locale_code", String(4))
    continentCode = Column("continent_code", String(4))
    continentName = Column("continent_name", String(15))
    countryIsoCode = Column("country_iso_code", String(5), unique=True)
    countryName = Column("country_name", String(50))
    isInEuropeanUnion = Column("is_in_european_union", Boolean)

    # Relationship
    # cities = relationship("City", back_populates="country")

    def __repr__(self):
        return f"[Repo DB Model] Country(geoNameId='{self.geoNameId}', localeCode='{self.localeCode}', continentCode='{self.continentCode}', \
                continentName='{self.continentName}', countryIsoCode='{self.countryIsoCode}', countryName='{self.countryName}', \
                isInEuropeanUnion='{self.isInEuropeanUnion}')"
