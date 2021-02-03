from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    'building_level_room', meta,
    Column('id', String(40), primary_key=True),
    Column('name', String(40)),
    Column('description', String(255)),
    Column('index', Integer),
    Column('building_level_id', String(40), ForeignKey('building_level.id', ondelete='CASCADE'), nullable=False),
    Column('modified_at', DateTime),
    Column('created_at', DateTime)
)

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    _t = Table('building_level', meta, autoload=True)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
