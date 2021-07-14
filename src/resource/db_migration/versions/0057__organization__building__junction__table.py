from sqlalchemy import *

meta = MetaData()

tbl = Table(
    "organization__building__junction",
    meta,
    Column("id", Integer, primary_key=True),
    Column(
        "organization_id",
        String(40),
        ForeignKey(
            "organization.id",
            name="fk__organization__building__junction__organization_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
    Column(
        "project_id",
        String(40),
        ForeignKey(
            "project.id",
            name="fk__organization__building__junction__project_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
    Column(
        "building_id",
        String(40),
        ForeignKey(
            "building.id",
            name="fk__organization__building__junction__building_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
    Column(
        "building_level_id",
        String(40),
        ForeignKey(
            "building_level.id",
            name="fk__organization__building__junction__building_level_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
    Column(
        "building_level_room_id",
        String(40),
        ForeignKey(
            "building_level_room.id",
            name="fk__organization__building__junction__building_level_room_id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    _t = Table("organization", meta, autoload=True)
    _t = Table("project", meta, autoload=True)
    _t = Table("building", meta, autoload=True)
    _t = Table("building_level", meta, autoload=True)
    _t = Table("building_level_room", meta, autoload=True)

    Index(
        "ix__organization__building__junction__organization_id",
        tbl.columns.organization_id)
    Index(
        "ix__organization__building__junction__project_id",
        tbl.columns.project_id)
    Index(
        "ix__organization__building__junction__building_id",
        tbl.columns.building_id,
    )
    Index(
        "ix__organization__building__junction__building_level_id",
        tbl.columns.building_level_id)
    Index(
        "ix__organization__building__junction__building_level_room_id",
        tbl.columns.building_level_room_id,
    )
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
