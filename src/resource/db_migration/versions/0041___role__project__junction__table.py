from sqlalchemy import *

meta = MetaData()

tbl = Table(
    "role__project__junction",
    meta,
    Column("id", Integer, primary_key=True),
    Column(
        "role_id",
        String(40),
        ForeignKey(
            "role.id",
            name="fk__role__project__junction__role__id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
    Column(
        "project_id",
        String(40),
        ForeignKey(
            "project.id",
            name="fk__role__project__junction__project__id",
            ondelete="CASCADE",
            onupdate="CASCADE",
        ),
    ),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    _t = Table("role", meta, autoload=True)
    _t = Table("project", meta, autoload=True)
    Index("ix__role__project__junction__role_id", tbl.columns.role_id)
    Index(
        "ix__role__project__junction__project_id",
        tbl.columns.project_id,
    )
    tbl.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    tbl.drop()
