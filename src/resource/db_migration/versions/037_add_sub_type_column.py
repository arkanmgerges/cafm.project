from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta = MetaData(bind=migrate_engine)
    tbl = Table('maintenance_procedure', meta, autoload=True)
    col = Column('sub_type', String(40))
    col.create(tbl)


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta = MetaData(bind=migrate_engine)
    tbl = Table('maintenance_procedure', meta, autoload=True)
    tbl.c.sub_type.drop()
