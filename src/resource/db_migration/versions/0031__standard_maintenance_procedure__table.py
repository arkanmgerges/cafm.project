from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    "standard_maintenance_procedure",
    meta,
    Column("id", String(40), primary_key=True),
    Column("name", String(255)),
    Column("type", String(40)),
    Column("subtype", String(40)),
    Column("frequency", String(40)),
    Column("start_date", DateTime, nullable=True),
    Column(
        "standard_equipment_category_group_id",
        String(40),
        ForeignKey(
            "standard_equipment_category_group.id",
            name="fk__std_maintenance_proc__std_eq_cat_grp__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column(
        "organization_id",
        String(40),
        ForeignKey(
            "organization.id",
            name="fk__standard_maintenance_procedure__organization__id",
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
    Table("organization", meta, autoload=True)
    Table("standard_equipment_category_group", meta, autoload=True)
    Index("ix__standard_maintenance_proc__org_id", tbl.c.organization_id)
    Index("ix__standard_maintenance_proc__std_eq_cat_grp_id", tbl.c.standard_equipment_category_group_id)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
