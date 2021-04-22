from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    "project",
    meta,
    Column("id", String(40), primary_key=True),
    Column("name", String(40)),
    Column("city_id", Integer),
    Column("country_id", Integer),
    Column("address_line", String(256)),
    Column("beneficiary_id", String(40)),
    Column("start_date", DateTime, nullable=True),
    Column("state", String(50)),
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
