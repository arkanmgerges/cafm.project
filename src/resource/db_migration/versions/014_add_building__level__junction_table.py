from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    'building__level__junction', meta,
    Column('id', Integer, primary_key=True),
    Column('building_id', String(40), ForeignKey('building.id'), index=True),
    Column('building_level_id', String(40), ForeignKey('building_level.id'), index=True)
)

def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    _t = Table('building', meta, autoload=True)
    _t = Table('building_level', meta, autoload=True)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
