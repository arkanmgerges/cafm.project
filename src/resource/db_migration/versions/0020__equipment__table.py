from sqlalchemy import *
from migrate import *

meta = MetaData()

tbl = Table(
    "equipment",
    meta,
    Column("id", String(40), primary_key=True),
    Column("name", String(40)),
    Column("quantity", Integer),
    Column(
        "project_id",
        String(40),
        ForeignKey(
            "project.id",
            name="fk__equipment__project__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column(
        "equipment_project_category_id",
        String(40),
        ForeignKey(
            "equipment_project_category.id",
            name="fk__equipment__equipment_project_category__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column(
        "equipment_category_id",
        String(40),
        ForeignKey(
            "equipment_category.id",
            name="fk__equipment__equipment_category__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column(
        "equipment_category_group_id",
        String(40),
        ForeignKey(
            "equipment_category_group.id",
            name="fk__equipment__equipment_category_group__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column(
        "building_id",
        String(40),
        ForeignKey(
            "building.id",
            name="fk__equipment__building__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column(
        "building_level_id",
        String(40),
        ForeignKey(
            "building_level.id",
            name="fk__equipment__building_level__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column(
        "building_level_room_id",
        String(40),
        ForeignKey(
            "building_level_room.id",
            name="fk__equipment__building_level_room__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column(
        "manufacturer_id",
        String(40),
        ForeignKey(
            "manufacturer.id",
            name="fk__equipment__manufacturer__id",
            onupdate="CASCADE",
        ),
        nullable=True,
    ),
    Column(
        "equipment_model_id",
        String(40),
        ForeignKey(
            "equipment_model.id",
            name="fk__equipment__equipment_model__id",
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
    Table("project", meta, autoload=True)
    Table("equipment_project_category", meta, autoload=True)
    Table("equipment_category", meta, autoload=True)
    Table("equipment_category_group", meta, autoload=True)
    Table("building", meta, autoload=True)
    Table("building_level", meta, autoload=True)
    Table("building_level_room", meta, autoload=True)
    Table("manufacturer", meta, autoload=True)
    Table("equipment_model", meta, autoload=True)

    Index("ix__equipment__project_id", tbl.c.project_id)
    Index(
        "ix__equipment__equipment_project_category_id",
        tbl.c.equipment_project_category_id,
    )
    Index("ix__equipment__equipment_category_id", tbl.c.equipment_category_id)
    Index(
        "ix__equipment__equipment_category_group_id", tbl.c.equipment_category_group_id
    )
    Index("ix__equipment__building_id", tbl.c.building_id)
    Index("ix__equipment__building_level_id", tbl.c.building_level_id)
    Index("ix__equipment__building_level_room_id", tbl.c.building_level_room_id)
    Index("ix__equipment__manufacturer_id", tbl.c.manufacturer_id)
    Index("ix__equipment__equipment_model_id", tbl.c.equipment_model_id)
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
