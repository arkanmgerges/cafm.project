from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta = MetaData(bind=migrate_engine)
    tbl = Table('subcontractor', meta, autoload=True)
    tbl.c.contact_person.alter(type=String(255))


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta = MetaData(bind=migrate_engine)
    tbl = Table('subcontractor', meta, autoload=True)
    tbl.c.contact_person.alter(type=String(40))
