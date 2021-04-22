from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    "building__level__junction",
    meta,
    Column("id", Integer, primary_key=True),
    Column(
        "building_id",
        String(40),
        ForeignKey(
            "building.id",
            name="fk__building__level__junction__building__id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
    Column(
        "building_level_id",
        String(40),
        ForeignKey(
            "building_level.id",
            name="fk__building__level__junction__building_level__id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    _t = Table("building", meta, autoload=True)
    _t = Table("building_level", meta, autoload=True)
    Index("ix__building__level__junction__building_id", tbl.c.building_id)
    Index("ix__building__level__junction__building_level_id", tbl.c.building_level_id)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
