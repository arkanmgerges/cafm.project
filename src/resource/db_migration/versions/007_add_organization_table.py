from sqlalchemy import *
from migrate import *


meta = MetaData()

tbl = Table(
    'organization', meta,
    Column('id', String(40), primary_key=True),
    Column('name', String(50)),
    Column('website_url', String(50)),
    Column('organization_type', String(30)),
    Column('address_one', String(255)),
    Column('address_two', String(255)),
    Column('postal_code', String(30)),
    Column('country_id', Integer, ForeignKey('country.geoname_id'), nullable=False),
    Column('city_id', Integer, ForeignKey('city.geoname_id'), nullable=False),
    Column('subdivision_1_name', String(100)),
    Column('manager_first_name', String(50)),
    Column('manager_last_name', String(50)),
    Column('manager_email', String(50)),
    Column('manager_phone_number', String(25)),
    Column('manager_avatar', String(255)),
    Column('modified_at', DateTime),
    Column('created_at', DateTime)
)

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    _t = Table('country', meta, autoload=True)
    _t = Table('city', meta, autoload=True)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
