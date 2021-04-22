from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    "city",
    meta,
    Column("geoname_id", Integer, primary_key=True),
    Column("locale_code", String(4)),
    Column("continent_code", String(4)),
    Column("continent_name", String(15)),
    # Column('country_iso_code', String(4), ForeignKey('country.country_iso_code')),
    Column("country_iso_code", String(4)),
    Column("country_name", String(50)),
    Column("subdivision_1_iso_code", String(15)),
    Column("subdivision_1_name", String(100)),
    Column("subdivision_2_iso_code", String(15)),
    Column("subdivision_2_name", String(100)),
    Column("city_name", String(100)),
    Column("metro_code", Integer, nullable=True),
    Column("time_zone", String(30)),
    Column("is_in_european_union", Boolean),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    # You can load the table country for adding foreign keys mentioned above if this is desired
    # _t = Table('country', meta, autoload=True)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    # You can load the table country for removing the foreign keys mentioned above if this is desired
    # _t = Table('country', meta, autoload=True)
    tbl.drop()
