from sqlalchemy import *


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta = MetaData(bind=migrate_engine)
    tbl = Table('role', meta, autoload=True)
    col = Column('title', String(50))
    col.create(tbl)


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta = MetaData(bind=migrate_engine)
    tbl = Table('role', meta, autoload=True)
    tbl.c.title.drop()
