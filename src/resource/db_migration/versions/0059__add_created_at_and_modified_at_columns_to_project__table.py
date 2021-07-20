from sqlalchemy import *
from migrate import *


def upgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    tbl = Table("project", meta, autoload=True)
    modifiedAt = Column("modified_at", DateTime)
    createdAt = Column("created_at", DateTime)
    modifiedAt.create(tbl)
    createdAt.create(tbl)
    Index("ix__project__modified_at", tbl.columns.modified_at).create()
    Index("ix__project__created_at", tbl.columns.created_at).create()


def downgrade(migrate_engine):
    meta = MetaData(bind=migrate_engine)
    tbl = Table("project", meta, autoload=True)
    tbl.c.modified_at.drop()
    tbl.c.created_at.drop()