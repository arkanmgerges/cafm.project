from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    'country', meta,
    Column('geoname_id', Integer, primary_key=True),
    Column('locale_code', String(4)),
    Column('continent_code', String(4)),
    Column('continent_name', String(15)),
    Column('country_iso_code', String(5), unique=True),
    Column('country_name', String(50)),
    Column('is_in_european_union', Boolean),
)

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
