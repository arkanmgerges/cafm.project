from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    "standard_equipment_category_group",
    meta,
    Column("id", String(40), primary_key=True),
    Column(
        "standard_equipment_category_id",
        String(40),
        ForeignKey(
            "standard_equipment_category.id",
            name="fk__standard_eq_category_group__standard_eq_category__id",
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
    _t = Table("standard_equipment_category", meta, autoload=True)
    Index(
        "ix__standard_eq_category_group__standard_eq_category_id",
        tbl.c.standard_equipment_category_id,
    )
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
