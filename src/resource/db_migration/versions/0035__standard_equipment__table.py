from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    "standard_equipment",
    meta,
    Column("id", String(40), primary_key=True),
    Column("name", String(40)),
    Column(
        "standard_equipment_category_id",
        String(40),
        ForeignKey(
            "standard_equipment_category.id",
            name="fk__standard_equipment__standard_equipment_category__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column(
        "standard_equipment_category_group_id",
        String(40),
        ForeignKey(
            "standard_equipment_category_group.id",
            name="fk__standard_equipment__standard_equipment_category_group__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column(
        "manufacturer_id",
        String(40),
        ForeignKey(
            "manufacturer.id",
            name="fk__standard_equipment__manufacturer__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column(
        "equipment_model_id",
        String(40),
        ForeignKey(
            "equipment_model.id",
            name="fk__standard_equipment__equipment_model__id",
            ondelete="CASCADE",
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
    Table("standard_equipment_category", meta, autoload=True)
    Table("standard_equipment_category_group", meta, autoload=True)
    Table("manufacturer", meta, autoload=True)
    Table("equipment_model", meta, autoload=True)

    Index(
        "ix__standard_equipment__standard_equipment_category_id",
        tbl.c.standard_equipment_category_id,
    )
    Index(
        "ix__standard_equipment__standard_equipment_category_group_id",
        tbl.c.standard_equipment_category_group_id,
    )
    Index("ix__standard_equipment__manufacturer_id", tbl.c.manufacturer_id)
    Index("ix__standard_equipment__equipment_model_id", tbl.c.equipment_model_id)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
