from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    "equipment_input",
    meta,
    Column("id", String(40), primary_key=True),
    Column("name", String(40)),
    Column("value", String(40)),
    Column(
        "unit_id",
        String(40),
        ForeignKey(
            "unit.id",
            name="fk__equipment_input__unit__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column(
        "equipment_id",
        String(40),
        ForeignKey(
            "equipment.id",
            name="fk__equipment_input__equipment__id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column("name", String(40)),
    Column("modified_at", DateTime),
    Column("created_at", DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    Table("unit", meta, autoload=True)
    Table("equipment", meta, autoload=True)
    Index("ix__equipment_input__unit_id", tbl.c.unit_id)
    Index("ix__equipment_input__equipment_id", tbl.c.equipment_id)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
