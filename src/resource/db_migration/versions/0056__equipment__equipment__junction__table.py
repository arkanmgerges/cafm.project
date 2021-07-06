from sqlalchemy import *

meta = MetaData()

tbl = Table(
    "equipment__equipment__junction",
    meta,
    Column("id", Integer, primary_key=True),
    Column(
        "src_equipment_id",
        String(40),
        ForeignKey(
            "equipment.id",
            name="fk__src__equipment__equipment__junction__equipment__id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
    Column(
        "dst_equipment_id",
        String(40),
        ForeignKey(
            "equipment.id",
            name="fk__dst__equipment__equipment__junction__equipment__id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    _t = Table("equipment", meta, autoload=True)
    Index("ix__src__equipment__equipment__junction__equipment_id", tbl.columns.src_equipment_id)
    Index(
        "ix__dst__equipment__equipment__junction__equipment_id",
        tbl.columns.dst_equipment_id,
    )
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
