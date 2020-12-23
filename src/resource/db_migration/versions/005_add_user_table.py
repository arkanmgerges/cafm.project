from sqlalchemy import *
from migrate import *


meta = MetaData()

tbl = Table(
    'user', meta,
    Column('id', String(40), primary_key=True),
    Column('name', String(50)),
    Column('password', String(255)),
    Column('first_name', String(25)),
    Column('last_name', String(25)),
    Column('address_one', String(255)),
    Column('address_two', String(255)),
    Column('postal_code', String(30)),
    Column('avatar_image', String(255))
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
