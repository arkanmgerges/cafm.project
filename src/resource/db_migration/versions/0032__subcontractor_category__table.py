from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    "subcontractor_category",
    meta,
    Column("id", String(40), primary_key=True),
    Column("name", String(40)),
    Column("modified_at", DateTime),
    Column("created_at", DateTime),
)


def upgrade(migrate_engine):
    meta.bind = migrate_engine
    tbl.create()


def downgrade(migrate_engine):
    meta.bind = migrate_engine
    tbl.drop()
