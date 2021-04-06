from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    'role', meta,
    Column('id', String(40), primary_key=True),
    Column('name', String(50)),
    Column('modified_at', DateTime),
    Column('created_at', DateTime),
    Column('title', String(255))
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