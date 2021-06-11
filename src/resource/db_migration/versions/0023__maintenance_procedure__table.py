from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    "maintenance_procedure",
    meta,
    Column("id", String(40), primary_key=True),
    Column("name", String(255)),
    Column("type", String(40)),
    Column("frequency", String(40)),
    Column("start_date", DateTime, nullable=True),
    Column("subcontractor_id", String(40)),
    Column("sub_type", String(40)),
    Column(
        "equipment_id",
        String(40),
        ForeignKey(
            "equipment.id",
            name="fk__maintenance_procedure__equipment__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column("modified_at", DateTime),
    Column("created_at", DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    Table("equipment", meta, autoload=True)
    Index("ix__maintenance_proc__equip_id", tbl.c.equipment_id)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
